#!/usr/bin/env python
# coding: utf-8


"""
2021/07/21
author:guisen chen
email:thecgs001@foxmail.com
"""
import re
import argparse

parser = argparse.ArgumentParser(description='将kofamscan结果与ko00001.keg连接重构，得到pathway与annotation',usage='python3 kofamscan_plus.py -K [ko00001.keg] -i [input] -o [output]',add_help=False,epilog='date:2021/07/21 author:guisen chen email:thecgs001@foxmail.com')
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument('-K','--Keg',metavar='[file.keg]',help='file.keg',required=True)
required.add_argument('-i','--input',metavar='[input_file]',help='input_file',required=True)
required.add_argument('-o','--output',metavar='[output_file]',help='output_file',required=True)
optional.add_argument('-h','--help',action='help',help='show this help message and exit')
optional.add_argument('-v','--version',action='version',version='v1.00')
args = parser.parse_args()

#ko00001.keg https://www.genome.jp/kegg-bin/download_htext?htext=ko00001.keg&format=htext&filedir=
#KEGG_Orthology = open('/home/guisen/ko00001.keg','r')
#input = open('/home/guisen/kegg.txt','r')
#output = open('/home/guisen/kegg.anno.txt','w')
KEGG_Orthology = open(args.Keg,'r')
input = open(args.input,'r')
output = open(args.output,'w')
header = 'gene_id' + '\t' + 'K_id' + '\t' + 'kegg_annotation' +'\t'+ 'ko_id' + '\t'+ 'pathway'+'\t'+ 'B_num' + '\t' + 'B_level' + '\t' + 'A_num' + '\t' + 'A_level' + '\n'
output.write(header)

A_level = {}
B_level = {}
C_level = {} #pathway
D_level = {} #K
A_B = {}
B_C = {}
C_D = {}

for line in KEGG_Orthology:
    if(line[0] == 'A'):
        if re.search('\d+',line):
            A_num = re.search('\d+',line).group(0)
            A_anno = re.search('A\d+\s+(.*)',line).group(1).strip()
            A_level.setdefault(A_num,set()).add(A_anno)   
    if(line[0] == 'B'):
        if re.search('\d+',line):
            B_num = re.search('\d+',line).group(0)
            B_anno = re.search('B\s+\d+\s+(.*)',line).group(1).strip()
            B_level.setdefault(B_num,set()).add(B_anno)
            A_B.setdefault(A_num,set()).add(B_num)
    if(line[0] == 'C'):
        C_num = re.search('\d+',line).group(0)
        C_anno = re.search('C\s+\d+\s+([^[]*)',line).group(1).strip()
        C_level.setdefault(f"ko{C_num}",set()).add(C_anno)
        B_C.setdefault(B_num,set()).add(f"ko{C_num}")
    if(line[0] == 'D'):
        D_num = re.search('K\d+',line).group(0)
        D_anno = re.search('D\s+K\d+(.*)',line).group(1).strip()
        D_level.setdefault(D_num, set()).add(D_anno)
        C_D.setdefault(f"ko{C_num}", set()).add(D_num)

#print(A_B)
#print(B_C)
#print(C_D)

for line in input:
    if re.search('K\d+',line):
        K_num = line.split('\t')[1].split('\n')[0]
        for ko,K in C_D.items():
            for B,C in B_C.items():
                if(ko in C):
                    B_num = B
                for A,B in A_B.items():
                    if (B_num in B):
                        A_num = A
            if(K_num in K):
                l = line.split('\n')[0]+ '\t' + list(D_level[K_num])[0] +'\t' + ko + '\t' + list(C_level[ko])[0] + '\t' + B_num + '\t' + list(B_level[B_num])[0] + '\t' + A_num + '\t' + list(A_level[A_num])[0] + '\n'
                output.write(l)

print('finished')

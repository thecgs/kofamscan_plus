# **kopfamscan_plus**

**A pipline of KEGG annotation**

**Author:** guisen chen  |  **Email:** <thecgs001@foxmail.com>

## Example:

```bash
$ head id.txt
evm.model.CM018427.2.26 K16479
evm.model.CM018427.2.260        K00746
evm.model.CM018427.2.262        K17609
evm.model.CM018427.2.263        K04545
evm.model.CM018427.2.264        K09783
evm.model.CM018427.2.265        K08397
evm.model.CM018427.2.266        K15378
evm.model.CM018427.2.267        K01796
evm.model.CM018427.2.268        K12384
evm.model.CM018427.2.269        K14308
$ head ko00001.keg
+D      KO
#<h2><a href="/kegg/brite.html"><img src="/Fig/bget/kegg3.gif" align="middle" border=0></a> &nbsp; KEGG Orthology (KO)</h2>
!
A09100 Metabolism
B
B  09101 Carbohydrate metabolism
C    00010 Glycolysis / Gluconeogenesis [PATH:ko00010]
D      K00844  HK; hexokinase [EC:2.7.1.1]
D      K12407  GCK; glucokinase [EC:2.7.1.2]
D      K00845  glk; glucokinase [EC:2.7.1.2]
$ head kegg.xls
gene_id K_id    kegg_annotation ko_id   pathway B_num   B_level A_num   A_level
evm.model.CM018427.2.26 K16479  ODF2; outer dense fiber protein 2       ko03036C                            hromosome and associated proteins       09182   Protein families: genetic inform                            ation processing        09180   Brite Hierarchies
evm.model.CM018427.2.260        K00746  CSGALNACT1_2; chondroitin sulfate N-acet                            ylgalactosaminyltransferase 1/2 [EC:2.4.1.174 2.4.1.175]        ko00532 Glycosam                            inoglycan biosynthesis - chondroitin sulfate / dermatan sulfate 09107   Glycan b                            iosynthesis and metabolism      09100   Metabolism
evm.model.CM018427.2.260        K00746  CSGALNACT1_2; chondroitin sulfate N-acet                            ylgalactosaminyltransferase 1/2 [EC:2.4.1.174 2.4.1.175]        ko01003 Glycosyl                            transferases    09181   Protein families: metabolism    09180   Brite Hierarchie                            s
evm.model.CM018427.2.262        K17609  NXN; nucleoredoxin [EC:1.8.1.8] ko01009P                            rotein phosphatases and associated proteins     09181   Protein families: metabo                            lism    09180   Brite Hierarchies
evm.model.CM018427.2.263        K04545  GNG10; guanine nucleotide-binding protei                            n G(I)/G(S)/G(O) subunit gamma-10       ko04014 Ras signaling pathway   09132  S                            ignal transduction      09130   Environmental Information Processing
evm.model.CM018427.2.263        K04545  GNG10; guanine nucleotide-binding protei                            n G(I)/G(S)/G(O) subunit gamma-10       ko04371 Apelin signaling pathway       0                            9132    Signal transduction     09130   Environmental Information Processing
evm.model.CM018427.2.263        K04545  GNG10; guanine nucleotide-binding protei                            n G(I)/G(S)/G(O) subunit gamma-10       ko04151 PI3K-Akt signaling pathway     0                            9132    Signal transduction     09130   Environmental Information Processing
evm.model.CM018427.2.263        K04545  GNG10; guanine nucleotide-binding protei                            n G(I)/G(S)/G(O) subunit gamma-10       ko04062 Chemokine signaling pathway    0                            9151    Immune system   09150   Organismal Systems
evm.model.CM018427.2.263        K04545  GNG10; guanine nucleotide-binding protei                            n G(I)/G(S)/G(O) subunit gamma-10       ko04926 Relaxin signaling pathway      0                            9152    Endocrine system        09150   Organismal Systems
```



## Used:

```bash
$ python3 kofamscan_plus.py -K ko00001.keg -i id.txt -o kegg.xls
```

## **Note:**

Click here to download the latest [ko00001.keg](https://www.genome.jp/kegg-bin/download_htext?htext=ko00001&format=htext&filedir=) or [br08901.keg](https://www.kegg.jp/kegg-bin/download_htext?htext=br08901.keg&format=htext&filedir=).

This script is used to parse kofamscan software results. 

Learn more, click here to [kofamscan](https://www.genome.jp/ftp/tools/kofam_scan/) software and [kofam](https://www.genome.jp/ftp/db/kofam/) database.


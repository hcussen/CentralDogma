# The Central Dogma

The Central Dogma of biology explains the flow of information from DNA, transcription into RNA, and translation into protein. I wrote this utility to help me with my Genetics homework. Writing this definetly took longer than doing the translations by hand, but it was a fun project. I haven't written Python code in a while, so remembering how to create command-line interactions was useful.

## What did I learn?

The biggest challenge I encountered was getting the codon mappings into a form that was readable by the computer. When I got the codon table from [genscript.com](https://www.genscript.com/tools/codon-table), copy-pasting it into a text file gave me a file that was in an unhelpful form (see resources/codontable.txt). So I wrote a bash script to transform it.

## Future Plans

- [ ] finish reading `transformed-codontable.tsv` into the tRNA mapping, finalize main.py
- [ ] create setup script
- [ ] add DNA -> RNA option
- [ ] add Protein -> DNA option
- [ ] add alternative codon -> Amino Acid mappings, with scripting setup support

## Setup

Run `python3 main.py`.
The `transformCodonTable` scripts have already bene run and their output added to the repo, but you should re-run it if you change the codon mapping text files.

## Sources

Codon table - (https://www.genscript.com/tools/codon-table)

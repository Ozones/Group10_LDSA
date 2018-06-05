#!/bin/bash
# A simple bash script for dublicating the data
yes ~/data/pdb_seqres.txt | head -n 2 | xargs cat > ~/data/pdb_seqres2.txt
echo "Made 2x dublicate"
yes ~/data/pdb_seqres.txt | head -n 3 | xargs cat > ~/data/pdb_seqres3.txt
echo "Made 3x dublicate"
yes ~/data/pdb_seqres.txt | head -n 4 | xargs cat > ~/data/pdb_seqres4.txt
echo "Made 4x dublicate"
yes ~/data/pdb_seqres.txt | head -n 5 | xargs cat > ~/data/pdb_seqres5.txt
echo "Made 5x dublicate"
yes ~/data/pdb_seqres.txt | head -n 6 | xargs cat > ~/data/pdb_seqres6.txt
echo "Made 6x dublicate"
yes ~/data/pdb_seqres.txt | head -n 7 | xargs cat > ~/data/pdb_seqres7.txt
echo "Made 7x dublicate"
yes ~/data/pdb_seqres.txt | head -n 8 | xargs cat > ~/data/pdb_seqres8.txt
echo "Made 8x dublicate"
yes ~/data/pdb_seqres.txt | head -n 9 | xargs cat > ~/data/pdb_seqres9.txt
echo "Made 9x dublicate"
yes ~/data/pdb_seqres.txt | head -n 10 | xargs cat > ~/data/pdb_seqres10.txt
echo "Made 10x dublicate"

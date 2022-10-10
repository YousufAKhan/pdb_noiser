# pdb_noiser

## Package requirements

-Biopython

-numpy

-os

-sys


## Summary

This is a file that will add noise to of user specified amount (in angstroms) to a PDB file and generate N number of noised PDB files
The arguments to enter are the following in order are
      input_file
      output_dir
      noise
      n
For example, python3 ./add_noise.py ./structures/c7_aligned.pdb ./test_noise 1 100 is an argument that will generate 100 PDBs with a 1 angstrom 
addition of noise to each atom to the c7_aligned.pdb file and output the files in the test_noise directory

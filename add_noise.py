#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import sys
from Bio.PDB import *
import numpy as np
parser = PDBParser()


# In[5]:


def generate_random_splits(noise_size):
    """
    Description:
        Generate a list of noise [x,y,z] to add to an atom coordinate
    Input:
        -noise_size: The amount of total noise desired in angstroms
    Returns:
        -noise_add: A list [x,y,z] of the noise to add to a coordinate
    """
    x_rand = np.random.uniform()
    y_rand = np.random.uniform()
    z_rand = np.random.uniform()
    sum_rand = x_rand + y_rand + z_rand
    factor = noise_size / sum_rand
    x_scale = x_rand * factor
    y_scale = y_rand * factor
    z_scale = z_rand * factor
    noise_add = [x_scale, y_scale, z_scale]
    return noise_add


# In[ ]:


def generate_noised_pdb(structure_path, noise, path, n):
    """
    Description:
        Write noised PDB file to the output path
    Input:
        -structure_path: The path to the structure
        -noise: The amount of noise (angstroms) that is desired
        -path: The output directory
        -n: The amount of noised PDB files to generate
    Returns:
    """
    for i in range(n):
        structure = parser.get_structure("structure", structure_path)
        print('Processing '+str(i)+' out of '+str(n))
        for model in structure:
            for chain in model:
                for res in chain:
                    for atom in res:
                        atom.set_coord(atom.coord + generate_random_splits(noise))
        io = PDBIO()
        io.set_structure(structure)
        filename = str(structure.id)+'_noised_'+str(i)+'.pdb'
        fp = os.path.join(path,filename)
        io.save(fp)


# In[ ]:


def main():
    # Take the inputs
    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    noise = float(sys.argv[3])
    n = int(sys.argv[4])
    generate_noised_pdb(input_file, noise, output_dir, n)


# In[ ]:


if __name__ == "__main__":
    main()


# Black_Hole_Mergers_Cosmology
Studies effects on cosmology of conversion of matter to radiation via black hole mergers.

The main code first computes H(z) numerically and analytically for Lambda-CDM so you can see the excellent match. 

You will need to install the necessary fonts and change the variable : path personal_path = "/home/hoelsczj/Library/static/" to your personal path,
or change the fonts used so this is not an issue. 

The code uses a brute force grid search to find initial values for the parameter fitting algorithm. This is slow, and means the entire notebook will likely
take a few hours to run on a laptop, if you choose to run it. 

The notebook (Black_Hole_Merger_Pipeline.ipynb) produces the results in our manuscript for the case of SMBH-SMBH mergers, SMBH formation from PBHs, and solar-mass black hole mergers. 

# Black_Hole_Mergers_Cosmology
Studies effects on cosmology from conversion of matter to radiation via black hole mergers.



***Notebook Black_Hole_Merger_Pipeline.ipynb : 

This main code first computes H(z) numerically and analytically for Lambda-CDM so you can see the excellent match. 

You will need to install the necessary fonts and change the variable : path personal_path = "/home/hoelsczj/Library/static/" to your personal path,
or change the fonts used so this is not an issue. 

The code uses a brute force grid search to find initial values for the parameter fitting algorithm. This is slow, and means the entire notebook will likely
take a few hours to run on a laptop, if you choose to run it. 

The notebook produces the results in our manuscript for the case of SMBH-SMBH mergers, SMBH formation from PBHs, and solar-mass black hole mergers. 



*** Python script CMB_SMBH_Formation.py : 

This generates a CMB power spectrum plot for Lambda-CDM (no conversion of matter to GW) and for a case where we have SMBH formation from PBH mergers, but have
restricted the comoving SMBH formation rate so that SMBHs are not overproduced. One can see a small ISW effect at low multipole moment. The plot this produces
is in this repo, though if you wish to run the code, you will need to install CLASS. 

import numpy as np
import matplotlib.pyplot as plt
from classy import Class

# Set matplotlib backend
plt.switch_backend('Agg')

base_params = {
    'omega_b': 0.02237,
    'omega_cdm': 0.12,
    'omega_ini_dcdm': 0.0,
    'T_cmb': 2.7255,
    'N_ur': 3.046,
    'z_reio': 7.67,
    'A_s': 2.1e-9,
    'n_s': 0.9649,
    'output': 'tCl,pCl,lCl,mPk,mTk',
    'l_max_scalars': 2500,
    'lensing': 'yes',
    'format': 'camb',
    'write background': 'yes',
    'background_verbose': 3,
    'perturbations_verbose': 2,
    'thermodynamics_verbose': 2
}

h_values = np.array([0.674,0.7185]) #Lambda - CDM value, and the value from the fit 

# Lists to store power spectra 
cl_tt_list = []
ell = None

# Loop over input values
for index in range(len(h_values)):
    # Update parameters 
    params = base_params.copy()
    params.update({
        'h': h_values[index]})

    # Initialize CLASS
    cosmo = Class()
    try:
        cosmo.set(params)
        cosmo.compute()
    except Exception as e:
        print(f"CLASS error: {e}")
        cosmo.struct_cleanup()
        cosmo.empty()
        continue

    # Get CMB power spectrum
    cls = cosmo.lensed_cl(2500)
    ell = cls['ell']
    T_cmb = 2.7255  # CMB temperature in K
    cl_tt = cls['tt'] * (ell * (ell + 1)) / (2 * np.pi) * (T_cmb * 1e6)**2  # Convert to μK^2, T_cmb part needed to scale it properly 
    # Store the power spectra
    cl_tt_list.append(cl_tt)
    # Clean up
    cosmo.struct_cleanup()
    cosmo.empty()

# Plot 1: TT Power spectrum
plt.figure(figsize=(10, 8))
colors = ['blue', 'red']
for i, (h, cl_tt) in enumerate(zip(h_values, cl_tt_list)):
    plt.plot(ell[2:], cl_tt[2:], color=colors[i])
plt.xscale('log')
plt.yscale('linear')
plt.xlabel(r'$\ell$')
plt.ylabel(r'$\ell(\ell+1)C_\ell^{TT}/2\pi$ [$\mu$K$^2$]')
plt.title('CMB Temp. Power Spectrum (Blue = No Matter Converted to GW)')
plt.legend()
plt.grid(True)
plt.savefig('cmb_power_SMBH_formation.png')

import numpy as np
import copy as cp


def metropolis_montecarlo(ham, conf, T=1, nsweep=1000, nburn=100):
    """Run montecarlo with metropolis sampling for the Hamiltonian

    Parameters
    ----------
    ham: IsingHamiltonian, required 
    conf: BitString, required
        configuration - probably not needed 
    T: float, optional
        Temperature 

    Returns
    E_samples: np.array
        Running average of the energy samples collected
    M_samples: np.array
        Running average of the magnetization samples collected
    EE_samples: np.array
        Running average of the energy^2 samples collected
    MM_samples: np.array
        Running average of the magnetization^2 samples collected
    -------
    """
    E_samples = np.zeros(nsweep)
    M_samples = np.zeros(nsweep)
    EE_samples = np.zeros(nsweep)
    MM_samples = np.zeros(nsweep)

    # thermalization
    for si in range(nburn):
        ham.metropolis_sweep(conf, T=T)

    # accumulation
    ham.metropolis_sweep(conf, T=T)
    Ei = ham.energy(conf)
    Mi = conf.get_magnetization()
    M_samples[0] = Mi
    E_samples[0] = Ei
    MM_samples[0] = Mi * Mi
    EE_samples[0] = Ei * Ei
    for si in range(1, nsweep):
        ham.metropolis_sweep(conf, T=T)
        Ei = ham.energy(conf)
        Mi = conf.get_magnetization()

        # E_samples[si]  = Ei
        # EE_samples[si]  = Ei*Ei
        E_samples[si] = (E_samples[si - 1] * (si) + Ei) / (si + 1)
        EE_samples[si] = (EE_samples[si - 1] * (si) + Ei * Ei) / (si + 1)

        # M_samples[si]  = Mi
        # MM_samples[si]  = Mi*Mi
        M_samples[si] = (M_samples[si - 1] * (si) + Mi) / (si + 1)
        MM_samples[si] = (MM_samples[si - 1] * (si) + Mi * Mi) / (si + 1)

    return E_samples, M_samples, EE_samples, MM_samples

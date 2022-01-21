import numpy as np
import random
import copy as cp

class SpinConfig:
    """
    Base class for different types of spin configurations (i.e., 1D, 2D, etc)
    """
    def __init__(self):
        print(" Why are you instantiating this?\n")



class SpinConfig1D(SpinConfig):
    """
    1-D spin configuration
    """
    def __init__(self, N=10, pbc=True):
        """
        Initialize instance

        Parameters
        ----------
        N   : int, default: 10
            Number of sites
        pbc : bool, default: true
            Should we use periodic boundary conditions?

        Returns
        -------
        """    
        self.config = np.zeros(N, dtype=int)
        self.N = N
        self.pbc = pbc

    def initialize(self, M=0):
        """
        Initialize spin configuration with specified magnetization
        
        Parameters
        ----------
        M   : Int, default: 0
            Total number of spin up sites 
        """
        self.config = np.zeros(self.N, dtype=int) 
        randomlist = random.sample(range(0, self.N-1), M)
        for i in randomlist:
            self.config[i] = 1

        print(" Initialized config to: ", self.config)

    def __getitem__(self,i):
        return self.config[i]

    def flip_site(self, i):
        """
        flip spin at site, i 
        
        Parameters
        ----------
        i   : int
            site to flip 
        """
        if self.config[i] == 1:
            self.config[i] = 0
        else:
            self.config[i] = 1
        

class IsingHamiltonian1D:
    """Class for 1D Hamiltonian
        
        .. math::
            H = -J\\sum_{\\left<ij\\right>} \\sigma_i\\sigma_j - \\mu\\sum_i h_i \\sigma_i

    Parameters
    ----------
    J: float, required
        Strength of coupling
    h: list[float], required
        Strength of onsite field 
    mu: float, required
        Chemical potential 
    pbc: bool, optional, default=true
        Do PBC?
    """
    def __init__(self, J, h, mu, pbc=True):
        self.J = J
        self.h = h
        self.mu = mu
        self.pbc = pbc

    def expectation_value(self, config):
        """Compute energy of configuration, `config` 
            
            .. math::
                E = \\left<\\hat{H}\\right> 

        Parameters
        ----------
        config   : SpinConfig1D
            input configuration 
        
        Returns
        -------
        energy  : float
            Energy of the input configuration
        """
        e = 0.0
        for i in range(config.N-1):
            if config[i] == config[i+1]:
                e -= self.J
            else:
                e += self.J
        if self.pbc:
            if config[config.N-1] == config[0]:
                e -= self.J
            else:
                e += self.J
        
        for i in range(config.N):
            if config[i]:
                e -= self.mu * self.h[i]
            else:
                e += self.mu * self.h[i]
        return e

    def delta_e_for_flip(self, i, config):
        """Compute the energy change incurred _if_ one were to flip the spin at site i

        Parameters
        ----------
        i        : int
            Index of site to flip
        config   : SpinConfig1D
            input configuration 
        
        Returns
        -------
        energy  : list[SpinConfig1D, float]
            Returns both the flipped config and the energy change
        """
        config_trial = cp.deepcopy(config) 
        config_trial.flip_site(i)
        return config_trial, self.expectation_value(config_trial) - self.expectation_value(config)




class tmp:
    """
    test class
    """
    def __init__(self):
        pass
    def print(self,a):
        """
        print for tmp class
        """
        print(a)

"""
montecarlo.py
Introduction to the Monte Carlo method

Handles the primary functions
"""
def canvas2(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote

def testa():
    """This is a conceptual class representation of a simple BLE device
    (GATT Server). It is essentially an extended combination of the
    :class:`bluepy.btle.Peripheral` and :class:`bluepy.btle.ScanEntry` classes

    :param client: A handle to the :class:`simpleble.SimpleBleClient` client
        object that detected the device
    :type client: class:`simpleble.SimpleBleClient`
    :param addr: Device MAC address, defaults to None
    :type addr: str, optional
    :param addrType: Device address type - one of ADDR_TYPE_PUBLIC or
        ADDR_TYPE_RANDOM, defaults to ADDR_TYPE_PUBLIC
    :type addrType: str, optional
    :param iface: Bluetooth interface number (0 = /dev/hci0) used for the
        connection, defaults to 0
    :type iface: int, optional
    :param data: A list of tuples (adtype, description, value) containing the
        AD type code, human-readable description and value for all available
        advertising data items, defaults to None
    :type data: list, optional
    :param rssi: Received Signal Strength Indication for the last received
        broadcast from the device. This is an integer value measured in dB,
        where 0 dB is the maximum (theoretical) signal strength, and more
        negative numbers indicate a weaker signal, defaults to 0
    :type rssi: int, optional
    :param connectable: `True` if the device supports connections, and `False`
        otherwise (typically used for advertising ‘beacons’).,
        defaults to `False`
    :type connectable: bool, optional
    :param updateCount: Integer count of the number of advertising packets
        received from the device so far, defaults to 0
    :type updateCount: int, optional
    """
    print(" testa\n")


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())



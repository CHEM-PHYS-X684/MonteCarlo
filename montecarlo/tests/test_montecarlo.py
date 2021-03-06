"""
Unit and regression test for the montecarlo package.
"""

# Import package, test suite, and other packages as needed
import montecarlo
import pytest
import sys
import random
import numpy as np
import copy as cp

def test_montecarlo_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "montecarlo" in sys.modules


def testa():
    assert 1 == 1

def test_average_values():
    N=10
    conf = montecarlo.SpinConfig1D(N=N)
    #conf.initialize(M=20)
    ham = montecarlo.IsingHamiltonian1D(J=-1.0, mu=0.1)

    T = 2.0
    E, M, HC, MS = ham.compute_average_values(conf, T) 
    assert(np.isclose(E, -4.6378514858094695))
    assert(np.isclose(M, -0.1838233606011354 ))
    assert(np.isclose(HC, 1.9883833749653714 ))
    assert(np.isclose(MS, 1.8391722085614428))
     

def test_classes():
    random.seed(2)
    conf = montecarlo.SpinConfig1D(N=10)
    conf.initialize(M=5)
    assert(all(conf.config == [1, 1, 1, 0, 0, 0, 0, 1, 1, 0]))

    ham = montecarlo.IsingHamiltonian1D(1.0, -.001)

    e = ham.energy(conf)
    print(" Energy = ", e)
    assert(np.isclose(e,-2))

    conf.flip_site(3)
    print(conf.config)
    e = ham.energy(conf)
    print(" Energy = ", e)
    assert(np.isclose(e,-2.002))
    
    # now flip back
    conf.flip_site(3)
    print(conf.config)
    e = ham.energy(conf)
    print(" Energy = ", e)
    assert(np.isclose(e,-2.00))

    ham.mu = 1.1
    conf_old = cp.deepcopy(conf)
    ham.metropolis_sweep(conf, T=.9)
    print(conf_old, " --> ", conf)
    print("Energy: %12.8f --> %12.8f" %(e, ham.energy(conf)))  
    assert(all(conf.config == np.ones(10)))
    
    ham.mu = -0.1
    ham.J  = -1.0
    random.seed(2)
    conf.set_int_config(44)
    conf_old = cp.deepcopy(conf)
    ham.metropolis_sweep(conf, T=.9)
    print(conf_old, " --> ", conf)
    print("Energy: %12.8f --> %12.8f" %(e, ham.energy(conf)))  
    assert(all(conf.config == [1,0,1,0,1,0,0,1,1,0]))
    
    
if __name__== "__main__":
    test_montecarlo_imported()
    test_classes()
    test_average_values()


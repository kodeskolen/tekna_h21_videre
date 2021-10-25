# Evaluer denne cellen først for å kunne kjøre resten av koden i Notebooken.
from numpy import *
from scipy import signal
from numpy.random import rand
from IPython.display import Audio, display
from matplotlib.pyplot import *
from ipywidgets import interact

rate = 48000.0

# En hjelpefunksjon for avspilling av lydsignalene
def spill_av(lydsignal):
    display(Audio(lydsignal, rate=rate, autoplay=True))

# Lydgeneratorene
def sinus_generator(frekvens=440, varighet=1.0, amplitude=1.0):
    t = linspace(0., varighet, int(varighet * rate))
    sinusbølge = sin(frekvens * pi * 2 * t) * amplitude
    return sinusbølge

def sagtann_generator(frekvens=440, varighet=1.0, amplitude=1.0):
    t = linspace(0., varighet, int(varighet * rate))
    sagtannbølge = signal.sawtooth(frekvens * pi * 2 * t) * amplitude
    return sagtannbølge

def trekant_generator(frekvens=440, varighet=1.0, amplitude=1.0):
    t = linspace(0., varighet, int(varighet * rate))
    sagtannbølge = signal.sawtooth(frekvens * pi * 2 * t, 0.5) * amplitude
    return sagtannbølge

def hvit_støy_generator(varighet=1.0, amplitude=1.0):
    # Merk at støy ikke tar frekvensparameteret, siden støy ikke har en frekvens
    hvit_støy = rand(int(varighet * rate))
    hvit_støy = (hvit_støy * 2.0) - 1.0  # Skift signal fra [0,1] til [-1, 1]
    hvit_støy = hvit_støy * amplitude
    return hvit_støy

# Funksjon til å lage melodier
def lag_melodi(liste_med_signaler):
    return concatenate(liste_med_signaler)

# Pausegeneratoren
def pause_generator(varighet=1):
    return zeros(int(varighet * rate))

# Til bitredusering
def bitcrusher(signal, n):
    return array([int(sample * (2**n)) / (2**n) for sample in signal])

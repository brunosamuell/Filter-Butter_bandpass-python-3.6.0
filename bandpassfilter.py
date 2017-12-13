import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from numpy import cos, sin, pi, absolute, arange, array, append, abs, angle,\
                  fft, linspace, zeros, log10, unwrap
from scipy.signal  import kaiserord, lfilter, firwin, freqz, butter, lfilter
from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, \
                  axes, show, subplot, axis, plot

#function for sinusoidal generation
def sine_generator(fs, sinefreq, duration):
    T = duration
    nsamples = fs * T*10
    w = 2. * np.pi * sinefreq
    t_sine = np.linspace(0, T, nsamples, endpoint=False)
    y_sine = np.sin(w * t_sine)
    result = pd.DataFrame({ 
        'data' : y_sine} ,index=t_sine)
    return result

#function butter_bandpass
def butter_bandpass(lowcut, highcut, fs, order=3):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

#function butter_bandpass_filter
def butter_bandpass_filter(data, lowcut, highcut, fs, order=3):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    
    return y
#sample frequency
fps = 100

#Generating 100Hz signal
sine_fq = 100 #Hz
duration = 100 #seconds
sine_100Hz = sine_generator(fps,sine_fq,duration)

#Generating 50Hz signal
sine_fq = 50 #Hz
duration = 100 #seconds
sine_50Hz = sine_generator(fps,sine_fq,duration)

#Generating 17Hz signal
sine_fq = 17 #Hz
duration = 100 #seconds
sine_17Hz = sine_generator(fps,sine_fq,duration)

#Generating 10Hz signal
sine_fq = 10 #Hz
duration = 100 #seconds
sine_10Hz = sine_generator(fps,sine_fq,duration)

#Generating 1Hz signal
sine_fq = 1 #Hz
duration = 100 #seconds
sine_1Hz = sine_generator(fps,sine_fq,duration)

#Add the waves
sine = sine_100Hz + sine_50Hz + sine_17Hz + sine_10Hz + sine_1Hz 

#Select low and high cut frequencies
lowcut = 15
highcut = 18

#Calls the butter_bandpass_filter function and filters the generated signal
y = butter_bandpass_filter(sine.data, lowcut, highcut, fps, order=3)

#plots the generated signal
plt.figure(1)
plt.clf()
plt.plot(range(len(sine_17Hz)),sine_17Hz)
plt.title('17Hz signal generated')

#plots the desired signal
plt.figure(2)
plt.clf()
plt.plot(range(len(sine)),sine)
plt.title('Signal to be filtered')

#plots the filtered signal
plt.figure(3)
plt.clf()
plt.plot(range(len(y)),y)
plt.title('Filtered signal')
plt.show()

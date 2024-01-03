import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc, logfbank
import os


data_dir = 'Dataset/'
categories = [i for i in os.listdir('Dataset')]


for category in categories:
    path = os.path.join(data_dir,category)
    for audio in os.listdir(path):
        frequency_sampling, audio_signal = wavfile.read(os.path.join(path,audio))


        audio_signal = audio_signal[:15000]

        features_mfcc = mfcc(audio_signal, frequency_sampling)

        print('\nMFCC:\nNumber of windows =', features_mfcc.shape[0])
        print('Length of each feature =', features_mfcc.shape[1])



        features_mfcc = features_mfcc.T
        plt.matshow(features_mfcc)
        plt.title('MFCC')
        plt.savefig(f'figs/{audio}.png')

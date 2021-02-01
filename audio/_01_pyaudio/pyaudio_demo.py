# coding=utf-8
#================================================================
#
#   File name   : pyaudio_demo.py
#   Author      : Faye
#   Created date: 2021/1/19 16:20 
#   Description :
#
#================================================================

import wave
import pyaudio


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
channels=CHANNELS,
rate=RATE,
input=True,
frames_per_buffer=CHUNK)

print("* recording")
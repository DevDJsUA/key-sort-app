# -*- coding: utf-8 -*-
from typing import Any
import pyACA
import librosa
import configparser



def keyDetect(path):
	paths = path.split(".")
	format = paths[-1]

	y: Any
	sr: Any
	if format == "mp3":
		y, sr = librosa.load(path)
	elif format == "wav":
		y, sr = pyACA.ToolReadAudio(path)
	else:
		raise Exception(f"Not current format of file! {path} / {format}")
	
	key = pyACA.computeKey(y,sr)
	return key 

# cPath = "./test1.wav"
# y,sr = librosa.load("09.Liveon-qShe_Saw_Me.mp3")
# [f_s,afAudioData] = pyACA.ToolReadAudio(cPath)

	# compute feature
# [vsc,t] = pyACA.computeFeature("SpectralCentroid", afAudioData, f_s)
# [vsf,t] = pyACA.computeFeature("SpectralFlux", afAudioData, f_s)
# [vsc,t] = pyACA.computeKey(afAudioData, f_s)
# key = pyACA.computeKey(afAudioData, f_s)


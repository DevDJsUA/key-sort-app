# -*- coding: utf-8 -*-
from typing import Any
import djPyACA
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
		y, sr = djPyACA.ToolReadAudio(path)
	else:
		raise Exception(f"Not current format of file! {path} / {format}")
	
	key = djPyACA.computeKey(y,sr)
	return key 

# cPath = "./test1.wav"
# y,sr = librosa.load("09.Liveon-qShe_Saw_Me.mp3")
# [f_s,afAudioData] = djPyACA.ToolReadAudio(cPath)

	# compute feature
# [vsc,t] = djPyACA.computeFeature("SpectralCentroid", afAudioData, f_s)
# [vsf,t] = djPyACA.computeFeature("SpectralFlux", afAudioData, f_s)
# [vsc,t] = djPyACA.computeKey(afAudioData, f_s)
# key = djPyACA.computeKey(afAudioData, f_s)


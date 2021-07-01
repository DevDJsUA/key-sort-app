# from ...KeyDetect.keyDetect import 
from modules.KeyDetect.keyDetect import keyDetect
from ..classes.track import Track
from modules.sorts.keyDict import keyDict

import os

def initTracks(directory):
    files = os.listdir(directory)
    if '.DS_Store' in files:
        files.remove('.DS_Store')
    
    tracks = []

    for i in range(len(files)):
        trackName = files[i]
        trackNames = trackName.split('.')
        

        format = trackNames[-1]
        if format == 'mp3' or format == 'wav':
            path = directory + '/' + trackName
            key = keyDetect(path)
            # keys.append(dict[key])
            _track = Track(i, trackName, path, keyDict[key])
            tracks.append(_track)

    return tracks
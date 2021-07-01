def printTracks(tracks):
    for track in tracks:
        for i in range(10):
            print("-", end=" ")
        print(f"\n{track.getId()}\n{track.getName()}\n{track.getSrc()}\n{track.getKey()}")
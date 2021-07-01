from ..classes import Track

def hardcodeTracks():
    _track1 = Track(0,"track 0", "/track0", "10B")
    _track2 = Track(1,"track 1", "/track1", "10B")
    _track3 = Track(2,"track 2", "/track2", "9A")
    _track4 = Track(3,"track 3", "/track3", "4B")
    _track5 = Track(4,"track 4", "/track4", "10A")
    _track6 = Track(5,"track 5", "/track5", "1B")
    _track7 = Track(6,"track 6", "/track6", "7B")
    _track8 = Track(7,"track 7", "/track7", "3A")
    _track9 = Track(8,"track 8", "/track8", "12A")

    tracks = [_track1, _track2, _track3, _track4, _track5, _track6, _track7, _track8, _track9]
    return tracks
from pygame import mixer

"""
Sound Player:
handles playing sound.
"""


class SoundPlayer:
    def __init__(self):
        mixer.init() # initialize the mixer library

    def play(self, sound):
        sound = mixer.Sound("../res/audio/" + sound)
        sound.play()
        
        

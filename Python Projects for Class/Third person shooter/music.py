import winsound
import random

playlist = ["danger.wav","waveshaper.wav"]
selection = playlist[random.randint(0,len(playlist)-1)]
winsound.PlaySound(selection, winsound.SND_ALIAS)


from audio_to_phoneme import Translator
from phoneme_to_audio import Player
import time

p = Player()
t = Translator(p.read)
t.start()

print "Start talking..."

while True:
  time.sleep(0.1)
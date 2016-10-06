import wave
import os.path
import pyaudio
import time

HERE = os.path.dirname( __file__ )
PHONEME_DIR = os.path.join(HERE, 'phonemes', 'single', '16-signed')
PHONEMES = [
  'AA', 'AE', 'AH', 'AO', 'AW', 'AX', 'AY', 'B', 'CH', 'D', 'DH', 
  'DX', 'EH', 'EL', 'EM', 'EN', 'ENG', 'EY', 'F', 'G', 'HH', 'IH', 
  'IY', 'JH', 'K', 'L', 'M', 'N', 'NG', 'NX', 'OW', 'OY', 'P', 'R', 
  'S', 'SH', 'T', 'TH', 'UH', 'UW', 'V', 'W', 'Y', 'Z', 'ZH',
]
CHUNK = 1024

def get_wavefile(phoneme):
  path = os.path.join(PHONEME_DIR, "%s.wav" % phoneme)
  return wave.open(path, 'rb')
  
  
def get_all_wavefiles():
  return dict(zip(PHONEMES, [get_wavefile(x) for x in PHONEMES]))


p = pyaudio.PyAudio()
  
class Player:
  
  def __init__(self):
    self.waves = get_all_wavefiles()
    self.open_stream()
    
    
  def read(self, sents):
    print sents
    for words in sents:
      for word in words:
        for phoneme in word.split(' '):
          self.play(phoneme)
      time.sleep(0.5)
    
    
  def play(self, phoneme):
    if phoneme in ['ER', 'AXR']:
      phoneme = 'R'
    wf = self.waves[phoneme]
    data = wf.readframes(CHUNK)
    while data != '':
      self.stream.write(data)
      data = wf.readframes(CHUNK)
    wf.setpos(0)
    
    
  def open_stream (self):
    wf = self.waves['AA']
    self.stream = p.open(
      format=p.get_format_from_width(wf.getsampwidth()),
      channels=wf.getnchannels(),
      rate=wf.getframerate(),
      output=True
    )
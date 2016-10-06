import speech_recognition as sr
import ipatoarpabet
import time
import config

class Handler:
  
  def __init__(self, callback):
    self.callback = callback
    
  def __call__(self, recognizer, audio):
    words = recognizer.recognize_wit(audio, key=config['WIT_KEY'])
    phonemes = map(ipatoarpabet.translate, words.split(' '))
    self.callback(phonemes)

class Translator:
  
  def __init__(self, callback):
    self.recognizer = sr.Recognizer()
    self.microphone = sr.Microphone()
    self.stop_listening = lambda: None
    
    with self.microphone as source:
      self.recognizer.adjust_for_ambient_noise(source)
      
    self.handler = Handler(callback)
      
  def start(self):
    self.stop_listening = self.recognizer.listen_in_background(self.microphone, self.handler)
    
  def stop(self):
    self.stop_listening()
    self.stop_listening = lambda: None

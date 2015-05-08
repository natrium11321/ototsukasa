import speech_recognition as sr

class Listener:
	def __init__(self, energy_threshold = 300):
		self.r = sr.Recognizer(language = "ja")
		self.r.energy_threshold = energy_threshold
	def listen(self):
		with sr.Microphone() as source:
			audio = self.r.listen(source)
		try:
			return self.r.recognize(audio)
		except LookupError:
			return None
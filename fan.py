import pingo
import RPi.GPIO as GPIO


class Fan(object):
	ON = True
	OFF = False

	SPEED_STOPPED = 1
	SPEED_SLOW = 1
	SPEED_MEDIUM = 2
	SPEED_FAST = 3

	def __init__(self):
		super(Fan, self).__init__()

		self.board = pingo.rpi.RaspberryPi()
		self.state_pin = self.board.pins[13]
		self.state_pin.mode = pingo.OUT

		self.set_state(Fan.OFF)

	def set_state(self, status):
		if status == Fan.ON:
			self.state_pin.lo()
		elif status == Fan.OFF:
			self.state_pin.hi()

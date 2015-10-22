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
		self.state_pin = self.board[7]

	def set_status(self, status):
		if status == Fan.ON:
			self.state_pin.high()
		elif status == Fan.OFF:
			self.state_pin.low()

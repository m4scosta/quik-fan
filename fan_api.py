import json
from bottle import route, run, error, abort
from fan import Fan


fan = Fan()


@route("/fan/turn_on")
def turn_on():
	fan.set_status(Fan.ON)
	return json.dumps({"status": "OK"})


@route("/fan/turn_off")
def turn_off():
	fan.set_status(Fan.OFF)
	return json.dumps({"status": "OK"})


@route("/fan/set_speed/<speed:int>")
def set_speed(speed):
	if speed not in [1, 2, 3]:
		abort(404, "")

	# TODO: call raspberry pi

	return json.dumps({"status": "OK", "speed": speed})


@error(404)
def error404(error):
	return json.dumps({"error": "Resource not found"})


if __name__ == "__main__":
	run(host='0.0.0.0', port=8000, debug=True)

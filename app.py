from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from gpiozero import LED
from time import sleep

led = LED(21)

# Development purpose - auto reload when templates are changed
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run(debug=True, host='0.0.0.0')

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/turn-on", methods=["post"])
def turn_on():
    led.on()
    return jsonify({"status" : "success"})

@app.route("/turn-off", methods=["post"])
def turn_off():
    led.off()
    return jsonify({"status" : "success"}) 
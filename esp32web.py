from flask import Flask, render_template

try:
    from urllib.request import urlopen  # python 3
    from urllib.error import HTTPError, URLError
except ImportError:
    from urllib2 import urlopen  # python 2
    from urllib2 import HTTPError, URLError

# import json
deviceIp = "192.168.0.81"
portnum = "80"
base_url = "http://" + deviceIp + ":" + portnum
events_url = base_url + "/events"
app = Flask(__name__)

@app.route('/events')
def getevents():
    u = urlopen(events_url)
    data = ""
    try:
        # data = u.readlines()
        data = u.read()
    except HTTPError as e:
        print("HTTPerror: % d" % e.code)
    except URLError as e:
        print("Network error: %s“ % e.reason.args[1]")
    return data


@app.route('/')
def dht22chart():
    return render_template("dhtchart.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")

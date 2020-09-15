from flask import Flask, render_template, abort
import datetime
import pymysql
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin=18

app = Flask(__name__)
db = pymysql.connect("113.198.235.225", "alsrhkd", "1234", "ming_dht")
cur = db.cursor()


def get_value():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
        cur.execute(f'''INSERT INTO dht22 VALUES(\'{nowDatetime}\', \'{temperature:.6f}\', \'{humidity:.6f}\');''')
        db.commit()

@app.route('/')
def show_all():
    get_value()
    cur.execute("select * from dht22")
    result = cur.fetchall()
    if not result:
        return abort(404, "Page not found")
    return render_template("dht22db.html", items=result)


if __name__ == '__main__':
    app.run(host='localhost', port=8080)

from flask import Flask, request, render_template, abort, redirect
import datetime
import pymysql
import re
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
        cur.execute("insert into dht22 value(%s,%s,%s)", (nowDatetime, str(temperature), str(humidity)))
        db.commit()

@app.route('/')
def show_all():
    get_value()
    cur.execute("select * from dht_22")
    result = cur.fetchall()
    if not result:
        return abort(404, "Page not found")
    return render_template("dht22.html", items=result)


@app.route('/add_phone', methods=['POST'])
def add_phone():    # 전화번호 추가
    user_name = str(request.form.get('u_name'))
    phone_num = str(request.form.get('p_num'))
    cur.execute("insert into phone_book.user_list value(%s,%s)", (user_name, phone_num))
    db.commit()
    return redirect('/')


@app.route('/search', methods=['GET'])
def search_phone():     # 이름 또는 번호로 검색
    value = str(request.args.get('param'))
    matcher = re.compile('^[0-9]+-[0-9]+-[0-9]+')
    if matcher.match(value):    # 전화번호일때
        cur.execute("select * from user_list where phone_num=%s", value)
    else:   # 이름일때
        cur.execute("select * from user_list where user_name=%s", value)
    result = cur.fetchall()
    if not result:
        return "<p> 검색 결과가 없습니다. </p>"
    return render_template("index.html", items=result)


if __name__ == '__main__':
    app.run(host='localhost', port=8080)

from flask import Flask, render_template_string
import RPi.GPIO as g

g.setmode(g.BCM)
g.setup(2, g.OUT)
led_state = False
app = Flask(__name__)

control_page = '''
                <h1>GPIO control page</h1>
                <input id="btn_status" value="" readonly/>
                <input id="led_status" type="button" onclick="changeLED();" value="ON"/> 
                <script>
                  var led = document.getElementById('led_status');
                  function changeLED(){
                    var xhr = new XMLHttpRequest();
                    xhr.open('GET', '/change', true);
                    xhr.onreadystatechange = function(){
                      if(xhr.readyState === 4 && xhr.status === 200){
                        if(xhr.responseText === '1'){
                          led.value = 'ON';
                        }
                        else{
                          led.value = 'OFF';
                        }

                      }
                    }
                    xhr.send();
                  };
                </script>
                '''


@app.route('/')
def index():
    return render_template_string(control_page)


@app.route('/change')
def control_led():
    global led_state
    led_state = not led_state
    g.output(2, led_state)
    if led_state:
        return '1'
    else:
        return '0'


if __name__ == '__main__':
    app.run()
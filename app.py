from flask import Flask, render_template, jsonify
import speedtest
import datetime

app = Flask(__name__)

def test_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    
    download_speed = st.download() / 8_000_000  # Convert from bits per second to MBps
    upload_speed = st.upload() / 8_000_000  # Convert from bits per second to MBps
    ping = st.results.ping
    
    return download_speed, upload_speed, ping

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_speed')
def test_speed():
    download_speed, upload_speed, ping = test_internet_speed()
    result = {
        "download_speed": f"{download_speed:.2f} MBps",
        "upload_speed": f"{upload_speed:.2f} MBps",
        "ping": f"{ping:.2f} ms",
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

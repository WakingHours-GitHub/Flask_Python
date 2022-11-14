from flask import Flask, Response, render_template
from camera import Camera

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b''b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(
        gen(Camera()),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)

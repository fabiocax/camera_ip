
#!/usr/bin/env python
from flask import Flask, render_template, Response
import cv2
import imutils

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    video = cv2.VideoCapture(0)
    while True:
        rval, frame = video.read()
        frame = imutils.resize(frame, width=400)
        cv2.imwrite('/tmp/buff.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('/tmp/buff.jpg', 'rb').read() + b'\r\n')


@app.route('/stream')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True)
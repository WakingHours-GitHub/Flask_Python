import io
from itertools import cycle

import cv2
from flask import Flask, render_template, request, url_for, send_from_directory, Response
import os
import config
from config import *
from camera import Camera



app = Flask(__name__)

app.config.from_object(config) # 导入配置


def generate(path):
    # yield cv.imencode('.jpg', np.hstack([frame]))[1].tobytes()  # to bytes.
    img = cv2.imread(path)
    img = cycle(img)
    while True:
        yield cv2.imencode('.jpg', img)[1].tobytes()



def get_pic(path):
    # img = cv2.imread(path)
    # ext = os.path.splitext(path)[-1]
    #
    while True:
        frame = generate(path)
        yield (b'--frame\r\n'
               b''b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



def gen(path):
    """Video streaming generator function."""
    img = cv2.imread(path)
    ext = os.path.splitext(path)[-1]
    while True:
        # frame = camera.get_frame()

        yield (b'--frame\r\n'
               b''b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')

@app.route('/video_feed')
def video_feed(path):
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(
        get_pic(path),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file'] # 得到文件，
        if file and allowed_file(file.filename):
            # 如果文件不空，并且在允许的范围内。


            filename = file.filename
            # 判断文件名：进行文件类型的判断:
            file_ext = os.path.splitext(filename)[-1].split(".")[-1]
            print(file_ext)
            if file_ext in image_limitation_list: # 是图片
                print(filename + " is picture")
                file_save_path = os.path.join(app.config['UPLOAD_FOLDER'],  image_upload_path, filename)
                file.save(file_save_path)

                # video_feed(file_save_path) # 保存文件
                print(file_save_path) # D:\PyCharm\Flask\load_file\file\image\AAAA_tesyt.png

                img = cv2.imread(file_save_path)
                # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                # _, img_encoded = cv2.imencode('.jpg', img)[1].tobytes()
                response = cv2.imencode('.jpg', img)[1].tobytes()
                file_url = url_for('uploaded_file', filename=filename)
                # return render_template("image.html", video_feed=video_feed, path=file_save_path)
                file_save_path = os.path.join("..\\", "\\".join(file_save_path.split('\\')[-3:]))
                print(file_save_path)
                try:
                    # return Response(response=response, status=200, mimetype='image/jpg')
                    return render_template('image.html', file=file_save_path)
                except:
                    return render_template('index1.html')
        else:
            print('input not conform to the regulation')
    return render_template("index1.html")


def deal_file():
    print("文件上传了.")

# 判断允许的文件类型.
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 从文件夹中找这个文件.
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")

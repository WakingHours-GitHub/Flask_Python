from flask import Flask, render_template, request, url_for, Response, send_from_directory
import os
import config
from config import *
from flask_dropzone import Dropzone
from pathlib import Path
import sys
import cv2 as cv




app = Flask(__name__)
dropzone = Dropzone(app) # 创建对象.

app.config.from_object(config)
app.config['UPLOADED_PATH'] = os.path.join(app.root_path, 'file')
# -*- coding: utf-8 -*-
"""
    Flask-upload-dropzone
    ===================================
    Summary: flask file upload with Dropzone.js.
    Author: Grey Li
    Repository: https://github.com/helloflask/flask-upload-dropzone
    License: MIT
"""


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    print("文件上传了.")
    if request.method == 'POST':
        for f in request.files.getlist('file'): # 遍历上传的文件夹
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))

    file_list = os.listdir('./file')



    fatch_image(os.path.join("file", file_list))
    return render_template('index.html')




def fatch_image(file_name):
    if len(os.listdir("file")) == 0:
        return None

    img = cv.imread(file_name)

    return Response(

        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

# 判断允许的文件类型.
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 从文件夹中找这个文件.
@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOADED_PATH'],
                               filename)
if __name__ == '__main__':
    app.run(debug=True)

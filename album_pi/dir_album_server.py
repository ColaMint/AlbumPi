#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from album_pi import *
from flask import Flask, Response, render_template
import argparse
import json
import os
from PIL import Image
import base64
import mimetypes


parser = argparse.ArgumentParser(description='Diretory Album Server.')
parser.add_argument(
    '--port',
    dest='port',
    help='server port',
    default=2333,
    type=int)
parser.add_argument(
    '--dir',
    dest='dir',
    required=True,
    help='dirtory path')
parser.add_argument(
    '--interval',
    dest='interval',
    help='switch picture interval (second)',
    default=10,
    type=int)
parser.add_argument(
    '--display_mode',
    dest='display_mode',
    help='display mode',
    choices=[DISPLAY_MODE_ORDER, DISPLAY_MODE_SHUFFLE],
    default=DISPLAY_MODE_SHUFFLE)
args = parser.parse_args()


global pics

app = Flask(__name__)


@app.route('/')
def home():
    global pics
    return render_template(
        'home.html',
        pics=json.dumps(pics),
        interval=args.interval,
        display_mode=args.display_mode)


@app.route('/pic/<path>')
def pic(path):
    path = path.encode('utf-8')
    path= base64.urlsafe_b64decode(path)
    mime = mimetypes.guess_type(path)[0]
    with open(path, 'r') as f:
        return Response(
            response=f.read(),
            content_type=mime)


def get_pics_from_dir(dir_path):
    if not os.path.isdir(dir_path):
        return None

    pics = []
    for f in os.listdir(dir_path):
        path = os.path.join(dir_path, f)
        if not os.path.isfile(path):
            continue
        mime = mimetypes.guess_type(path)[0]
        if not mime or 'image' not in mime:
            continue
        im = Image.open(path)
        pic = {
            'url': '/pic/%s' % base64.urlsafe_b64encode(path),
            'width': int(im.size[0]),
            'height': int(im.size[1]),
        }
        pics.append(pic)
    return pics


if __name__ == '__main__':
    global pics
    pics = get_pics_from_dir(dir_path=args.dir)
    if pics:
        print '%d pictures found.' % len(pics)
        app.run(port=args.port)
    else:
        print 'No pictures found. Maybe dirtory is wrong.'

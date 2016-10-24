#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, Response, render_template
from optparse import OptionParser
import base64
import requests
import xmltodict
import json

DISPLAY_MODE_ORDER = 'order'
DISPLAY_MODE_SHUFFLE = 'shuffle'

parser = OptionParser()
parser.add_option(
    '--port',
    dest='port',
    help='server port',
    default=2333,
    type='int')
parser.add_option(
    '--qq',
    dest='qq',
    help='qq number')
parser.add_option(
    '--albumid',
    dest='albumid',
    help='album id. eg. 099c6fb8-d278-4b96-adbc-5d6356ad316a')
parser.add_option(
    '--interval',
    dest='interval',
    help='switch picture interval (second)',
    default=10,
    type='int')
parser.add_option(
    '--display_mode',
    dest='display_mode',
    help='display mode: order, shuffle',
    default=DISPLAY_MODE_SHUFFLE)
args, _ = parser.parse_args()


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


@app.route('/pic/<url>')
def pic(url):
    url = url.encode('utf-8')
    url = base64.urlsafe_b64decode(url)
    image_resp = requests.get(url)
    resp = Response(
        response=image_resp.content,
        content_type=image_resp.headers['Content-Type'])
    return resp


def get_qq_album_pics(qq, albumid):
    url = 'http://shalist.photo.qq.com/fcgi-bin/fcg_list_photo?uin=%s&albumid=%s' \
        % (qq, albumid)
    album_resp = requests.get(url)
    doc = xmltodict.parse(album_resp.text)
    if 'album' in doc:
        pics = []
        for pic in doc['album']['pic']:
            pic = {
                'url': '/pic/%s' % base64.urlsafe_b64encode(pic['url']),
                'width': int(pic['width']),
                'height': int(pic['height']),
            }
            pics.append(pic)
        return pics
    else:
        return None


if __name__ == '__main__':
    global pics
    pics = get_qq_album_pics(qq=args.qq, albumid=args.albumid)
    if pics:
        print '%d pictures found.' % len(pics)
        app.run(port=args.port)
    else:
        print 'No pictures found. Maybe qq or albumid is wrong.'

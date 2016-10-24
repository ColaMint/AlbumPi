#!/usr/bin/python
# -*- coding:utf-8 -*-

import argparse
import requests
import xmltodict

parser = argparse.ArgumentParser(description='List QQ Album.')
parser.add_argument(
    '--qq',
    dest='qq',
    required=True,
    help='qq number')
args = parser.parse_args()


def get_albums(qq):
    url = 'http://shalist.photo.qq.com/fcgi-bin/fcg_list_album?uin=%s' % qq
    resp = requests.get(url)
    doc = xmltodict.parse(resp.content.decode('gb2312'))
    if 'data' in doc and 'album' in doc['data']:
        albums = []
        for album in doc['data']['album']:
            albums.append({'id': album['id'], 'name': album['name']})
        return albums
    else:
        return None


if __name__ == '__main__':
    albums = get_albums(args.qq)
    if albums:
        print 'public album list:'
        for album in albums:
            print '%s - %s' % (album['name'], album['id'])
    else:
        print 'No albums found.'

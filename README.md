# QQAlbumPi

可供树莓派使用来播放QQ相册中的照片

# 使用方法

```
# 安装依赖库
pip install -r requirement.txt

# 获取公开相册列表（关键是获取相册ID）
# qq: QQ号
python list_album.py --qq {qq}

# 运行服务端
# port: 服务端监听的端口号，默认为2333
# qq: QQ号
# albumid: 相册ID
# interval: 切换图片的时间间隔，单位秒，默认10秒
# display_mode： 图片播放模式，order: 顺序播放，shuffle: 随机播放，默认为shuffle
python server.py --port {port} --qq {qq} --albumid {albumid} --interval {interval} --display_mode {display_mode}

# 浏览器访问http://localhost:{port}，并开启全屏模式
```
# 效果
![效果图1](https://github.com/Everley1993/QQAlbumPi/blob/master/example/p1.JPG)
![效果图2](https://github.com/Everley1993/QQAlbumPi/blob/master/example/p2.JPG)

# AlbumPi

供树莓派使用来播放`QQ相册`或`文件夹`中的照片

## 安装依赖的库

```
pip install -r requirement.txt
```

## 播放QQ相册中的照片

```
# 获取公开相册列表（关键是获取相册ID）
# qq: QQ号
python album_pi/list_qq_album.py --qq {qq}

# 运行服务端
# port: 服务端监听的端口号，默认为2333
# qq: QQ号
# albumid: 相册ID
# interval: 切换图片的时间间隔，单位秒，默认10秒
# display_mode： 图片播放模式，order: 顺序播放，shuffle: 随机播放，默认为shuffle
python album_pi/qq_album_server.py --port {port} --qq {qq} --albumid {albumid} --interval {interval} --display_mode {display_mode}
```

## 播放文件夹中的照片

```
# 运行服务端
# port: 服务端监听的端口号，默认为2333
# dir: 文件夹路径
# interval: 切换图片的时间间隔，单位秒，默认10秒
# display_mode： 图片播放模式，order: 顺序播放，shuffle: 随机播放，默认为shuffle
python album_pi/dir_album_server.py --port {port} --dir {dir} --interval {interval} --display_mode {display_mode}
```


## 开始播放

```
# 浏览器访问http://localhost:{port}，并开启全屏模式
```

## 效果

![](https://github.com/Everley1993/AlbumPi/blob/master/example/p1.JPG)
![](https://github.com/Everley1993/AlbumPi/blob/master/example/p2.JPG)

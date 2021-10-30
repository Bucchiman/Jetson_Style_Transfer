# Let's play Style Transfer with Jetson
We use Jetson Nano (2GB) and JetPack 4.5.
If you follow the steps below, you can play Real-time Style Transfer.

https://user-images.githubusercontent.com/52972710/139449867-42138f17-f613-4cfb-99b5-9d137e43a701.mp4

# Prerequisite
You have to __prepare__ __raspberry__ __pi__ camera module.
Currently, we don't prepare usb camera type.
If you play style transfer outside, you also need portable battery and small display.

# Install
We make venv environment.
First of all, you change directory to our repository.
Then the "install.sh" script is running.
This script is written for JetPack 4.5.
If you use other JetPack, you have to change a part of the script.
(If you use Jetpack 4.3, change https://developer.download.nvidia.com/compute/redist/jp/v45 -> https://developer.download.nvidia.com/compute/redist/jp/v43)
```bash
    $ git clone git@github.com:Bucchiman/Jetson_Style_Transfer.git
    $ cd Jetson_Style_Transfer
    $ ./install.sh  # You need to adjust url of tensorflow depending on your JetPack
```

# Usage
## Live Style Only
If you want to open real-time style transfer on full screen, then you can input the following.
```bash
    $ cd src
    $ ./running.sh live_style_only ../models/001.h5
```

## Live Original and Style Transfer
If you want to real-time original and style transfer, you can use the command.
```bash
    $ cd src
    $ ./running.sh live_original_style ../models/001.h5
```

## Make videos
If you want to make videos of style transfer, this command is input.
```bash
    $ cd src
    $ ./running.sh record ../models/001.h5
```
If Escape key is typed, then style transfer runs.
Output directory is made and you can find time stamp directories.
In this directory, original videos and style_transfer videos are found.


# Many trained models
We have many trained models.
We make sure you can find your favorite style tranfer images.
In this repository, "images" directory have style transfer images we gather.
So you can see style transfer images there.
Also, we prepare stylized images in "sample_style_transfer" directory.


<img src="https://user-images.githubusercontent.com/52972710/139523140-abc6a273-1d7b-493b-954c-5956da8bb4e1.jpeg" width="640.px">

# Lego blocks are Useful!
We use lego blocks in order to play style transfer outside.
If you are interesting, let's make original portable jetson.

<img src="https://user-images.githubusercontent.com/52972710/139456085-85f6a579-623e-4135-8b4a-81e4dd3f54ca.jpeg" width="640px">

![output](https://user-images.githubusercontent.com/52972710/139541647-b774af37-b8d8-4cee-bc2c-3bb71601d118.gif)

# Reference
- https://github.com/fritzlabs/fritz-models
- https://github.com/JetsonHacksNano/CSI-Camera

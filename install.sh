#!/bin/bash
#
# FileName: 	install
# CreatedDate:  2021-10-29 21:06:50 +0900
# LastModified: 2021-10-29 23:13:03 +0900
#


sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran
venv_dir="style_transfer_venv"
python3 -m venv $venv_dir

source $venv_dir/bin/activate
pip install -U pip testresources setuptools==49.6.0

# tensorflow install
pip install -U numpy==1.16.1 future==0.18.2 mock==3.0.5 h5py==2.10.0 keras_preprocessing==1.1.1 keras_applications==1.0.8 gast==0.2.2 futures protobuf pybind11
# If your jetson install Jetpack4.5 you don't have to change this command.
# Otherwise, you have to change 'https://developer.download.nvidia.com/compute/redist/jp/v45', suffix 'v45'
pip install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v45 tensorflow==1.15.5+nv21.6

# Other package install
pip install git+https://www.github.com/keras-team/keras-contrib.git
pip install keras==2.2.4

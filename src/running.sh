#!/bin/zsh
#
# FileName: 	running
# CreatedDate:  2021-10-17 23:50:21 +0900
# LastModified: 2021-10-30 03:45:26 +0900
#


source ../style_transfer_venv/bin/activate
if [[ $1 == "live_style_only" ]]
then
    python live.py --model_path $2
elif [[ $1 == "live_original_style" ]]
then
    python live.py --type original_and_style --model_path $2
elif [[ $1 == "record" ]]
then
    now=`date "+%Y_%m_%d_%H_%M_%S"`
    output_path="../outputs/$now"
    python record.py --output_path $output_path --model_path $2
    ffmpeg -r 20 -i $output_path/tmp/image_%05d.jpg -vcodec libx264 -pix_fmt yuv420p -r 20 $output_path/stylize_movie.mp4
    rm -r $output_path/tmp
else
    echo "usage error: live_style_only, live_original_style or record?"
fi
return


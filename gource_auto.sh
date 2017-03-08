#!/bin/sh

printf "Loading all git enabled Folders form current Folder...\n"
gitDir=($(gfind -name '*.git' -printf '%h\n' | sed 's/ /_/g' | sort -u))
if [ -x $gitDir ]
then
    echo "No git enabled directory found here, try command in upper directory."
    exit
fi
printf "Please select folder(Please wait until search for the folder end):\n"
read -p "$(
    f=0
    for dirname in "${gitDir[@]}" ; do
        echo "$((++f)) ${dirname##*/}"
    done
    echo 'Please select a directory > '
)" selection
while true
do
    if [ $selection -le ${#gitDir[@]} ]
    then
        d="${gitDir[$((selection-1))]}"
        break
    else
    read -p "$(echo '>>> Invalid Selection\nPlease Select a valid directory > ')" selection
    fi
done
read -p "$(echo 'Second Per Day(0.01-0.2 recommended > ')" SPD
name=${d//[^[:alnum:]]/}
dir=$(cd $d; pwd)
gource \
--path $dir \
--seconds-per-day $SPD \
--title "$name" \
-1280x720 \
--file-idle-time 0 \
--auto-skip-seconds 0.75 \
--multi-sampling \
--stop-at-end \
--highlight-users \
--hide filenames,mouse,progress \
--max-files 0 \
--background-colour 000000 \
--disable-bloom \
--font-size 24 \
--output-ppm-stream - \
--output-framerate 30 \
-o - \
| ffmpeg \
-y \
-r 60 \
-f image2pipe \
-vcodec ppm \
-i - \
-vcodec libx264 \
-preset ultrafast \
-pix_fmt yuv420p \
-crf 1 \
-threads 0 \
-bf 0 \
~/gitPreviews/$name.mp4

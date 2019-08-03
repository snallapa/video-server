for i in *.srt ; do ffmpeg -i "$i" "${i%.*}.vtt" ; done

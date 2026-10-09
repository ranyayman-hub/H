#!/bin/sh
# Lay EP01's music bed under EP02 (after the logo intro), ducked under the dialogue.
set -e
cd "$(dirname "$0")"
IN=${1:-EP02-flow-v4.mp4}; OUT=${2:-EP02-flow-v5.mp4}
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
ffmpeg -v error -y -i "$IN" -stream_loop -1 -i ../../ep01/audio/music.mp3 -filter_complex "
[0:a]aresample=44100,asplit=2[dlg][key];
[1:a]aresample=44100,aformat=channel_layouts=stereo,volume=-15dB,atrim=0:$D,adelay=6000|6000,afade=t=in:st=6:d=2,afade=t=out:st=$(echo "$D-4"|bc):d=4[m];
[m][key]sidechaincompress=threshold=0.03:ratio=6:attack=40:release=600[md];
[dlg][md]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=44100[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 160k -movflags +faststart "$OUT"

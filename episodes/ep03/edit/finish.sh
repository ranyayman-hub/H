#!/bin/sh
# EP03: logo intro (same as EP01/EP02) -> v2, then music bed ducked under dialogue -> v3.
set -e
cd "$(dirname "$0")"
ffmpeg -v error -y -i ../../ep01/build/intro-final.mp4 -i EP03-flow-v1.mp4 -filter_complex "
[0:v]scale=1280:720,fps=24,format=yuv420p,setsar=1,settb=1/24[iv];
[1:v]fps=24,format=yuv420p,setsar=1,settb=1/24[bv];
[iv][bv]xfade=transition=fade:duration=1:offset=6[v];
[0:a]aresample=44100,aformat=channel_layouts=stereo[ia];
[ia][1:a]acrossfade=d=1[a]" \
 -map "[v]" -map "[a]" -c:v libx264 -crf 24 -preset medium -c:a aac -b:a 192k -movflags +faststart EP03-flow-v2.mp4
IN=EP03-flow-v2.mp4; OUT=EP03-flow-v3.mp4
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
ffmpeg -v error -y -i "$IN" -stream_loop -1 -i ../../ep01/audio/music.mp3 -filter_complex "
[0:a]aresample=44100,asplit=2[dlg][key];
[1:a]aresample=44100,aformat=channel_layouts=stereo,volume=-15dB,atrim=0:$D,adelay=6000|6000,afade=t=in:st=6:d=2,afade=t=out:st=$(echo "$D-4"|bc):d=4[m];
[m][key]sidechaincompress=threshold=0.03:ratio=6:attack=40:release=600[md];
[dlg][md]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=44100[a]" \
 -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -movflags +faststart "$OUT"

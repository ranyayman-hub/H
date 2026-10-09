#!/bin/sh
# Prepend the channel logo intro (same as EP01) to EP02, dissolving into the first shot.
set -e
cd "$(dirname "$0")"
ffmpeg -v error -y -i ../../ep01/build/intro-final.mp4 -i EP02-flow-v3.mp4 -filter_complex "
[0:v]scale=1280:720,fps=25,format=yuv420p,setsar=1,settb=1/25[iv];
[1:v]fps=25,format=yuv420p,setsar=1,settb=1/25[bv];
[iv][bv]xfade=transition=fade:duration=1:offset=6[v];
[0:a]aresample=44100[ia];
[ia][1:a]acrossfade=d=1[a]" \
 -map "[v]" -map "[a]" -c:v libx264 -crf 20 -preset medium -c:a aac -b:a 160k -movflags +faststart EP02-flow-v4.mp4

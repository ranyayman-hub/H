#!/bin/bash
# usage: put.sh <file> <upload_id>   (run from build/lipsync/in)
U='https://www.googleapis.com/upload/storage/v1/b/xi-backend/o?uploadType=resumable&upload_id='
case "$1" in *.mp4) T=video/mp4;; *) T=audio/mpeg;; esac
curl -sS -o /dev/null -w "$1 %{http_code}\n" -X PUT -H "Content-Type: $T" --data-binary @"$1" "$U$2"

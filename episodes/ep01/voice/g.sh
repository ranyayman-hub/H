#!/bin/bash
# usage: g.sh <out-name> <ext> <session> <generation> <X-Goog-Date> <signature>
B='https://storage.googleapis.com/xi-backend/database/workspace/dd12cfc60041462da31c2575ab520bc5/content_generation'
Q='X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=xi-backend-prod%40xi-labs.iam.gserviceaccount.com%2F20261002%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Expires=7200&X-Goog-SignedHeaders=host'
curl -sS -o "$1" "$B/$3/$4/content.$2?$Q&X-Goog-Date=$5&X-Goog-Signature=$6" && echo "$1 $(file -b "$1" | cut -c1-25)"

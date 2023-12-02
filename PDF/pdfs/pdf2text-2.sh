#!/bin/bash

# Check if a filename was provided as an argument
if [ -z "$1" ]; then
  echo "Please provide a filename as an argument."
  exit 1
fi

# Loop through all specified files and process them
for file in "$@"; do
  # Use sed to join lines starting with whitespace to the previous line
  sed -i '1!{ /^[[:space:]]*RCW/ b; N; /^[[:space:]]*RCW/! s/\n\s*/ /; }' "$file"
  sed -i -e ':a;N;$!ba;s/\n / /g' "$file"
done

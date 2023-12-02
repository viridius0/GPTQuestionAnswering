for file in *.pdf; do
  pdftotext "$file"
done

for file in *.txt; do
  sed -i 's/\x0C//g' "$file"
  sed -i ':a; s/\[[^][]*\]//g; N; ba' "$file"
  sed -i ':a;N;$!ba;s/\n\([^[:blank:]\n]\)/ \1/g;s/\n//g' "$file"
  cat "$file" >> RCW.txt
done

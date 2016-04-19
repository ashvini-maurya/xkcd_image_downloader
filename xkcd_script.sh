curl http://xkcd.com/{1..1669}/ | grep http://imgs.xkcd.com/comics/ > urls.txt

cat urls.txt | awk '{ print $5 }' > final_urls.txt

wget -i final_urls.txt

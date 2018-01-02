# official-account-crawler
A crawler that can crawling wechat official account's newest or most famous article in 7 days
data source: http://www.newrank.cn/

framework: selenium + phantomJs + web.py & python 2.7

how to use:

clone

install all dependencies

cd official-account-crawler

edit PhantomJS path in line 31 (replace [YOUR-PhantomJS-PATH] with specific path)

python crawler-web.py

http://0.0.0.0:8080/officialaccount?id=[YOUR-OFFICIAL-ACCOUNT-ID]
 or
http://localhost:8080/officialaccount?id=[YOUR-OFFICIAL-ACCOUNT-ID]

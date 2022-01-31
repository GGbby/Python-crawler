import bs4

url="https://www.ptt.cc/bbs/Gossiping/index.html"
# built a request object, which include a "Request Headers" imformation
request=req.Request(url, headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data, "html.parser")


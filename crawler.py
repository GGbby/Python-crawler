import urllib.request as req
import bs4

url="https://ck101.com/forum-3621-1.html"
# built a request object, which include a "Request Headers" imformation
request=req.Request(url, headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

root=bs4.BeautifulSoup(data, "html.parser")

# find all data as a list that meet the condition we set
# btw if using find it will be a string data
titles=root.find_all("a", class_="s xst") 
i=1
ev=0
for x in titles:

    if i <1:
        if ev==0:
            print(x.string,end=" ")
            ev+=1
        else:
            print(x.string+"\n")
            ev-=1
    else:
        i=0
    
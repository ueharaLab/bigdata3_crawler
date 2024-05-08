import urllib.request
response = urllib.request.urlopen('https://news.yahoo.co.jp/')

html = response.read()
print(html.decode('utf-8'))
txtFile_html = open("homepage.html",'w',newline='',encoding='utf-8')
txtFile_html.write(html.decode('utf-8'))
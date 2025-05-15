import urllib.request
import lxml.html
response = urllib.request.urlopen('https://www.yahoo.co.jp/')

html = response.read()
print(html.decode('utf-8',errors='replace'))

txtFile_html = open("homepage.html",'w',newline='',encoding='utf-8')
txtFile_html.write(html.decode('utf-8'))
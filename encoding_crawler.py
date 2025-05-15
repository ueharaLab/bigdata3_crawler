import urllib.request
#response = urllib.request.urlopen('https://tabelog.com/rstLst/RC0123/2/?sk=うどん&svd=20240213&svt=2100&svps=2/')
response = urllib.request.urlopen('https://tabelog.com/rstLst/RC0123/2/?sk=%E3%81%86%E3%81%A9%E3%82%93&svd=20240213&svt=2100&svps=2')
html = response.read()
print(html.decode('utf-8'))
txtFile_html = open("homepage.html",'w',newline='',encoding='utf-8')
txtFile_html.write(html.decode('utf-8'))
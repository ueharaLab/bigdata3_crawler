# 検索キーワードをURLに含むクローラー
[keyword_crawler.py](/keyword_crawler/)を実行するとエラーになる。中身は正しく見える。
``` python
response = urllib.request.urlopen('https://tabelog.com/rstLst/RC0123/2/?sk=うどん&svd=20240213&svt=2100&svps=2/')

html = response.read()
print(html.decode('utf-8'))
txtFile_html = open("homepage.html",'w',newline='',encoding='utf-8')
txtFile_html.write(html.decode('utf-8'))
```
次に、うどん屋一覧2ページ目のURLボックスから上記プログラムの該当URLに貼り付けて再度実行するとうまくいくはず。貼り付けたURLを見ると、うどんが消えて、%記号が入った妙な文字化けが表示されている。

``` python
https://tabelog.com/rstLst/RC0123/2/?sk=%E3%81%86%E3%81%A9%E3%82%93&svd=20240213&svt=2100&svps=2
```
# URL encodeを自動的に行う
[urlEncode.py](/urlEncode.py)を実行すると、うどんをURL encodeした結果が表示される。

``` python

import urllib.parse
inputWord='うどん'
keyWord = urllib.parse.quote(inputWord)
print(keyWord)

```

### 演習1. コマンドラインからキーワードを自由に入力するとURL encodeした文字列を画面表示するプログラムを書いてください。

### 演習2. 上記のプログラムと、[encoding_crawler.py](/encoding_crawler.py)を連結して、URL encodingした文字列で該当のページを取得するプログラムを作成せよ。
encoding_crawler.pyは以下のように修正ればよい。
``` python

import urllib.request

# 以下のURL encode文字列の部分に演習1. でURL encoding した文字列を代入する
response = urllib.request.urlopen('https://tabelog.com/rstLst/RC0123/2/?sk=%E3%81%86%E3%81%A9%E3%82%93&svd=20240213&svt=2100&svps=1')

html = response.read()
print(html.decode('utf-8'))
txtFile_html = open("homepage.html",'w',newline='',encoding='utf-8')
txtFile_html.write(html.decode('utf-8'))
```

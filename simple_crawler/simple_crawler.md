# webサイトを１ページだけ取り込むCrawler

[crawler1.py](/crawler1.py)を実行すると、同じフォルダーにhomepage.htmlというファイルが出来上がる。このファイルをダブルクリックすると、ホームページが表示される。  

URLを変えて実行してみる

``` python
サンプルコード解説

import urllib.request # webサイトに情報をリクエストするためのライブラリを取り込む
                               
response = urllib.request.urlopen('https://news.yahoo.co.jp/')
# urllib.request.urlopen ：webサイトに情報をリクエスト(httpリクエスト）するクラス（ライブラリ名に続けてドット.クラス名で呼び出す）
#　変数 = クラス名でインスタンスを生成

html = response.read()
#.read():urlopenのメソッド  

print(html.decode('utf-8'))
# utf-8 : 文字コード(取得したwebサイトが何の文字コードで書かれているかに依存する）　
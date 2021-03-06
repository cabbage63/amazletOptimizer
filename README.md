# Amazlet Optimizer
## 概要
Bloggerの全記事に含まれるAmazletのリンクをhttpsに適した形式に変換します。
python2.7で動作確認しています。

## 使い方
0. Google APIライブラリをインストール
1. リポジトリをクローンorダウンロード
2. client_secrets.jsonのAPI情報を更新
3. amazletOptimizer.py中のブログIDを変更
4. 実行

### 1. Google APIライブラリをインストール
```
$ pip install --upgrade google-api-python-client
```

### 2.リポジトリをクローンorダウンロード
```
$ git clone git@github.com:cabbage63/amazletOptimizer.git
```

### 3. client_secrets.jsonのAPI情報を更新
[Blogger API: Using the API  |  Blogger  |  Google Developers](https://developers.google.com/blogger/docs/3.0/using#auth)

こちらのサイトを参考にしながらBloggerのAPIキーを取得してください。
取得できたらクライアントIDとクライアントシークレットを`client_secrets.json`中の対応する変数を変更してください。
```
        "client_id": "input your client_id",
        "client_secret": "input your client_secret",
```

### 4. amazletOptimizer.py中のブログIDを変更
Bloggerのブログ管理画面のURL`https://www.blogger.com/blogger.g?blogID=***************#overview`の`blogID=`以降の数字部分をコピーして、`amazletOptimizer.py`中のBLOG_ID定数を置換えてください。
```
  #input your blog ID
  BLOG_ID = ********************
```
### 5. 実行
万が一に備えて記事のバックアップをとっておいてください。
管理画面のサイドメニューより、設定＞その他＞コンテンツをバックアップで可能です。

```
$ python amazletOptimizer.py
```

# mkdocsセットアップ

## プラグイン導入の基本

### 各種プラグインのパッケージをインストールする

プラグインは各自インストールしたり、テーマに付属しているものがある。
例えば、mkdocs-materialテーマには独自のsearchプラグインが導入されていたりするため、個別インストールなしにこのプラグインを使用することができる。

プラグイン名        | 説明
-------------------|----------------------------------------
[mkdocs-macros-plugin](https://github.com/fralau/mkdocs_macros_plugin)| マクロを有効にするプラグイン。Pythonで処理を自由に書いてマクロを組める。
[search (mkdocs-material)](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-search/)| mkdocs-materialテーマの内蔵プラグイン。全文検索ができる。
[mkdocstrings](https://pawamoy.github.io/mkdocstrings/)|Pythonコードを解析してドキュメント生成してくれる。mkdocs-materialと一緒に動作するプラグインであるため注意。

##### インストール方法

基本的にはPIPインストールすることで動作環境を作る。(例: mkdocs-macros-plugin)

```bash
pip install mkdocs-macros-plugin
```

### mkdocsでプラグインの使用を宣言する

```yaml
plugins:
  - search:
      separator: '[\s\-\.]+'
      lang:
        - en
        - ja
  - macros
  - mkdocstrings:
      handlers:
        python:
          setup_commands:
            - import sys
            - sys.path.append("src")
```


## マクロを入れる

### プラグインをインストールする

```bash
pip install mkdocs-macros-plugin
```
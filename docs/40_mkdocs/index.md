# mkdocsセットアップ

## エクステンションを導入する

エクステンションを導入することで、mkdocs自体のふるまいや、マークダウン記述の拡張を行って、絵文字を簡単に入力可能にしたり、キャレットを有効にしたりなど、ドキュメントの視認性を向上するなどに活用できる機能を数多く導入できる。
こちらもかなりの数あるので、テストをしながら導入していくのをおススメ。

### エクステンションをインストールする

ものによってはmkdocs自体にデフォルトで入っていたり、テーマに付属してきたりするが、インストールを行うことでさらに機能拡張が行える。

### mkdocs.mdでエクステンションの使用を宣言する

mkdocs.mdで以下の様に記述をすれば使用可能になる。

```yaml
extensions:
  - admonition # アノテーションブロックを有効
  - codehilite # コードハイライトを有効
  - footnotes # 下部への注釈表記を有効
  - tables # テーブルを有効
  - pymdownx.arithmatex # Arithmatex統合を有効
  - pymdownx.mark # ハイライト機能を有効
  - pymdownx.details # 折り畳みアノテーションを有効
  - pymdownx.keys # キーショートカットの表示
  - pymdownx.tabbed # タブ表示の有効化
  - pymdownx.caret # キャレットを有効化
  - fontawesome_markdown
  - markdown_blockdiag: # Makrkdownダイアグラムを有効
      format: svg
  - pymdownx.emoji: # 絵文字を有効
        emoji_index: !!python/name:materialx.emoji.twemoji
        emoji_generator: !!python/name:materialx.emoji.to_svg
```

## プラグインを導入する

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

### mkdocs.mdでプラグインの使用を宣言する

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


## マクロを導入する

### プラグインをインストールする

```bash
pip install mkdocs-macros-plugin
```

### mkdocs.mdで使用を宣言する

```yaml
plugins:
    - macros
```

### main.pyを作成する

main.pyをルートディレクトリに作成し、 `define_env(env)` 関数を作成する。

```Python
def define_env(env):
    @env.filter
    def vimeo(videoid):
        """VimeoのVideoIDを引数にVimeoの埋め込みコンテンツを返す。
        """
        return f'<iframe src="https://player.vimeo.com/video/{videoid}"'\
                'width="640" height="360" frameborder="0" allow="autoplay;'\
                'fullscreen" allowfullscreen></iframe>'
```

!!! note
    ここら辺は、[Reincanation+#Techの記事](https://fereria.github.io/reincarnation_tech/10_Programming/99_Documentation/02_mkdocs_macro/)が詳しいので、そちらを参照。


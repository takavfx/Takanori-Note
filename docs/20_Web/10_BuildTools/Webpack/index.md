# Webpack

## Webpack環境の準備

### プロジェクトの作成

```shell
プロジェクトの作成コマンド
mkdir webpack-project
cd webpack-project
npm init -y
```

アウトプット
```json
{
  "name": "webpack-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

### WebpackとWebpack CLI，Webpack Dev Serverのインストール

```
npm install --save-dev webpack webpack-cli webpack-dev-server
npx webpack init
```

!!! note
    ここでWebpackプロジェクトを作成する際にどの環境を作るかを選択できる。
    JavaScript/TypeScriptやCSS/SASSの選択など。
# TensorFlowをCPP上で動かす

!!! note
    ここでの基本的な環境はWindowsとしてノートを記述する。
    
    各種DCCツールや当人の業務環境が普段はWindowsのため。

## 基本

### ライブラリをダウンロードする

TensorFlowの公式ページにて、[インストール > 言語バインディング > C の項目](https://www.tensorflow.org/install/lang_c)から使用するOSを選択してダウンロードする。

ダウンロードしたライブラリは管理しやすい場所に配置する。

!!! warning
    現状、TensorFlowの公式から入手可能な言語バインディングはバージョンが旧式なものしかない。
    将来的にはサポートされるとのことだが、TensorFlow 2.0以降のバージョンなどは現状使えない。

### コードを書く

```C++
#include <stdio.h>
#include <tensorflow/c/c_api.h>

int main() {
    printf("Hello from TensorFlow C library version %s\n", TF_Version());
    return 0;
}
```

### ビルドする

```Bash
gcc main.c -IF:\Develop\TensorFlow\CPP\lib\libtensorflow-cpu-windows-x86_64-1.15.0\include -LF:\Develop\TensorFlow\CPP\lib\libtensorflow-cpu-windows-x86_64-1.15.0\lib -ltensorflow  -o hello_tf
```

!!! note
    ビルド環境においてはlib以下がexeディレクトリ以下にコピーされないため、各自コピーしないと、dllが見つからないエラーが発生する。


### 実行

```Bash
hello_tf
# > Hello from TensorFlow C library version 1.15.0
```


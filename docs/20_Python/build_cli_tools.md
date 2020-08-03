# PythonでのCLIツールの作り方

## 基本

### pip installできる環境を作る。

以下の様にインストールできる環境を作る。

```bash
pip install sample-cli
```

GitHubなどにあげておいて、レポジトリから直接インストールする場合は次のような感じ。

```bash
pip install git+https://github.com/takavfx/sample-cli
```


#### ディレクトリ構成

```
- package_root
    |- setup.py
    |- src
        |- samplecli
            |- __init__.py
            |- cli.py
```

### setup.pyを書く

```python
import os
from setuptools import setup, find_packages

current_dir = os.path.abspath(os.path.dirname(__file__))

requires = [
    "pyyaml",
    "autopep8",
    "docopt"
]

test_requirements = [
    "pytest"
]

about = {}
with open(os.path.join(current_dir, "src", "tatool", "__init__.py"), "r") as f:
    exec(f.read(), about)


setup(
    name=about["__title__"],
    url=about["__url__"],
    version=about["__version__"],
    description=about["__description__"]
    install_requires=requires,
    python_requires=">=3.7.*, <4",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "mytool = mytoolcli.cli:main"
        ]
    },
    tests_require=test_requirements,
)
```

!!! note
    [setup.pyについて。](https://docs.python.org/ja/3/distutils/setupscript.html)

!!! note

    entry_points
    このentry_points辞書に、コンソールで入力した際の実行スクリプトを記述する。

    ```<command> = <cliパッケージ>.<CLIモジュール>:<実行関数名>
    ```

### ソースを書く

#### `__init__.py`

```python
__title__ = "sample-cli"
__version__ = "1.0.0"
__description__ = "Sample python package for Command Line tool creation by Python"
__url__ = "https://github.com/takavfx/sample-cli"
```

#### src/samplecli/cli.py

```python
def main():
    print("hello, world")
```

!!! note
    上記のサンプルseup.pyファイルで、 `"mytoolcli = mytoolcli.cli:main"` と宣言している。そのため、ここでは、コマンドライン上で `mytool` と実行すると、この `main()` 関数が呼ばれることになる。
    もし、別の関数を実行したい場合には、setup.pyの部分とこの `main()` 関数名を変更する。
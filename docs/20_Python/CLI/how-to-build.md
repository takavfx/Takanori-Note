# PythonでのCLIツールの作り方

## 基本

### 1. pip installできる環境を作る。

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

### 2. setup.pyを書く

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
with open("src", "r") as f:
    exec(f, about)

setup(
    name="mytool-cli",
    url="",
    install_requires=requires,
    python_requires=">=3.7.*, <4",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "mytoolcli = mytoolcli.cli:main"
        ]
    },
    tests_require=test_requirements,
)
```

!!! note

    entry_points
    このentry_points辞書に、コンソールで入力した際の実行スクリプトを記述する。

    ```<command> = <cliパッケージ>.<CLIモジュール>:<実行関数名>
    ```

### 3. ソースを書く

```python
__title__ = "sample-cli"
__version__ = "1.0.0"
__description__ = "Sample python package for Command Line tool creation by Python"
__url__ = "https://github.com/takavfx/sample-cli"
```

```python
commands = [
    "format"
]

def main():
    print("hello, world")
```
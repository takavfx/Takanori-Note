# PythonでのCLIツールの作り方

## 基本

1. pip installできる環境を作る。

```bash
```

2. setup.pyを書く

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
    return 

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
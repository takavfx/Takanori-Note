# Maya HLSL

[![Image from Gyazo](https://i.gyazo.com/3b0c595568c1f6f79b0be061cbd4ccf9.png)](https://gyazo.com/3b0c595568c1f6f79b0be061cbd4ccf9)

## MayaでのHLSL

Mayaではdx11Shaderを利用する事でHLSLを使用したシェーダーを用意する事が出来る。

!!! note
    * [ナレッジ(Maya2020)](https://knowledge.autodesk.com/ja/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2019/JPN/Maya-LightingShading/files/GUID-A842D2FC-C191-452B-9229-3AC15DC00179-htm.html)
    * [ドキュメント(Maya2020)](http://help.autodesk.com/view/MAYAUL/2020/JPN/?guid=GUID-21D2A020-EC76-4679-B38A-D5270CE52566)

## Mayaでdx11Shaderを使用する

### 設定の有効かとプラグインのロード

Mayaでdx11Shaderを有効にするには、設定項目の有効化とプラグインのロードが必要になる。

* Windows > Rendering Editors > Preferences > Display > Viewport 2.0で**DirectXを指定**する。
* Plug-in Mangerでdx11Shader.mllを**有効**にする。
* Viewport > Shading > Hadware Texturingを**有効**にする。
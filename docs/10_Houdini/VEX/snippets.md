# Houdini VEX

## 一定の範囲でランダムにスケールを変える

[![Image from Gyazo](https://i.gyazo.com/711d5e4ae02449116785db887cc8f875.png)](https://gyazo.com/711d5e4ae02449116785db887cc8f875)

```
@pscale = fit01(rand(@ptnum), 0.1, 1);
```
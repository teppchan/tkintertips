% 逆引きPython/Tk
<!-- -*- coding:utf-8 -*- -->

CheckButton Widget
--------------

### ボタンの選択、非選択を切り替える

```python
$import(py/checkbutton/active_cb.py)
```

* "select"ボタンを押すと、チェックボタンにチェックが入る、
* "deselect"ボタンを押すと、チェックボタンにチェックが消える、
* "toggle"ボタンを押す度に、チェックボタンにチェックがオンオフする。

![](py/checkbutton/active_cb1.png)

![](py/checkbutton/active_cb2.png)

### チェックされているかどうか調べる

```python
$import(py/checkbutton/check_checked.py)
```

チェックボタンがオフの時は、０が表示される。

![](py/checkbutton/check_checked1.png)

チェックボタンがオンの時は、１が表示される。

![](py/checkbutton/check_checked2.png)

Tk.Variableの代わりにTk.BooleanVarを使うと、True/Falseを得られる。

<!-- ### ボタンをグループ化する -->

### チェック領域を表示しないようにする（トグルボタンになる）

```python
$import(py/checkbutton/toggle_button.py)
```

チェックボタンの代わりにトグルボタンになる。

![](py/checkbutton/toggle_button1.png)

![](py/checkbutton/toggle_button2.png)


### ビットマップを使用する

```python
$import(py/checkbutton/internal_bitmap.py)
```

テキストの代わりに画像を表示する（Tk.Buttonと同様）。

![](py/checkbutton/internal_bitmap1.png)

![](py/checkbutton/internal_bitmap2.png)

### ボタンを選択（非選択）した時の動作を設定する

```python
$import(py/checkbutton/command.py)
```

チェックボタンをオンオフすると呼ばれる関数を設定する。

![](py/checkbutton/command1.png)

![](py/checkbutton/command2.png)

### ボタンを選択した時の背景色を設定する

```python
$import(py/checkbutton/bg_color.py)
```

![](py/checkbutton/bg_color1.png)

チェックボタンを押下した時に背景色が変わる。

![](py/checkbutton/bg_color2.png)


### チェックボタンがOn/Offの場合にテキストを設定する

```python
$import(py/checkbutton/onoffvalue.py)
```

![](py/checkbutton/onoffvalue1.png)

![](py/checkbutton/onoffvalue2.png)


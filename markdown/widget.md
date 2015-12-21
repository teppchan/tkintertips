% 逆引きPython/Tk
<!-- -*- coding:utf-8 -*- -->

Widget全般
--------------

### 幅や高さを設定する

300x200のウィンドウができる。
```python
$import(py/widget/set_wh.py)
```

![](py/widget/set_wh.png)

ラベルのサイズに合わせたウィンドウができる。
```python
$import(py/widget/set_wh_label.py)
```

ボタンで大きさが変わるサンプル。
```python
$import(py/widget/set_wh_button.py)
```

### 幅や高さを取得する

ボタンを押すと標準出力にウィンドウサイズを表示する。
```python
$import(py/widget/get_wh.py)
```

ボタンを押すと標準出力にウィンドウサイズを表示する。実際の画素数が出ているっぽい。画面のサイズを大きくすると出力値が変わる。
```python
$import(py/widget/get_wh2.py)
```

### Widgetの見た目を変える

ラベルの枠を変更できる。
```python
$import(py/widget/label_pref.py)
```

![](py/widget/label_pref.png)

### Widget間の間隔（余白）を設定する

```python
$import(py/widget/label_margin.py)
```

![](py/widget/label_margin.png)

### 前景、背景色を変える

fgで文字の色、bgで背景の色を変更する。
```python
$import(py/widget/label_color.py)
```

![](py/widget/label_color.png)

### アクティブ時（マウスが上に来た時）に前景、背景色を変える

```python
$import(py/widget/label_mouse.py)
```

![デフォルト状態](py/widget/label_mouse1.png)デフォルト状態

![カーソルをラベルに乗せた状態](py/widget/label_mouse2.png)カーソルをラベルに乗せた状態


### フォントを変える

```python
$import(py/widget/font_change.py)
```

![](py/widget/font_change.png)


### フォントの大きさを変える

```python
$import(py/widget/font_size.py)
```

![](py/widget/font_size.png)


<!-- ### フォントの一覧を取得する -->

<!-- ### フォーカスを移動する -->

### マウスカーソルの形状を変更する

```python
$import(py/widget/font_size.py)
```

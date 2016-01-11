% 逆引きPython/Tk
<!-- -*- coding:utf-8 -*- -->

RadioButton Widget
--------------

### どのボタンが選択されているかどうかを調べる

```python
$import(py/radiobutton/check.py)
```

RadioButton1が押されると、１が表示される。
RadioButton2が押されると、２が表示される。
Tk.Variableを介して調べることができる。

![](py/radiobutton/check1.png)

![](py/radiobutton/check2.png)


### ボタンの選択、非選択を切り替える

```python
$import(py/radiobutton/active_rb.py)
```

RadioButton2が選択されている時にrb1.select()を実行するとRadioButton1が選択される。
RadioButton1が選択されている時にrb1.deselect()を実行すると、どこも選択されない状態になる（４枚目画像）。

![](py/radiobutton/active_rb1.png)

![](py/radiobutton/active_rb2.png)

![](py/radiobutton/active_rb3.png)

![](py/radiobutton/active_rb4.png)


<!-- ### ボタンをグループ化する -->

### チェック領域を表示しないようにする（トグルボタンにする）

```python
$import(py/radiobutton/toggle_button.py)
```

indicatoronを'off'にすると、トグルボタンになる。

![](py/radiobutton/toggle_button1.png)

![](py/radiobutton/toggle_button2.png)


### ビットマップを使用する

```python
$import(py/radiobutton/internal_bitmap.py)
```

テキストの代わりに画像を表示する（Tk.Buttonと同様）。

![](py/radiobutton/internal_bitmap1.png)

![](py/radiobutton/internal_bitmap2.png)


<!-- ### ボタンを選択、非選択した時の動作を設定する -->


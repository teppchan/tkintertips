% 逆引きPython/Tk
<!-- -*- coding:utf-8 -*- -->

イベント
--------------

### マウスの第１ボタンをクリックした時の動作を設定する

```python
$import(py/event/mouse_single1.py)
```

左クリックすると"Clicked!!"と表示される。

![](py/event/mouse_single1.png)

（変なエラーが出ているのは使っているPythonの環境のせいらしい。実害ないのでこのまま進めます）

### マウスをダブルクリックした時の動作を設定する

```python
$import(py/event/mouse_double.py)
```

### マウスの第２ボタンをクリックした時の動作を設定する

```python
$import(py/event/mouse_single2.py)
```

### マウスを移動した時の動作を設定する

```python
$import(py/event/mouse_motion.py)
```

ウィンドウ上でマウスを動かすと、コンソールに"Motion"と表示される。

![](py/event/mouse_motion.png)

### マウスの座標を取得する

```python
$import(py/event/mouse_coord.py)
```

ウィンドウ上でマウスを動かすと、カーソル（写ってないけど）の位置座標が、
クリックするとカーソルの位置座標が、コンソールに表示される。

![](py/event/mouse_coord.png)

### Enterキーを押した時の動作を設定する

```python
$import(py/event/press_enter.py)
```

エンターキー（リターンキー）を押すとコンソールに"Return!!"と表示される。

![](py/event/press_enter.png)

### どのキーが押されたかを取得する

```python
$import(py/event/press_key.py)
```

どれかキーを押すと押したキーの文字がコンソールに表示される。ShiftキーやMetaキーにも反応する。

![](py/event/press_key.png)

### Widgetにフォーカスが移ってきた時の動作を設定する

```python
$import(py/event/focus.py)
```

選択されたWidgetの文字の色が変わる。

![](py/event/focus.png)


### ファンクションキーF1でヘルプを表示する

```python
$import(py/event/open_newwin.py)
```

F1キーを押すと新しいウィンドウが出てくる。

![](py/event/open_newwin.png)

<!-- ### 特殊キー(Shift, Ctrl, Alt)などが押されたかどうかを知る -->

### C-x Ccで終了する

```python
$import(py/event/cx_cc.py)
```

連続したキーもイベントとして反応できる。

<!-- ### 特定のWidgetイベント -->
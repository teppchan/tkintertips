% 逆引きPython/Tk
<!-- -*- coding:utf-8 -*- -->

Button Widget
--------------

### Enterで選択できるようにする

```python
$import(py/button/enter.py)
```

ボタンを押してもEnterキーを押しても数字がインクリメントする。（focus使ってるけど、他でうまく流用できるかな？）

![](py/button/enter.png)

```python
$import(py/button/enter2.py)
```

rootでReturnのイベントを補足して、b.invoke()しても同じことになる。こちらの方b.focus()しないから自然？


### ショートカットキーを設定する

```python
$import(py/button/short.py)
```

Control-aを押すと数字がインクリメントする。

![](py/button/short.png)

### ボタンを使用不可にする

```python
$import(py/button/disable.py)
```

Checkbuttonにチェックを入れると、ボタンが押せなくなる。

![](py/button/disable1.png)

![](py/button/disable2.png)

### イメージつきボタンを使用する

```python
$import(py/button/internal_bitmap.py)
```


![](py/button/internal_bitmap.png)

Tk標準で内蔵しているbitmap画像をボタンとして使える。

```python
$import(py/button/read_image1.py)
```

Tkは標準でXBM,GIF,PPM,PGMを読めるので、それをボタンに貼り付けられる。

![](py/button/read_image1.png)


```python
$import(py/button/read_image2.py)
```

JPEGやPNGを使う場合は、PILのImageTkを使えばいいらしいけど、私の環境ではライブラリが競合して実行できなかった。OSX標準のライブラリとAnacondaのライブラリとが混信しているらしい。無念。。。


% 逆引きPython/Tk
<!-- -*- coding:utf-8 -*- -->

配置
--------------

### Widget間の間隔（余白）を設定する

padyで余白を指定。水平方向はpadx

```python
$import(py/place/margin.py)
```

![](py/place/margin.png)

### 親Widgetを指定する

root以外も親Widgetにできる。親をコンテナWidget（ここではFrame）に指定する。
```python
$import(py/place/frame.py)
```

### Widgetを非表示にする

```python
$import(py/place/unpack.py)
```

起動時の様子。ラベルとボタンの両方が表示されている。

![](py/place/unpack1.png)

unpackボタンを押すとラベルが消える。

![](py/place/unpack2.png)

### 上から下に順にpackする

```python
$import(py/place/pack_top.py)
```

![](py/place/pack_top.png)

### 下から上に順にpackする

```python
$import(py/place/pack_bottom.py)
```

![](py/place/pack_bottom.png)

### 左から右に順にpackする

```python
$import(py/place/pack_left.py)
```

![](py/place/pack_left.png)

### 右から左に順にpackする

```python
$import(py/place/pack_right.py)
```

![](py/place/pack_right.png)

### Widget間の幅を揃える

```python
$import(py/place/align.py)
```

![](py/place/align.png)


### 親Widgetが大きくなった時それに合わせてWidgetを大きくする

```python
$import(py/place/expand.py)
```

起動時の状態。３つのボタンはどれも同じ大きさ。

![](py/place/expand1.png)

ウィンドウを大きくすると、Button1はそのまま、Button2は水平方向にexpand、Button3は水平垂直方向にexpandする。

![](py/place/expand2.png)

### 絶対座標で配置する

```python
$import(py/place/absolute.py)
```

絶対座標で指定した位置にラベルが配置される。

![](py/place/absolute1.png)

ウィンドウを大きくしても位置は変わらない。

![](py/place/absolute2.png)


### 相対座標で配置する

```python
$import(py/place/relative.py)
```

相対座標で指定した位置にラベルが配置される。

![](py/place/relative1.png)

ウィンドウを大きくすると相対的な関係を保って移動する。

![](py/place/relative2.png)


### 格子状の配置をする

```python
$import(py/place/lattice1.py)
```

![](py/place/lattice1_1.png)

ウィンドウを広げてもついていかない。

![](py/place/lattice1_2.png)




```python
$import(py/place/lattice2.py)
```

ボタンのサイズが変わっても隙間を埋めてくれない。

![](py/place/lattice2_1.png)

この例もウィンドウを広げてもついていかない。

![](py/place/lattice2_2.png)


グリッドに対する配置方法は、grid()にstickyオプションで指定できる。なぜかここだけ東西南北で指定する。

* 上に寄せる：sticky="n" (north)
* 下に寄せる：sticky="s" (south)
* 左に寄せる：sticky="w" (west)
* 右に寄せる：sticky="e" (east)
* 左右一杯に広げる：sticky="we" (or "ew")
* 上下一杯に広げる：sticky="ns" (or "sn")
* 上下左右に広げる：sticky="news" (順不同)

```python
$import(py/place/lattice3.py)
```

上下左右に広がって配置される。

![](py/place/lattice3_1.png)

この例もウィンドウを広げてもついていかない。

![](py/place/lattice3_2.png)


ウィンドウのサイズを変えた時にグリッドのサイズを変えるには、Grid.columnconfigureとGrid.rowconfigureを用いる。第１引数が親Widget、第２引数が行・列番号、第３引数にオプションを指定する。

```python
$import(py/place/lattice4.py)
```

![](py/place/lattice4_1.png)

ウィンドウを広げると合わせてボタンも大きくなる。

![](py/place/lattice4_2.png)



weightを変えると大きくなる度合いを変更できる。

```python
$import(py/place/lattice5.py)
```

![](py/place/lattice5_1.png)

１行目の高さはそのまま、２行目の高さだけ変わり、２列目を1列目より２倍早く大きくなる。

![](py/place/lattice5_2.png)


### 格子状の配置で幾つかのセルをまたがらせる


```python
$import(py/place/lattice6.py)
```

![](py/place/lattice6.png)






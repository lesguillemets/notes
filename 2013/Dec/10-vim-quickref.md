Vim の quickref をつらつらよむ，他
------------------------------

`:help quickref` とかを読みながら目に留まったところを書き留めていくよ


#### N th column に行きたいぜ
`|bar|	N  |		to column N (default: 1)`

#### `f` とかの繰り返し
```
|;|  N  ;    repeat the last "f", "F", "t", or "T" N times
|,| N  ,    repeat the last "f", "F", "t", or "T" N times in
         opposite direction
```

#### 上下のちょっとかっこいい動き
```
|-|	N  -		up N lines, on the first non-blank character
|+|	N  +		down N lines, on the first non-blank character (also:
|_| N  _    down N-1 lines, on the first non-blank character
```

#### unclosed bracket への text object

```
|[(|	N  [(		N times back to unclosed '('
|[{|	N  [{		N times back to unclosed '{'
|])|	N  ])		N times forward to unclosed ')'
|]}|	N  ]}		N times forward to unclosed '}'
```

`:help Q_tm` の辺り他にも (for Java) とかあるのでやってみると良いと思う．

#### partial match も含めた `*` とか

```
|gstar| N  g*   like "*", but also find partial matches
|g#|  N  g#   like "#", but also find partial matches
```


すこしずつ書いてくでー．

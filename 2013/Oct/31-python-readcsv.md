Python から csv ファイルを読む
------------------------------

python でデータ扱うとなると csv ファイルとか読みたいよね，というわけで．

例によって `csv` モジュールがあるのでそれを使う．おそらくそこからデータ解析とかするのは `numpy` がよく似合うのではないか．
ということでついでに numpy つかったよー．

data.csv 読み込んで一列目を取り出し (`data[:,0]`), その標準偏差を出す

```python
#!/usr/bin/python
import numpy as np
import csv
with open("./data.csv", "rb") as csvfile: # opens file
    reader = csv.reader(csvfile, delimiter='\t') # reads file with delimiter \t
    # type(reader) => <type '_csv.reader'>
    data = np.array(list(reader), dtype=float)
    # print list(reader) => []

print np.std(data[:,0])
print data[:,0].std() # 標準偏差．どっちでもよい
```

`rb` でファイルを開いてるのはなんか改行コードがうにょうにょみたいな雰囲気．

`csv` module では読み書き両方できるようだが，とりあえず読み出しだけを考えてみる．
`csv.reader(csvfile, dialect='excel', **fmtparams)` で reader object がかえる．これは iterator.
`next()` とか `for row in reader` みたいな記法ができます．あと `csvreader.fieldnames` とか． `delimiter` を指定してる感じで `doublequote`, `escapechara` とかがあるようです．

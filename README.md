# AOJ
Aizu Online Judge  
本家（？）
http://judge.u-aizu.ac.jp/onlinejudge/  
やりやすい方
https://onlinejudge.u-aizu.ac.jp/home  
なむぱいはつかえない

*最後の出力の際に改行が無いとPEになる．

# VScodeスニペット
```json
	"map(int, input().split())":{
		"prefix": "mapint",
		"body": "map(int, input().split())",
		"description": "横のint型の入力",
	},

	"enumerate":{
        "prefix": "fore",
        "body": "for i, elem in enumerate():",
        "description": "インデックスも同時に",
	},
	
	"codeformat":{
		"prefix": ["format","solve",],
		"body": [
			"def solve():",
			"\t",
			"",
			"if __name__ == '__main__':",
            "\tsolve()",
        ],
		"description": "フォーマット"
	}
```

## 入力の種類
横にn個入力するパターンは  
```python
List = input().split() 
```

縦にn個入力するパターンは
```python
List = [input() for _ in range(n)]
#nは入力する数
```

横にn個出力するパターンは
```python
print(*List)
#めっちゃ便利
```

縦にn個出力するパターンは
```python
[print(x) for x in List]
```
## ALDS1
挿入ソート，最大公約数，素数判定，最大利益（FX取引）  
バブルソート，選択ソート，安定なソート，シェルソート  
スタック，キュー，双方向連結リスト，!水たまり問題!  
線形探索，二分探索，辞書，!割り当て!
総当たり探索（bit全探索），マージソート，コッホ曲線，!反転数!
計数ソート，分割

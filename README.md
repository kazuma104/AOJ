# AOJ

Aizu Online Judge
なむぱいつかえない

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

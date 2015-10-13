# coding: UTF-8
# お米

print "SEX"

# 変数
msg = "OPPAI"
print msg

# 数字 True False None
# 演算子 + - * / // % **
print 10 * 5 # 50
print 10 // 3 # 3
print 10 % 3 # 1
print 2 ** 3 # 8

#整数と小数の演算は少数になる
print 5 + 2.0 # 7.0

# 整数同士の割り算 → 切り捨ての整数
print 10 / 3 # 3
print 10 / 3.0 # 3.3333333333

# 文字列
# 日本語は u"おこんばんは"

print "hello " + "world"
print u"無駄！" * 10

# エスケープ \n \t \\
print "hello\n"

# データを改行付きで定義したい時は３つで囲う
print """<html lawng="ja">
<body>
ダブルクォートはかってにエスケープされる
</body>
</html>"""

# 文字列の関数
s = "abcdefghijklmn"
print len(s)
print s.find("c")
print s.find("z")
print s[2:5]
print s[:5]
print s[2:-1]

# 数値 <> 文字列
# 文字列 → 数値 int float
# 数値 → 文字列 str

# コレはエラー→  print 5 + "5"
print 5 + int("5")
print 5 + float("5")

age = 20
# コレはエラー→  print "i am " + age + " years old."
print "i am " + str(age) + " years old."

# 関数オブジェクト
# 要素が並んだもの
# - 文字列：文字が並んだもの
# - リスト：データが並んだもの

sales = [255, 200, 454, 499, "mojiretsu ok"];
# len + * []
print len(sales) # 5
print sales[2] # 454
sales[2] = "sex"
print sales[2]
# in
print 200 in sales # True
# range
print range(10) # 0,1,2,3,4,5,6,7,8,9
print range(3, 10) # 3,4,5,6,7,8,9
print range(3, 10, 2) # 3,5,7,9  2つ飛ばし

# sort / reverse
sales.sort()
print sales
sales.reverse()
print sales

# 文字列とリスト
d = "2013/12/15"
print d.split("/") # リストになる
a = ["a", "b", "c"]
print "-".join(a)


# - タプル：データが並んだもの(変更ができない)
a = (2,4,6)
# len + * []
print len(a) # 3
print a * 3
# a[2] = 10 これはエラー
# 変更できないデータなので早かったりセーフなコードになる

# タプル <> リスト
b = list(a)
print b
# 戻せる
c = tuple(b)
print c


# - セット：データが並んだもの(重複を許さない)
a = set([1,2,3,4])
print a
a = set([1,2,3,4,3,2]) #重複されてるものは無視される
print a

b = set([3,4,5])
# -
print a - b # aにないものが出てくる

# |
print a | b # 両方のものを合わせて表示

# &
print a & b # 両方にあるものだけ

# ^
print a ^ b # どちらかにしかないものを表示



# - 辞書：キーと値がペア
[2505, 523, 500]
sales = { "shichiku": 1000, "yuki": 23432, "sato": 9857}
print sales
print sales["shichiku"]
sales["sato"] = 12345678
print sales

# in
print "taguchi" in sales # True
# keys それぞれリスト型で帰ってくる
print sales.keys()
print sales.values()
print sales.items()


# 文字列にデータを入れる
a = 10
b = 1.2343564
c = "shichiku"
d = {"shichiku": 233334545, "sex":3487385}

print "age: %d" % a  # desimal
print "age: %10d" % a  # desimal
print "age: %010d" % a  # desimal
print "age: %f" % b  # float
print "age: %.2f" % b  # float
print "name: %s" % c# string

print "sales :%(shichiku)d" % d # dictionary
print "%d / %f" % (a, b)


# if文

score = 70
if score > 60:
  print "ok!"
  print "sex!"

# > < >= <= == !=
# and or not

if score > 60 and score < 90:
  # これでもいい→  if 60 < score < 90:
  print "fuck"

if score > 50:
  print "ok!!!"
elif score > 40:

  print "......."
else:
  print "fucking"

print "OK!" if score > 60 else "NG"


# for loop

sales = [13, 3523, 31, 238]
sum = 0
for sale in sales:
  sum = sum + sale
  # sum += sale
  print sale
else: #for後に一回だけ処理
  print sum
print sum

# continue break
for i in range(10):
  if i == 3:
    continue
  print i
  if i == 7:
    break


# dictionary for
users = {"shichiku": 23489, "hige": 3342, "guho": 238473}
for key, value in users.iteritems():
  print "key: %s value: %d" % (key, value)
for key in users.iterkeys():
  print key
for value in users.itervalues():
  print value


n = 0
while n < 10:
  if n == 3:
    n += 1
    continue
  print n
  n += 1
else:
  print "while end"



# 関数
def hello():
  print "hello"

hello()

# args
def seyhello(name, num = 3):
  return "hello %s" % name * num

print seyhello("sex")
print seyhello("OPPAI", 3)


#変数のスコープ
name = "yuki"
def hello():
  name = "shichiku"

print name # yukiになる。まぁね。

# pass
def hello2():
  pass # jsみたいに空にすれば良いものと違って、なんか書かないといけないからpassって書くと何もしない


# リスト の各要素に 関数 を適用させる map

def double(x):
  return x * x
print map(double, [2, 5, 8])

# 無名関数 lambda
print map(lambda x: x * x, [2,5,8])


# オブジェクト 変数と関数をまとめて扱う
# クラス : オブジェクトの設計図
# インスタンス : クラスを実体化したものがインスタンス
class User(object):
  def __init__(self, name):
    self.name = name
  def greet(self):
    print "my name is %s!" % self.name

bob = User("Bob")
shichiku = User("shichiku")

print bob.name
shichiku.greet()

# クラスの継承 上のUserを継承する

# Userを引数にいれるだけなんだーなるほど。
class SuperUser(User):
  def shout(self):
    print "FUCKIN %s!!!!!!" % self.name

antonio = SuperUser("unko")
antonio.shout()


# モジュールを使ってみる。ｐｙてょｎが持ってる。
# doc にあるぽい global module hogehoge

import math, random
from datetime import date # datetime の中の date を import
print date.today()
print math.ceil(5.2) # 6
for i in range(5):
  print random.random()



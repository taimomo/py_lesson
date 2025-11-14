# Week1 - Day1

# --- 基本の型 ---
num = 10           # int型の変数
pi = 3.14          # float型の変数
message = "Hello"  # str型の文字列
flag = True        # bool変数

print("num:", num)
print("pi:", pi)
print("message:", message)
print("flag:", flag)

# --- 算術 ---
a = 15
b = 4
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)  # 整数除算
print("a % b =", a % b)

# --- 条件分岐 ---
temperature = 28

if temperature >= 30:
    print("暑い！")
elif temperature >= 20:
    print("快適")
else:
    print("寒い…")

# --- for 文 ---
print("0〜4 をループ表示")
for i in range(5):
    print(i)

# --- while 文 ---
count = 3
while count > 0:
    print("カウント:", count)
    count -= 1

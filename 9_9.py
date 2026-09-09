import random

# 随机生成1~10之间的整数
secret_num = random.randint(1, 10)
print("=== 猜数字游戏 ===")
print("我想了一个1到10之间的数字，你来猜猜看！")

while True:
    guess = int(input("请输入你猜的数字："))
    if guess < secret_num:
        print("小了，再试试！")
    elif guess > secret_num:
        print("大了，再试试！")
    else:
        print(f"恭喜你猜对啦！数字就是{secret_num}")
        break

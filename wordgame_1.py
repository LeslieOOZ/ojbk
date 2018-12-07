import random
print("...............鱼C.............")
ser = random.randint(1,10)
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
while guess !=ser:
    temp = input("重新输入：")
    guess = int(temp)

    if guess == ser:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > ser:
            print("大了大了。")
        else:
            print("小了小了。")
print("游戏结束，不玩啦")

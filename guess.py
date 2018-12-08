import random
secret = random.randint(1,99)
guess = 0
tries = 0
print('我有一个秘密，它是1-10之间的一个数字，下面我给你6次机会！')
while guess != secret and tries < 6:
    guess = input('你猜的数字是什么：')
    if guess < secret:
        print('too low!')
    elif guess > secret:
        print('too high!')
    tries = tries + 1
if guess == secret:
    print('you are right!')
else:
    print('no more guess!')
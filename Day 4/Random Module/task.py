import random
import my_module

# rand_num = random.randint(1, 10)
# print(rand_num)
# print(my_module.my_favorite_number)
#
rand_coin_toss = round(random.random() * 1)
# print(rand_coin_toss)

if rand_coin_toss == 0:
    print("heads")
else:
    print("tails")
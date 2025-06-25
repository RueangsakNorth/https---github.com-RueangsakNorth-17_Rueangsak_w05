import random
# print(f"{random.random}")
# print(f"{random.randint(1,99)}")
# print(f"{random.randrange(1,99,30)}")
# print(f"{random.uniform(1,100):.9f}")
# colors = ["red" , "green" , "blue" , "black"]
# random_list = random.choice(colors) #สุ่มช
# print(random_list)

colors = ["red" , "green" , "blue" , "black"]
# random_3 = random.choices(colors, k=3) #สุ่มช้อยออกมา3
# print(random_3)
random_uniq = random.sample(colors,3) #สุ่มช้อยออกมา3
print(random_uniq)

number=list(1,100)
num_shuf = random.shuffle(number)
print(number)
# coding: utf-8
import random

# testing set 250
testing_set = []

training_set_1500 = []
training_set_2000 = []
training_set_2500 = []
training_set_3000 = []
training_set_4000 = []

charac_file = "../charset/chinese_characters.txt"
with open(charac_file, "r") as f:
    charset = f.readlines()
    charset = [char.strip() for char in charset]
    print(len(charset))
    print(charset)

    random.shuffle(charset)
    random.shuffle(charset)
    random.shuffle(charset)


    radio = 0.03719131
    for c in charset:
        r = random.random()
        print(r)
        if r < radio:
            testing_set.append(c.strip())

    print(len(testing_set))
    print(testing_set)
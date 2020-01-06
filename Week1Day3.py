#Task 2 Counting Animals
chickens = 2
cows = 4
pigs = 4

#animals(2,3,5) = 36
#animals(1, 2, 3) = 22
#animals(5, 2, 8) = 50
animals = ((chickens*2)+(cows*3)+(pigs*5))
print(animals)
animals = ((chickens)+(cows*2)+(pigs*3))
print(animals)
animals = ((chickens*5)+(cows*2)+(pigs*8))
print(animals)

#Task 3
#workers(147, 33, 526) = 493
#workers(33, 72, 74) = 41
#workers(1, 5, 9) = 8
if 147 > 526:
    print(false)
elif 33 > 526:
    print(false)
else:
    print(526-33)

if 33 > 74:
    print(false)
elif 72 > 74:
    print(false)
else:
    print(74-33)

if 1 > 9:
    print(false)
elif 5 > 9:
    print(false)
else:
    print(9-1)
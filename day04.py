# Assignment 8.6~8.9

life = dict(animals=dict(cats="Henri", octopi="Grumpy", emus="Lucy"),
            plants=dict(),
            other=dict())
life2 = {'animals':{'cats':'Henri','octopi':'Grumpy','emus':'Lucy'},
         'plants':{},
         'other':{}}
print(life2)
print(life)

# 8.7

print(list(life.keys()))

# 8.8

print(list(life['animals'].keys()))

# 8.9

print(life['animals']['cats'])

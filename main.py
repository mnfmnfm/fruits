fruits = ["apple", "banana", "cantaloupe", "dragonfruit"]
for fruit in fruits:
    print(fruit)

user_fruit = input("what is your favorite fruit?\n")
if user_fruit in fruits:
    print("good job, that is a fruit")
else:
    print("sorry, that is not a fruit, there are only 4 fruits: " + ", ".join(fruits))
fruits = ["apple", "banana", "cantaloupe", "dragonfruit", "carrot"]
for fruit in fruits:
    print(fruit)

while True:
    user_fruit = input("what is your favorite fruit?\n")
    if user_fruit in fruits:
        print("good job, that is a fruit")
        break
    else:
        print("sorry, that is not a fruit, there are only 4 fruits: " + ", ".join(fruits))
        print("please try again")
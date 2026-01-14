fruits = ["apple", "banana", "cantaloupe", "dragonfruit", "elderberry"]
for fruit in fruits:
    print(fruit)

while True:
    user_fruit = input("what is your favorite fruit?\n")
    if user_fruit in fruits:
        print(f"good job, {user_fruit} is a fruit, you are good at fruit")
        break
    else:
        print("sorry, that is not a fruit, there are only 4 fruits: " + ", ".join(fruits))
        print("please try again")
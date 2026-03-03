print("Hello! I'm an AI bot. What's your name?: ")
name = input()
print(f"Nice to meet you, {name}!")

while True:
    print("\nHow are you feeling today? (good/bad/okay/other): ")
    mood = input().lower()

    if mood == 'good':
        print("That's great! Keep smiling!")
    elif mood == 'bad':
        print("I'm sorry to hear that. I hope things get better soon.")
    elif mood == 'okay':
        print("I understand. Some days are just okay.")
    else:
        print("It's ok, sometimes it is hard to describe feelings.")

    print("\nLet's chat! Choose a topic: hobbies, favorite color, or pets")
    topic = input().lower()

    if topic == "hobbies":
        print("Cool! What hobby do you enjoy the most? ")
        hobby = input()
        print(f"Nice! {hobby} sounds really nice! ")
    elif topic == "favorite color":
        print("What's your favorite color? ")
        color = input()
        print(f"{color} is a beautiful color! ")
    elif topic == "pets":
        print("Do you have any pets? (yes/no)")
        has_pet = input().lower()
        if has_pet == "yes":
            print("Pets are the best companions! ")
        else:
            print("Pets aren't for everyone, but they can be fun. ")
    else:
        print("Hmm, that's an interesting topic! ")

    print("\nDo you want to continue chatting? (yes/no)")
    repeat = input().lower()
    if repeat != "yes":
        print(f"It was nice talking to you, {name}! Goodbye!")
    else:
        print('It was nice chatting with you! See you again!')
        break
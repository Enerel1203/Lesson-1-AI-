print("Hello! I'm an AI bot. What's your name?: ")

name=input()

print(f"Nice to meet you, {name}!")

print("How are you? (good/bad): ")
mood=input().lower()

if mood == 'good':
    print("I'm glad to hear that!")
elif mood == 'bad':
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print("I see. Sometimes it's hard to put your feelings into words")

    
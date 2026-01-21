import webbrowser

print("Hello! I'm an AI bot. What's your name?: ")

name=input()

print(f"Nice to meet you, {name}!")

print("Which website do you want to open? (Example: youtube, google, wikipedia): ")
site_name=input().strip().lower()

url=f"https://www.{site_name}.com"

print(f"Opening {url} now...")
webbrowser.open(url)

print(f"It was nice chatting with you {name}. Bye!")

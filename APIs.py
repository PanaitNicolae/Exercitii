import requests


def print_jokes(jokes):
    no = 1
    if isinstance(jokes, list):
        for elem in jokes:
            for i, j in elem.items():
                if i == "setup":
                    print (no,".",j)
                elif i == "punchline":
                    print("       ",j)
            no += 1
    else:
        for i, j in jokes.items():
            if i == "setup":
                print(1, ".", j)
            elif i == "punchline":
                print("     ", j)
    print()


def check_jokes_type(jokes):
    type = jokes[0]["type"]
    for elem in jokes:
        for i, j in elem.items():
            if i == "type" and j != type:
                print("Not all jokes are the same type!")
                return 0
    print("Al jokes have the type: ", type)

def display_odd_id(jokes):
    print("Odd id jokes are:")
    for elem in jokes:
        for i, j in elem.items():
            if i == "id" and j % 2 != 0:
                print_jokes(elem)

def display_even_id(jokes):
    print("Even id jokes are:")
    for elem in jokes:
        for i, j in elem.items():
            if i == "id" and j % 2 == 0:
                print_jokes(elem)

random_joke = requests.get("https://official-joke-api.appspot.com/random_joke")
ten_random_jokes = requests.get("https://official-joke-api.appspot.com/random_ten")
jokes_by_type = requests.get("https://official-joke-api.appspot.com/jokes/programming/ten")

# print_jokes(random_joke.json())
# print_jokes(ten_random_jokes.json())
# check_jokes_type(jokes_by_type.json())
display_odd_id(ten_random_jokes.json())
display_even_id(ten_random_jokes.json())
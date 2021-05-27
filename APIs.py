import requests

common_link = "https://official-joke-api.appspot.com/"


def get_random_joke():
    return requests.get(common_link+"random_joke").json()


def get_ten_random_jokes():
    return requests.get(common_link+"random_ten").json()


def get_jokes_by_type():
    return requests.get(common_link+"jokes/programming/ten").json()


def print_jokes(jokes):
    no = 1
    if isinstance(jokes, list):
        for elem in jokes:
            print(f"{no}. {elem['setup']}\n     {elem['punchline']}")
            no += 1
    else:
        print(f"1. {jokes['setup']}\n     {jokes['punchline']}")



def check_jokes_type(jokes, type):
    no = 0
    for elem in jokes:
        if elem["type"] == type:
            no += 1
    interpret_jokes_type(jokes,no, type)


def interpret_jokes_type(jokes, no, type):
    if no == len(jokes):
        print("All jokes have the type:", type)
    elif no > 0:
        print(no, "jokes have the type", type)
    else:
        raise Exception("No jokes of this type!")


def print_odd_even_id(jokes, mode):
    """
        mode = 1 => print ODD jokes
        mode = 0 => print EVEN jokes
    """
    if mode:
        print("Odd id jokes are:")
    else:
        print("Even id jokes are:")
    for elem in jokes:
        if elem["id"] % 2 != 0 and mode == 1:
            print_jokes(elem)
        elif elem["id"] % 2 == 0 and mode == 0:
            print_jokes(elem)


# print_jokes(get_random_joke())
# print_jokes(get_ten_random_jokes())
check_jokes_type(get_jokes_by_type(), "progrming")
# print_odd_even_id(get_ten_random_jokes(), 1)

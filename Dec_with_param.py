
def do_it_n_times(n):
    def inner_function(func):
        def wrapper_repeat():
            for i in range(n):
                func()
        return wrapper_repeat

    return inner_function

@do_it_n_times(7)
def count_to_five():
    for i in range(5):
        print(i+1, end = " ")
    print()

count_to_five()
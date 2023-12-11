from random import randint, choice, shuffle


def welcome():
    print("Welcome to the PyPassword Generator!")


def take_int_input(message):
    print(message)
    n = int(input())
    return n


def generate_random_letter():
    x = randint(65, 90)
    y = randint(97, 122)
    z = choice([x, y])
    return chr(z)


def generate_random_symbol():
    x = randint(33, 47)
    return chr(x)


def generate_random_number():
    x = randint(0, 9)
    return str(x)


def get_input():
    num_letters = take_int_input("How many letters would you like in your password?")
    num_symbols = take_int_input("How many symbols would you like?")
    num_nums = take_int_input("How many numbers would you like?")
    return num_letters, num_symbols, num_nums


def generate_password(num_letters, num_symbols, num_nums):
    chars = [ generate_random_letter() for _ in range(num_letters) ] + \
            [ generate_random_symbol() for _ in range(num_symbols) ] + \
            [ generate_random_number() for _ in range(num_nums) ]
    shuffle(chars)
    password = "".join(chars)
    return password


def run():
    welcome()
    num_letters, num_symbols, num_nums = get_input()
    password = generate_password(num_letters, num_symbols, num_nums)
    print(f"Your password is: {password}")


if __name__ == "__main__":
    run()
#initiate film-stock reciprocity factor (p-factor)
portra400 = 1.35
colorplus = 1.3
hp5 = 1.32
trix = 1.54
other = 1.33

def print_films():
    print()
    print("1: portra400")
    print("2: colorplus")
    print("3: hp5")
    print("4: trix")
    print("5: other")

def get_stock():
    print("What is your film stock? ")
    print_films()
    user_input = input()
    if user_input == "1":
        film_stock = portra400
    elif user_input == "2" :
        film_stock = colorplus
    elif user_input == "3" :
        film_stock = hp5
    elif user_input == "4" :
        film_stock = trix
    elif user_input == "5" :
        film_stock = other
    return film_stock

def get_shutter():
    print("what is your suggested shutter speed? (1/30, 1/15, 1, 2, etc..")
    shutter = float(input())
    return shutter

def calc_reciprocity(film_stock, shutter):
    if shutter > 1 :
        reciprocity = round(shutter**film_stock, 2)
        print("new time: ")
        print(reciprocity)
    else :
        print("don't need to account for reciprocity")


def main():
    calc_reciprocity(get_stock(), get_shutter())

main()
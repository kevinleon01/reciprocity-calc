#initiate film-stock reciprocity factors (p-factor)
portra400 = 1.35
pancro400 = 1.3
hp5 = 1.32
trix = 1.54
cinestill800t = 1.33
tmax400 = 1.24
tmax100 = 1.15
other = 1.33

#film menu
def print_films():
    print()
    print("1: portra 400")
    print("2: pancro 400")
    print("3: hp5")
    print("4: trix")
    print("5: Cinestill 800T")
    print("6: tmax 400")
    print("7: tmax 100")
    print("8: other")

#gets p-factor
def get_stock():
    print("What is your film stock? ")
    print_films()
    user_input = input()
    if user_input == "1":
        film_stock = portra400
    elif user_input == "2" :
        film_stock = pancro400
    elif user_input == "3" :
        film_stock = hp5
    elif user_input == "4" :
        film_stock = trix
    elif user_input == "5" :
        film_stock = cinestill800t
    elif user_input == "6" :
        film_stock = tmax400
    elif user_input == "7" :
        film_stock = tmax100
    elif user_input == "8" :
        film_stock = other
    return film_stock

#gets initial shutter speed
def get_shutter():
    print("what is your suggested shutter speed? (1/30, 1/15, 1, 2, etc..")
    shutter = float(input())
    return shutter

#calculates appropriate speed for film's p-factor
def calc_reciprocity(film_stock, shutter):
    if shutter > 1 :
        reciprocity = round(shutter**film_stock, 2)
        print()
        print("new time: ")
        print(reciprocity, " seconds")
    else :
        print()
        print("don't need to account for reciprocity")


def main():
    calc_reciprocity(get_stock(), get_shutter())

main()
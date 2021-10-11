def searchname():
    infile = open("names.txt", "r")
    for s in infile:
        print (s[:-1])


def display_names():
    infile = open("names.txt", "r")
    for s in infile:
        if s[0].lower() == "a":
            print(s[:-1])

def search_name():
    infile = open("names.txt", "r")
    first_letter = input("Enter the search letter:\n")
    for s in infile:
        if s[0].lower() == first_letter[0].lower():
            print(s[:-1])


def search_age():
    infile = open("names.txt", "r")
    age = input("Enter the search age:\n")
    for s in infile:
        if age in s:
            print(s[:-1])




def searchage():
    infile = open("names.txt", "r")
    for s in infile:
        if str(5) in s:
            print(s[:-1])



def main():
    search_options = int(input("Enter your search choice:\n 1 for search by name: \n 2 for search by age: \n"))
    if int(search_options) == 1:
        search_name()
    elif int(search_options) == 2:
        search_age()
    else:
        print("Invalid choice ; Try again")


def search_age2():
    infile = open("names.txt", "r")
    display_age = int(input("Enter the search age: \n"))
    search_creteria = int(input("Enter age search creteria:\n 1 display age equal to:\n 2 display age less or equal to:\n 3 display age greater or equal to:\n"))
    for s in infile:
        name_age = s.split()
        age = int(name_age[1])
        if search_creteria == 1:
            if display_age == age:
                print(s[:-1])
        elif search_creteria == 2:
            if display_age >= age:
                print(s[:-1])
        elif search_creteria == 3:
            if display_age <= age:
                print(s[:-1])

search_age2()
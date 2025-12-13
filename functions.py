class car:
    def __init__(self,id,name,make,body,year,value):
        self.__id = id
        self.__name = name
        self.__make = make
        self.__body = body
        self.__year = year
        self.__value = value
        
    def __str__(self):
        return f"{self.__id}, {self.__name}, {self.__make}, {self.__body}, {self.__year}, {self.__value}"
    def set_name(self,new_name):
        self.__name = new_name
    def set_id(self,new_id):
        self.__id = new_id
    def set_make(self,new_make):
        self.__make = new_make
    def set_body(self,new_body):
        self.__body = new_body
    def set_year(self,new_year):
        self.__year = new_year
    def set_value(self,new_value):
        self.__value = new_value
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_make(self):
        return self.__make
    def get_body(self):
        return self.__body
    def get_year(self):
        return self.__year
    def get_value(self):
        return self.__value
def main_menu():
    '''
    loop for the main menu,
    returns the user input if it's 1 through 6
    '''
    check_loop = True
    while check_loop:
        print("What would you like to do today?")
        print("-Add a car? enter 1")
        print("-Search for car 2")
        print("-Edit car info? enter 3")
        print("-Remove a car? enter 4")
        print("-Print the car list? enter 5")
        print("-Save the data to a file? enter 6")
        print("-Exit the program? Enter 0")
        user_input = int(input(""))
        if user_input == 1 or user_input == 2 or user_input == 3 or user_input == 4 or user_input == 5 or user_input == 6 or user_input == 0:
            check_loop = False
    return user_input
def search_id(cars,id):
    '''
    Docstring for search_id
    searches the list by calling the id attribute of each class & comparing it to the user input
    does not return anything
    :param cars: list of car classes
    :param id: user inputted ID
    '''
    id_index = -1
    for vehicle in cars:
        if vehicle.get_id() == id:
            id_index = cars.index(vehicle)
    return id_index

def search_name(carlist,name):
    '''
    searches the list by calling the name attribute of each class & comparing them to the user input
    does not return anything
    called by run_search function
    :param cars: list of car classes
    :param name: user submitted first name
    '''
    car_index = -1
    for vehicle in carlist:
        if vehicle.get_name() == name:
            car_index = carlist.index(vehicle)
    return car_index

def add_car(carlist,id,name,make,body,year,value):
    '''
    Takes the user submitted info for a new car, checks if the name or id has already been used, then if both are available it creates a new car class with the info and appends the list with it
    returns the updated list
    runs through run_add_car
    :param carlist: list of car classes
    :param id: user submitted ID
    :param name: user submitted name
    :param make: user submitted make
    :param body: user submitted body
    :param year: user submitted year
    :param value: user submitted value
    '''
    check_id = True
    check_name = True
    for vehicle in carlist:
        if vehicle.get_id() == id:
            check_id = False
        if vehicle.get_name() == name:
            check_name = False
    if check_id == False:
        print("ERROR")
        print("ID already in the system")
    elif check_name == False:
        print("The car is already in inventory. No action is required.")
    else:
        new_car = car(id,name,make,body,year,value)
        carlist.append(new_car)
        print("Vehicle added to inventory")
        print(str(carlist[-1]).replace(",", "  "))
    return carlist

def remove_car(carlist,id):
    id_check = False
    for vehicle in carlist:
        if vehicle.get_id() == id:
            carlist.pop(carlist.index(vehicle))
            id_check = True
            print("Car removed")
    if id_check == False:
        print("Car not found")
    return carlist

def edit_car(carlist,id):
    '''
    takes the id user inputted from run_edit_car and, if found in the list, replaces the info with the user submitted info
    returns the updated list
    called through run_edit_car
    
    :param carlist: list of car classes
    :param id: id of car to edit
    '''
    id_check = False
    for vehicle in carlist:
        if vehicle.get_id() == id:
            print("Name:")
            input_name = input("")
            vehicle.set_name(input_name)
            print("Make:")
            input_make = input("")
            vehicle.set_make(input_make)
            print("Body:")
            input_body = input("")
            vehicle.set_body(input_body)
            print("Year:")
            input_year = int(input(""))
            vehicle.set_year(input_year)
            print("Value:")
            input_value = float(input(""))
            vehicle.set_value(input_value)
            id_check = True
            print("Car's new info is:", str(vehicle).replace(",", "  "))
    if id_check == False:
        print("Car not found")
    return carlist

def run_search_car(carlist):
    '''
    function for running the search car function
    
    :param carlist: list of car classes
    '''
    loop_check = True
    while loop_check:
        print("To search using the Id enter 1. To search using the name enter 2. Enter -1 to return to the previous menu")    
        user_input = int(input(""))
        if user_input == 1:
            print("Please Enter the id of the car")
            input_id = int(input())
            id_index = search_id(carlist,input_id)
            if id_index != -1:
                print("Car found")
                print(str(carlist[id_index]).replace(",","  "))
            else:
                print("Car not found")
        elif user_input == 2:
            print("Please enter the name of the car")
            input_name = input("")
            car_index = search_name(carlist,input_name,)
            if car_index != -1:
                print("Car found")
                print(str(carlist[car_index]).replace(",", "  "))
            else:
                print("Car not found")
        elif user_input == -1:
            loop_check = False

def run_add_car(carlist):
    '''
    function for running the add scar function
    
    :param carlist: list of car classes
    '''
    loop_check = True
    while loop_check:
        print("Enter id of the car, followed by the car's information")
        print("ID:")
        input_id = int(input(''))
        print("Name:")
        input_name = input("")
        print("Make:")
        input_make = input("")
        print("Body:")
        input_body = input("")
        print("year:")
        input_year = int(input(""))
        print("Value:")
        input_value = float(input(""))
        carlist = add_car(carlist,input_id,input_name,input_make,input_body,input_year,input_value)
        print("Would you like to add another car? (y/yes to continue, n/no to stop)")
        checky = True
        while checky:
            choice = input("").lower()
            if choice == "yes" or choice == "y":
                checky= False
                continue
            if choice == "no" or choice == "n":
                loop_check = False
                checky = False
            else:
                print("Please Enter a valid response.")
    

    return carlist

def run_edit_car(carlist):
    '''
    function for running the edit car function
    
    :param carlist: list of car classes
    '''
    loop_check = True
    while loop_check:
        print("Enter the id of the car. Enter -1 to return to the previous menu")
        input_id = int(input(""))
        if input_id == -1:
            loop_check = False
            pass
        else:
            carlist = edit_car(carlist,input_id)
    return carlist
def run_remove_car(carlist):
    '''
    function for running the remove car function
    
    :param carlist: list of car classes
    '''
    loop_check = True
    while loop_check:
        print("Enter the id of the car you want to remove from inventory.")
        input_id = int(input(""))
        carlist = remove_car(carlist,input_id)
        print("Would you like to remove more cars? y(yes)/n(no)")
        loop_checker = input("").lower()
        if loop_checker == "y" or loop_checker == "yes":
            loop_check = True
        elif loop_checker == "n" or loop_checker == "no":
            loop_check = False
    return carlist
def print_list(carlist):
    '''
    prints the list of car classes
    doesn't return anything
    
    :param carlist: list of car classes
    '''
    for vehicle in carlist:
        print(str(vehicle).replace(",", "  "))
def save_info(carlist):
    '''
    Saves the strings from the car classes to the data.txt file
    doesn't return anything
    
    :param carlist: list of car classes
    '''
    with open("data.txt", "w") as f:
        for car in carlist:
            f.write(str(car) + "\n")
    print(f"{len(carlist)} car(s) saved successfully.")
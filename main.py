import functions as fn
carlist = []
with open("data.txt") as f:
    for x in f:
        car_info = x.split(" ")
        new_car = fn.car(int(car_info[0]),car_info[1],car_info[2],float(car_info[3]),int(car_info[4]))
        carlist.append(new_car)

print("Welcome to the Car Management System")
checker = True 

while checker:
    option = fn.main_menu()

    if option == 1:
        fn.run_add_car(carlist)
    elif option == 2:
        fn.run_search_car(carlist)
    elif option == 3:
        fn.run_edit_car(carlist)
    elif option == 4:
        fn.run_remove_car(carlist)
    elif option == 5:
        fn.print_list(carlist)
    elif option == 6:
        fn.save_info(carlist)
    elif option == 0:
        print("Exiting program immediately. Goodbye!")
        checker = False

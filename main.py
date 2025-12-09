import functions as fn
carlist = []
with open("data.txt") as f:
    for x in f:
        car_info = x.split(" ")
        new_car = fn.car(int(car_info[0]),car_info[1],car_info[2],float(car_info[3]),int(car_info[4]))
        carlist.append(new_car)
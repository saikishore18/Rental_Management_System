import vehicles_list


def index():
    print("======================//Rent/hire a vehicle//====================")
    print("select the vehicle type: ")
    print("1.car \n 2.byke \n 3.auto ")
    try:
        ip = int(input("select the vehicle type: "))
        if ip == 1:
            print("the available list of cars are: ")
            vehicles_list.list_of_cars()
        elif ip == 2:
            print("the available list of bykes are: ")
            vehicles_list.list_of_bykes()
        elif ip == 3:
            vehicles_list.auto()
        else:
            print("NO vehicle selected!!!!!")

    except Exception as e:
        print(e.args)


index()

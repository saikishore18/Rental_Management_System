class thar:
    def price(self):
        print("1.3500/1hr\n 2.1day/12000 \n3.50000/month")
        rental_type = int(input())
        if rental_type == 1:
            hrs = int(input("how many hrs: "))
            print("you have to pay:  ", hrs * 3500)
        elif rental_type == 2:
            days = int(input("how many days: "))
            print("you have to pay:  ", days * 12000)
        else:
            print("you have to pay 50000 ")


class xuv(thar):
    pass


class scorpio(thar):
    pass


class defender(thar):
    pass


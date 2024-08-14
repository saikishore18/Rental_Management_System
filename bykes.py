class scooty:
    def price(self):
        print("1.300/1hr\n 2.1day/1000")
        rental_type = int(input())
        if rental_type == 1:
            hrs = int(input("how many hrs: "))
            print("you have to pay:  ", hrs * 300)
        elif rental_type == 2:
            days = int(input("how many days: "))
            print("you have to pay:  ", days * 1000)
        else:
            print("byke not available ")


class ola_electric:
    def e_price(self):
        print("1.150/1hr\n 2.1day/500")
        rental_type = int(input())
        if rental_type == 1:
            hrs = int(input("how many hrs: "))
            print("you have to pay:  ", hrs * 150)
        elif rental_type == 2:
            days = int(input("how many days: "))
            print("you have to pay:  ", days * 500)
        else:
            print("byke not available ")


class RE_standard_350:
    def rePrice(self):
        print("1.900/1hr\n 2.1day/5000")
        rental_type = int(input())
        if rental_type == 1:
            hrs = int(input("how many hrs: "))
            print("you have to pay:  ", hrs * 900)
        elif rental_type == 2:
            days = int(input("how many days: "))
            print("you have to pay:  ", days * 5000)
        else:
            print("byke not available ")


class RX100:
    def rxprice(self):
        print("1.100/1hr\n 2.1day/600")
        rental_type = int(input())
        if rental_type == 1:
            hrs = int(input("how many hrs: "))
            print("you have to pay:  ", hrs * 100)
        elif rental_type == 2:
            days = int(input("how many days: "))
            print("you have to pay:  ", days * 600)
        else:
            print("byke not available ")

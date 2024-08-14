from cars import thar, defender, xuv, scorpio
from bykes import scooty, ola_electric, RE_standard_350, RX100
from auto import cng,electric


def list_of_cars():
    print("1.thar \n 2.xuv \n 3.scorpio \n 4.defender ")
    ctype = int(input(""))
    if ctype == 1:
        thar().price()
    elif ctype == 2:
        xuv().price()
    elif ctype == 3:
        scorpio().price()
    elif ctype == 4:
        defender().price()
    else:
        print("car unavailable!!!!!")


def list_of_bykes():
    print("1.scooty \n 2.ola electric \n 3.RE standard 350 \n 4.RX100 ")
    btype = int(input(""))
    if btype == 1:
        scooty().price()
    elif btype == 2:
        ola_electric().e_price()
    elif btype == 3:
        RE_standard_350().rePrice()
    elif btype == 4:
        RX100().rxprice()
    else:
        print("byke unavailable!!!!!")


def auto():
    print("1.CNG \n 2.Electric ")
    atype = int(input())
    if atype == 1:
        cng().price()
    elif atype == 2:
        electric().e_price()
    else:
        print("select any AUTO first!!!")

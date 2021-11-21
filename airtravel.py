from aircraft import AirbusA319, Boeing777
from flight import Flight, console_card_printer


def make_fligts():

    f = Flight("BA758",AirbusA319("G-EUPT"))
    f.allocate_seat("1C","Kerim Embel")
    f.allocate_seat("15F","Bjarne Stroustrup")
    f.allocate_seat("1A","Ulaşcan Çakmak")
    f.allocate_seat("1B","Doğukan Demirtaş")
    f.allocate_seat("1D","Onur Uysal")

    g = Flight("AF72",Boeing777("F-GSPS"))
    g.allocate_seat("55J","Larry Wall")
    g.allocate_seat("52F","Yukihiro Matsumoto")
    g.allocate_seat("33G","Satoshi Makamoto")
    g.allocate_seat("4B","Brian Kerninghan")
    g.allocate_seat("1A","Dennis Ritchie")

    return f,g


f,g = make_fligts()

print(f.aircraft_model())
print(g.aircraft_model())
print(f.num_available_seats())
print(g.num_available_seats())
g.reallocate_seat("55J","54J")
g.make_boarding_cards(console_card_printer)
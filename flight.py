
from pprint import pprint

class Flight:
    '''A flight object with a particular passenger aircraft.'''
    def __init__(self,number, aircraft):

        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"No airline code in '{number}'")

        self._number = number
        self._aircraft = aircraft
        row, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in row]

    def number(self):
        return self._number

    def aircraft_model(self):
        return self._aircraft.model()
    
    def seating(self):
        pprint(self._seating)
    
    def allocate_seat(self,seat, passenger):
        '''
        Allocate a seat for a passenger.

        Args:
            seat: A seat designator such as '11B' or '15A'.
            passenger: The passenger name.
        Raises:
            ValueError: If the seat is unavailable.
        '''

        row, letter = self.parse_seat(seat)

        if(self._seating[row][letter] is not None):
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passenger


    def reallocate_seat(self,from_seat, to_seat):
        '''
        Reallocate a passenger to a different seat.

        Args:
            from_seat: Current seat of passenger.
            to_seat  : New seat for passenger.
        Raises:  
            ValueError: If the seat is unavailable or there are no passenger in current seat.
        '''

        from_row, from_letter = self.parse_seat(from_seat)

        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat{from_seat}")

        to_row, to_letter = self.parse_seat(to_seat)

        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


    def passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")

    def num_available_seats(self):

        return sum(sum(1 for s in row.values() if s is None)
                    for row in self._seating
                    if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self.passenger_seats()):
            card_printer(passenger,seat,self.number(),self.aircraft_model())

    def parse_seat(self, seat):

        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter '{letter}'")
        
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row '{row_text}'")

        if row not in rows:
            raise ValueError(f"Invalid row number '{row}'")

        return row, letter


def console_card_printer(passenger, seat, flight_number, aircraft):

    output = f"|Name : {passenger}"      \
             f" Flight: {flight_number}" \
             f" Seat: {seat}" \
             f" Aircraft: {aircraft}" \
             " |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"

    lines = [banner,border,output,border,banner]
    card = "\n".join(lines)
    print(card)
    print()
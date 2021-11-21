class Aircraft:
    '''Model for aircraft Flights.'''

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
    
    def registration(self):
        return self._registration
    
    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1,self._num_rows + 1),
        "ABCDEFGHJK"[:self._num_seats_per_row])
    
    def num_seats(self):
        rows , row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):

     def __init__(self, registration):
         super().__init__(registration, "Airbus A319", 22, 6)

class Boeing777(Aircraft):
    
     def __init__(self, registration):
         super().__init__(registration, "Boeing 777", 55, 9)
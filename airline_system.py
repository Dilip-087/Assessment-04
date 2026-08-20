class AirlineReservation:
    def __init__(self, total_seats=50, base_fare=3000):
        self.total_seats = total_seats
        self.booked_seats = set()
        self.base_fare = base_fare

    def calculate_fare(self, seat_class, days_before_flight):
        multiplier = 1.0
        if seat_class.lower() == "business":
            multiplier = 1.8
        elif seat_class.lower() == "first class":
            multiplier = 2.5

        # Dynamic pricing based on remaining capacity and urgency
        load_factor = (len(self.booked_seats) / self.total_seats)
        surge = 1.3 if load_factor > 0.7 or days_before_flight <= 3 else 1.0

        return round(self.base_fare * multiplier * surge, 2)

    def book_seat(self, seat_number, passenger_name, baggage_kg, days_before=10, seat_class="Economy"):
        if seat_number in self.booked_seats:
            raise ValueError("Seat already booked")
        if len(self.booked_seats) >= self.total_seats:
            raise ValueError("Flight fully booked")

        baggage_fee = max(0, baggage_kg - 15) * 400
        fare = self.calculate_fare(seat_class, days_before) + baggage_fee
        self.booked_seats.add(seat_number)

        return {"status": "CONFIRMED", "seat": seat_number, "total_fare": fare}

    def cancel_seat(self, seat_number):
        if seat_number not in self.booked_seats:
            raise ValueError("No booking found for seat")
        self.booked_seats.remove(seat_number)
        return {"status": "CANCELLED", "refund_amount": self.base_fare * 0.6}

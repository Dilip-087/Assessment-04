class ParkingManagement:
    SLOT_MAP = {"Bike": "S", "Car": "M", "SUV": "L", "Truck": "XL", "Electric Vehicle": "EV"}
    HOURLY_RATES = {"Bike": 20, "Car": 40, "SUV": 60, "Truck": 100, "Electric Vehicle": 50}

    def __init__(self):
        self.active_tickets = {}

    def park_vehicle(self, vehicle_number, vehicle_type, is_vip=False):
        if vehicle_type not in self.SLOT_MAP:
            raise ValueError("Unsupported vehicle type")
        if vehicle_number in self.active_tickets:
            raise ValueError("Vehicle already parked")

        slot_type = f"VIP-{self.SLOT_MAP[vehicle_type]}" if is_vip else self.SLOT_MAP[vehicle_type]
        self.active_tickets[vehicle_number] = {"type": vehicle_type, "vip": is_vip, "slot": slot_type}
        return {"status": "PARKED", "vehicle": vehicle_number, "allocated_slot": slot_type}

    def exit_parking(self, vehicle_number, hours_parked, is_peak_hour=False, lost_ticket=False, charge_ev=False):
        if vehicle_number not in self.active_tickets and not lost_ticket:
            raise ValueError("Invalid vehicle exit")

        if lost_ticket:
            return {"fee": 500.0, "note": "Penalty for lost ticket"}

        record = self.active_tickets.pop(vehicle_number)
        rate = self.HOURLY_RATES[record["type"]]
        base_fee = rate * hours_parked

        if is_peak_hour:
            base_fee *= 1.5
        if charge_ev and record["type"] == "Electric Vehicle":
            base_fee += 150.0  # Flat EV Charging fee

        return {"vehicle": vehicle_number, "fee": round(base_fee, 2)}

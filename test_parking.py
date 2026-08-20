import pytest
from parking_system import ParkingManagement

def test_park_vehicle_and_slot_allocation():
    lot = ParkingManagement()
    res = lot.park_vehicle("TN-01-1234", "Car")
    assert res["allocated_slot"] == "M"

def test_duplicate_vehicle_entry():
    lot = ParkingManagement()
    lot.park_vehicle("TN-01-1234", "Car")
    with pytest.raises(ValueError, match="already parked"):
        lot.park_vehicle("TN-01-1234", "Car")

def test_peak_hour_pricing():
    lot = ParkingManagement()
    lot.park_vehicle("TN-02-5678", "Car")
    bill = lot.exit_parking("TN-02-5678", 2, is_peak_hour=True)
    assert bill["fee"] == 120.0  # 40 * 2 * 1.5

def test_lost_ticket():
    lot = ParkingManagement()
    bill = lot.exit_parking("TN-99-9999", 1, lost_ticket=True)
    assert bill["fee"] == 500.0

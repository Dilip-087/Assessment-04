from app.hospital_system import HospitalManagement

def test_emergency_patient_billing():
    res = HospitalManagement.calculate_bill("emergency", "regular", 1000, 500, False)
    assert res["consultation_fee"] == 900
    assert res["patient_payable"] == 2400.0

def test_senior_citizen_with_insurance():
    res = HospitalManagement.calculate_bill("senior citizen", "regular", 200, 300, True)
    assert res["insurance_coverage"] > 0
    assert res["patient_payable"] < 1000

def test_followup_discount():
    res = HospitalManagement.calculate_bill("regular", "follow-up", 0, 0, False)
    assert res["consultation_fee"] == 300

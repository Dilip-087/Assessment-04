class HospitalManagement:
    @staticmethod
    def calculate_bill(patient_type, appointment_type, lab_tests_cost, medicines_cost, has_insurance=False):
        consultation_fee = 300 if appointment_type.lower() == "follow-up" else 500

        if patient_type.lower() == "emergency":
            consultation_fee += 400  # Emergency surcharge

        total_cost = consultation_fee + lab_tests_cost + medicines_cost

        # Senior citizen discount (15% on total)
        if patient_type.lower() == "senior citizen":
            total_cost *= 0.85

        # Insurance coverage calculation
        insurance_coverage = (total_cost * 0.70) if has_insurance else 0.0
        payable_amount = total_cost - insurance_coverage

        return {
            "consultation_fee": consultation_fee,
            "total_cost": round(total_cost, 2),
            "insurance_coverage": round(insurance_coverage, 2),
            "patient_payable": round(payable_amount, 2)
        }

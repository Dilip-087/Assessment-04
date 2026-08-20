class LoanProcessingSystem:
    @staticmethod
    def process_loan(customer_id, age, monthly_salary, existing_loan, credit_score, employment_type, requested_amount, tenure_months):
        # Boundary validation
        if not (21 <= age <= 60):
            return {"status": "REJECTED", "reason": "Age outside eligibility criteria (21-60)"}
        if monthly_salary <= 0:
            raise ValueError("Invalid salary amount")
        if credit_score < 300 or credit_score > 900:
            raise ValueError("Credit score out of range (300-900)")
        if credit_score < 650:
            return {"status": "REJECTED", "reason": "Low credit score"}

        # Debt-to-income (DTI) ratio
        dti = (existing_loan / monthly_salary) * 100
        if dti > 50:
            return {"status": "REJECTED", "reason": "High DTI ratio"}

        # Eligible loan amount
        multiplier = 20 if employment_type.lower() == "salaried" else 15
        eligible_amount = monthly_salary * multiplier
        if requested_amount > eligible_amount:
            return {"status": "REJECTED", "reason": "Requested amount exceeds eligibility limit"}

        # Interest rate and EMI calculation
        rate_annual = 8.5 if credit_score >= 750 else 10.5
        r = (rate_annual / 12) / 100
        emi = (requested_amount * r * ((1 + r) ** tenure_months)) / (((1 + r) ** tenure_months) - 1)

        return {
            "status": "APPROVED",
            "customer_id": customer_id,
            "dti": round(dti, 2),
            "eligible_amount": eligible_amount,
            "interest_rate": rate_annual,
            "emi": round(emi, 2)
        }

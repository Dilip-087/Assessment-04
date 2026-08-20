import pytest
from loan_system import LoanProcessingSystem

def test_successful_loan_approval():
    result = LoanProcessingSystem.process_loan("C01", 30, 50000, 5000, 780, "salaried", 200000, 24)
    assert result["status"] == "APPROVED"
    assert result["interest_rate"] == 8.5

def test_min_max_age_boundary():
    assert LoanProcessingSystem.process_loan("C02", 20, 50000, 0, 750, "salaried", 100000, 12)["status"] == "REJECTED"
    assert LoanProcessingSystem.process_loan("C03", 65, 50000, 0, 750, "salaried", 100000, 12)["status"] == "REJECTED"

def test_invalid_salary_exception():
    with pytest.raises(ValueError):
        LoanProcessingSystem.process_loan("C04", 30, -5000, 0, 750, "salaried", 100000, 12)

def test_poor_credit_score():
    result = LoanProcessingSystem.process_loan("C05", 35, 60000, 0, 550, "salaried", 100000, 12)
    assert result["status"] == "REJECTED"
    assert result["reason"] == "Low credit score"

def test_high_dti_ratio():
    result = LoanProcessingSystem.process_loan("C06", 35, 40000, 25000, 750, "salaried", 100000, 12)
    assert result["status"] == "REJECTED"

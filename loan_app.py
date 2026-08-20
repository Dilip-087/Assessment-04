from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <title>Loan Approval System</title>
</head>
<body>
  <h2>Banking Loan Approval System</h2>
  <form method="POST" action="/check_loan">
    <label>Age:</label>
    <input type="number" id="age" name="age" required><br><br>
    
    <label>Salary:</label>
    <input type="number" id="salary" name="salary" required><br><br>
    
    <label>Credit Score:</label>
    <input type="number" id="credit_score" name="credit_score" required><br><br>
    
    <label>Existing Loan:</label>
    <input type="number" id="existing_loan" name="existing_loan" required><br><br>
    
    <label>Requested Amount:</label>
    <input type="number" id="requested_amount" name="requested_amount" required><br><br>
    
    <button type="submit" id="submit_btn">Evaluate Application</button>
  </form>

  {% if result %}
    <h3 id="result_status">{{ result }}</h3>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/check_loan", methods=["POST"])
def check_loan():
    age = int(request.form.get("age", 0))
    salary = float(request.form.get("salary", 0))
    credit_score = int(request.form.get("credit_score", 0))
    existing_loan = float(request.form.get("existing_loan", 0))
    requested_amount = float(request.form.get("requested_amount", 0))

    if not (21 <= age <= 60):
        result = "REJECTED: Age not eligible"
    elif credit_score < 650:
        result = "REJECTED: Low credit score"
    elif (existing_loan / salary) * 100 > 50:
        result = "REJECTED: High DTI ratio"
    elif requested_amount > (salary * 20):
        result = "REJECTED: Exceeds eligible loan limit"
    else:
        result = "APPROVED: Loan Approved"

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(port=5000)

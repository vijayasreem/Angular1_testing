@app.route('/validate_policy', methods=['POST'])
def validate_policy():
    request_data = request.get_json()
    min_sum_assured = request_data['minSumAssured']
    max_sum_assured = request_data['maxSumAssured']
    min_age = request_data['minAge']
    max_age = request_data['maxAge']
    annual_income = request_data['annualIncome']
    sum_assured_options = request_data['sumAssuredOptions']
    policy_tenure_options = request_data['policyTenureOptions']
    otp_authentication = request_data['otpAuthentication']

    if (annual_income < 40000):
        return jsonify({
            "success": False,
            "message": "Insurance coverage not provided for members whose annual income is less than 40K"
        })

    if (min_sum_assured == None or max_sum_assured == None or min_age == None or max_age == None):
        return jsonify({
            "success": False,
            "message": "Minimum and maximum sum assured, minimum and maximum age limits are required"
        })

    if (sum_assured_options == None or policy_tenure_options == None):
        return jsonify({
            "success": False,
            "message": "Sum assured and policy tenure options must be provided"
        })

    if (otp_authentication == False):
        return jsonify({
            "success": False,
            "message": "Insurance coverage not provided as OTP authentication is not received"
        })

    return jsonify({
        "success": True,
        "message": "Eligibility criteria validated successfully"
    })
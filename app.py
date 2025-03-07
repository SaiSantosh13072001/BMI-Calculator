from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_bmi(weight, feet, inches):
    height_in_inches = (feet * 12) + inches
    bmi = (weight * 2.20462 * 703) / (height_in_inches ** 2)
    return round(bmi, 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi <= 24.9:
        return "normal weight"
    elif bmi < 29.9:
        return "overweight"
    elif bmi < 34.9:
        return "obese"
    elif bmi < 39.9:
        return "severely obese"
    else:
        return "morbidly obese"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    category = None
    error = None
    bmi = None
    name = request.form['name']
    weight = float(request.form['weight'])
    feet = float(request.form['feet'])
    inches = float(request.form['inches'])
    if(inches < 0 or inches >= 12):
        error = "Invalid input detected: Inches should be greater than or equal to 0 and less than 12."
    if(weight < 0):
        error = "Invalid input detected: Weight should be greater than 0."
    if(feet < 0 or feet >= 9):
        error = "Invalid input detected: Feet should be greater than 0 and less than 9."
        
    if(error is not None):
        return jsonify({'name': name, 'bmi': bmi, 'category': category, 'error': error})
         
    bmi = calculate_bmi(weight, feet, inches)
    category = get_bmi_category(bmi)
        
    return jsonify({'name': name, 'bmi': bmi, 'category': category, 'error': error})

if __name__ == '__main__':
    app.run(debug=True)

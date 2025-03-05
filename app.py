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
    try:
        name = request.form['name']
        weight = float(request.form['weight'])
        feet = float(request.form['feet'])
        inches = float(request.form['inches'])
        
        bmi = calculate_bmi(weight, feet, inches)
        category = get_bmi_category(bmi)
        
        return jsonify({'name': name, 'bmi': bmi, 'category': category})
    except ValueError:
        return jsonify({'error': 'Invalid input!'}), 400

if __name__ == '__main__':
    app.run(debug=True)

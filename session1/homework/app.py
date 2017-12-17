from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/aboutme')
def aboutme():
    Info = {
        "Name": "Minh Anh",
        "Work": "Estatopia Property",
        "Hobbies": "Eating",
        "Dog": "Tu",
        "Crush": "Nayeon Twice"
    }
    return render_template('aboutme.html', Info = Info)

@app.route('/school')
def school():
    return redirect('http://techkids.vn/')

@app.route('/bmi/<weight>/<height>')
def bmi(weight,height):
    BMI = int(weight)/(float(height))**2
    bmi = str(BMI)
    if BMI < 16:
        return bmi + "severely Underweight"
    elif BMI <18.5:
        return bmi + "Underweight"
    elif BMI < 25:
        return bmi + "Normal"
    elif BMI <30:
        return bmi + "Overweight"
    else:
        return bmi + "Obese"
if __name__ == '__main__':
  app.run(debug=True)

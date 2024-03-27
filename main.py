from flask import Flask, render_template
import database
import db_of_patient

app = Flask(__name__)

@app.route('/')
def home():
    # Connect to the database
    db = database.connect()
    patients = db_of_patient.get_all(db)

    # Render the index.html template
    return render_template('index.html', patients=patients)

@app.route('/appointment')
def appointment():
    # Connect to the database
    db = database.connect()
    patients = db_of_patient.get_all(db)

    # Render the patient.html template
    return render_template('patient.html', patients=patients)

if __name__ == '__main__':
    app.run(debug=True)

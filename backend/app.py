from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this in production

# Mock data for demonstration
patient_records = [
    {"id": "P001", "name": "Ramesh Kumar", "age": 45, "last_visit": "12 March 2025", "status": "Active"},
    {"id": "P002", "name": "Sita Devi", "age": 38, "last_visit": "09 March 2025", "status": "Active"}
]

health_camps = [
    {"id": 1, "name": "Camp at Village X", "date": "20 April 2025", "location": "Village X Community Center"},
    {"id": 2, "name": "Camp at Village Y", "date": "25 April 2025", "location": "Village Y School"}
]

# Mock admin credentials
ADMIN_EMAIL = "admin@health.gov"
ADMIN_PASSWORD = "admin123"

# Routes
@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/aadhar-access')
def aadhar_access():
    return render_template('aadhar_access.html')

@app.route('/ayushman-check')
def ayushman_check():
    return render_template('ayushman_check.html')

@app.route('/nearby-hospitals')
def nearby_hospitals():
    return render_template('nearby_hospitals.html')

@app.route('/voice-assistant')
def voice_assistant():
    return render_template('voice_assistant.html')

# Patient routes
@app.route('/patient/login', methods=['GET', 'POST'])
def patient_login():
    if request.method == 'POST':
        # Simple login logic
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Mock validation
        if username == 'patient' and password == 'password':
            session['patient_logged_in'] = True
            return redirect(url_for('landing_page'))
        else:
            flash('Invalid username or password', 'error')
            
    return render_template('patient_login.html')

@app.route('/patient/register', methods=['GET', 'POST'])
def patient_register():
    if request.method == 'POST':
        # Registration logic would go here
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('patient_login'))
    
    return render_template('patient_register.html')

@app.route('/patient/details', methods=['GET', 'POST'])
def patient_details():
    if request.method == 'POST':
        # Save patient details logic would go here
        flash('Patient details saved successfully!', 'success')
        return redirect(url_for('landing_page'))
    
    return render_template('patient_details.html')

# Admin/Doctor routes
@app.route('/doctor-login', methods=['GET', 'POST'])
def doctor_login():
    if request.method == 'POST':
        email = request.form.get('adminEmail')
        password = request.form.get('adminPassword')
        
        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('doctor_login.html')

@app.route('/admin-dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('doctor_login'))
    
    return render_template('admin_dashboard.html', 
                          patient_records=patient_records,
                          health_camps=health_camps,
                          total_patients=1250,
                          active_camps=8,
                          pending_approvals=15)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('landing_page'))

if __name__ == '__main__':
    app.run(debug=True)
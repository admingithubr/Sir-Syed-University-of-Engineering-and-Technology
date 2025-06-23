from flask import Flask, render_template, request, redirect, url_for, flash, session
from data_manager import load_data, save_data
import os

app = Flask(__name__)
app.secret_key = 'cms_secret'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student/login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        sid = request.form['sid']
        pw = request.form['password']
        students = load_data('students.pkl')
        if sid in students and students[sid].get('password') == pw:
            session['student_id'] = sid
            return redirect(url_for('student_dashboard'))
        flash("Invalid student credentials.")
    return render_template('student_login.html')

@app.route('/student/dashboard')
def student_dashboard():
    sid = session.get('student_id')
    if not sid:
        return redirect(url_for('student_login'))
    students = load_data('students.pkl')
    results = load_data('results.pkl')
    attendance = load_data('attendance.pkl')
    transcripts = load_data('transcripts.pkl')
    return render_template('student_dashboard.html',
                           student=students[sid],
                           result=results.get(sid, "N/A"),
                           attendance=attendance.get(sid, "N/A"),
                           transcript=transcripts.get(sid, "N/A"))

@app.route('/teacher/login', methods=['GET', 'POST'])
def teacher_login():
    if request.method == 'POST':
        tid = request.form['tid']
        pw = request.form['password']
        teachers = load_data('teachers.pkl')
        if tid in teachers and teachers[tid].get('password') == pw:
            session['teacher_id'] = tid
            return redirect(url_for('teacher_dashboard'))
        flash("Invalid teacher credentials.")
    return render_template('teacher_login.html')

@app.route('/teacher/dashboard', methods=['GET', 'POST'])
def teacher_dashboard():
    tid = session.get('teacher_id')
    if not tid:
        return redirect(url_for('teacher_login'))
    
    if request.method == 'POST':
        sid = request.form['sid']
        field = request.form['field']
        value = request.form['value']
        filename = 'results.pkl' if field == 'result' else 'attendance.pkl'
        data = load_data(filename)
        data[sid] = value
        save_data(data, filename)
        flash(f"{field.capitalize()} updated for student {sid}")
        
    return render_template('teacher_dashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    os.makedirs('database', exist_ok=True)
    app.run(debug=True)

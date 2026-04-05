from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "event_secret_key"

# Task 2: Sample event data passed to Jinja2 templates 
events_list = [
    {"id": 1, "name": "Global Tech Summit", "date": "2026-05-15 | 10:00 AM", "venue": "Convention Center", "desc": "Exploring AI and Robotics."},
    {"id": 2, "name": "Jazz Under the Stars", "date": "2026-06-20 | 07:00 PM", "venue": "City Park", "desc": "An evening of live jazz music."},
    {"id": 3, "name": "Startup Pitch Day", "date": "2026-07-10 | 09:00 AM", "venue": "Innovation Hub", "desc": "New ventures pitching to investors."},
    {"id": 4, "name": "Photography Workshop", "date": "2026-08-05 | 11:00 AM", "venue": "Studio 42", "desc": "Mastering DSLR manual settings."}
]

@app.route('/')
def index():
    # Task 1: Styled landing page [cite: 21]
    return render_template('index.html')

@app.route('/events')
def events():
    # Task 2: Display list of events 
    return render_template('events.html', events=events_list)

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Task 4: Handling registration form submission [cite: 24]
    if request.method == 'POST':
        flash("Registration successful! We will contact you soon.")
        return redirect(url_for('events'))
    return render_template('register.html', events=events_list)

@app.route('/admin')
def admin():
    # Task 5: Admin panel for managing events [cite: 25]
    return render_template('admin.html', events=events_list)

if __name__ == '__main__':
    app.run(debug=True) # Task 1: Debug mode enabled [cite: 21]

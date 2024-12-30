from flask import render_template
from app import app
from app.models import Event

@app.route('/')
def home():
    events = Event.query.all()
    return render_template('index.html', events=events)
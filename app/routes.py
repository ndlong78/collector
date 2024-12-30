from flask import render_template, jsonify
from app import app
from app.models import Event
import logging

@app.route('/')
def home():
    logging.info("Accessing home route")
    events = Event.query.all()
    logging.info("Fetched %d events from database", len(events))
    return render_template('index.html', events=events)

@app.route('/events')
def get_events():
    logging.info("Accessing events route")
    events = Event.query.all()
    events_data = [
        {
            "date": event.date.strftime('%Y-%m-%d'),
            "description": event.description
        } for event in events
    ]
    logging.info("Returning %d events", len(events_data))
    return jsonify(events_data)
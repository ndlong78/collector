import requests
from bs4 import BeautifulSoup
from app import db, app  # Import app từ app/__init__.py
from app.models import Event
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

def fetch_data(url):
    logging.info("Fetching data from URL: %s", url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []
    
    # Cập nhật phần này dựa trên cấu trúc HTML mới của trang web
    events = soup.find_all('div', class_='event')
    for event in events:
        date = event.find('span', class_='date').text
        description = event.find('span', class_='description').text
        data.append({'date': date, 'description': description})
    logging.info("Fetched %d events", len(data))
    return data

def save_data(data):
    with app.app_context():
        for item in data:
            date = datetime.strptime(item['date'], '%Y-%m-%d').date()
            event = Event(date=date, description=item['description'])
            db.session.add(event)
        db.session.commit()
        logging.info("Saved %d events to the database", len(data))
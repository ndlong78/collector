import requests
from bs4 import BeautifulSoup
from app import db
from app.models import Event
from datetime import datetime

def fetch_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []
    events = soup.find_all('div', class_='event')
    for event in events:
        date = event.find('span', class_='date').text
        description = event.find('span', class_='description').text
        data.append({'date': date, 'description': description})
    return data

def save_data(data):
    for item in data:
        date = datetime.strptime(item['date'], '%Y-%m-%d').date()
        event = Event(date=date, description=item['description'])
        db.session.add(event)
    db.session.commit()
    print(f"Saved {len(data)} events to the database")

url = 'https://www.thoigian.com.vn/'
data = fetch_data(url)
save_data(data)
from app import app, db
from app.collector import fetch_data, save_data

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        url = 'https://www.thoigian.com.vn/'
        data = fetch_data(url)
        save_data(data)
    app.run(debug=True, port=8088)  # Thay đổi cổng sang 8088
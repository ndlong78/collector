from app import app, db
from app.collector import fetch_data, save_data
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        url = 'https://www.thoigian.com.vn/'
        logging.info("Fetching data from URL: %s", url)
        data = fetch_data(url)
        logging.info("Saving data to database")
        save_data(data)
    logging.info("Starting Flask app on port 8088")
    app.run(debug=True, host='0.0.0.0', port=8088)  # Lắng nghe trên tất cả các địa chỉ IP
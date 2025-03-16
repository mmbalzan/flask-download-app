import logging
from flask import Flask, render_template, send_file, request
from datetime import datetime

# Set up logging
logging.basicConfig(filename="access.log", level=logging.INFO)

app = Flask(__name__, template_folder="templates")


@app.route('/')
def home():
    visitor_ip = request.remote_addr  # Get user IP
    visit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log visit
    logging.info(f"Home page visited from {visitor_ip} at {visit_time}")

    return render_template('index.html')


@app.route('/download')
def download_file():
    visitor_ip = request.remote_addr  # Get user IP
    download_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log download event
    logging.info(f"File downloaded from {visitor_ip} at {download_time}")

    return send_file("file.pdf", as_attachment=True, download_name="ReadMe.pdf")


if __name__ == '__main__':
    app.run(debug=True)
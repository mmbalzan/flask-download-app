from flask import Flask, render_template, send_file

app = Flask(__name__, template_folder='templates')  # Ensure Flask looks in 'templates/'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def download_file():
    return send_file("file.pdf", as_attachment=True, download_name="ReadMe.pdf")

if __name__ == '__main__':
    app.run(debug=True)
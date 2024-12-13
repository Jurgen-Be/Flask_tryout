# Import modules
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>Huiswerk opgave 4 in txt file<p>"

# Hoofdprogramma
if __name__ == "__main__":
    app.run(port=5000, debug=True)
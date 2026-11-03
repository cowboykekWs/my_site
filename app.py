from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Мой сайт</title>
    </head>
    <body>
        <h1>Привет!</h1>
        <p>Это мой первый сайт на Python.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
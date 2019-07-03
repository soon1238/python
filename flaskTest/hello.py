from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Simple web server using flask!"

if __name__ == "__main__":
    app.run()
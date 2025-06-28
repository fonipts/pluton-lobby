from flask import Flask


#noqa: create the app
app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>Hello world</p>"
@app.route("/heath")
def health():
    return "<p>Server is running</p>"

if __name__ == "__main__":
  app.run()

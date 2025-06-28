from flask import Flask

from .views.simple_page import simple_page


#noqa: create the app
app = Flask(__name__)

app.register_blueprint(simple_page)

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"
@app.route("/heath")
def health():
    return "<p>Server is running</p>"

if __name__ == "__main__":
  app.run()

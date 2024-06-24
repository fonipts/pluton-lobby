from flask import Flask
({   
    @condition{
        database != "none"
    }
    @content{
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy.orm import declarative_base,sessionmaker
    from decouple import config
    from urllib.parse import quote_plus

    }
    @end{}
    @content{
    

    }
})
#noqa: create the app
app = Flask(__name__)
({   
    @condition{
        database == "postgres"
    }
    @content{
    db = SQLAlchemy()
    app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql+psycopg://{config("DB_USER")}:{quote_plus(config("DB_PASSWORD"))}@{config("DB_CONNECTION")}/{config("DB_NAME")}'
    db.init_app(app)

    }
    @end{}
    @condition{
        database == "mysql"
    }
    @content{
    db = SQLAlchemy()
    app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{config("DB_USER")}:{quote_plus(config("DB_PASSWORD"))}@{config("DB_CONNECTION")}/{config("DB_NAME")}'
    db.init_app(app)

    }
})
@app.route("/heath")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
  app.run()

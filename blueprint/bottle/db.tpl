({   
    
    @content{
    from decouple import config
    from sqlalchemy import create_engine
    from sqlalchemy.orm import declarative_base,sessionmaker
    from urllib.parse import quote_plus

    }
})


({   
    @condition{
        $choices.database == "postgres"
    }
    @content{
    engine = create_engine(f'postgresql+psycopg://{config("DB_USER")}:{quote_plus(config("DB_PASSWORD"))}@{config("DB_CONNECTION")}/{config("DB_NAME")}')
    conn = engine.connect()
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()

    }
    @end{}
    @condition{
        $choices.database == "mysql"
    }
    @content{
    engine = create_engine(f'mysql://{config("DB_USER")}:{quote_plus(config("DB_PASSWORD"))}@{config("DB_CONNECTION")}/{config("DB_NAME")}')
    conn = engine.connect()
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()

    }
})


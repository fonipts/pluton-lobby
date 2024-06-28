# Functional syntax

## Sample syntax

In a browser :
```html
({   
    @condition{
        database == "postgres"
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
        database == "mysql"
    }
    @content{
    engine = create_engine(f'mysql://{config("DB_USER")}:{quote_plus(config("DB_PASSWORD"))}@{config("DB_CONNECTION")}/{config("DB_NAME")}')
    conn = engine.connect()
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()

    }
})

```

### Group action in yaml architecture

|Action type | Description | Status |
|----------- | ----------- |--------- |
|condition | Project name | Dev |
|end       | Project name | Dev |
|content   | Project name | Dev |
|load      | Project name | Pending |



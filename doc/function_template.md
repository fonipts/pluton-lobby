# Functional syntax

## Introduction
The goal is to have an idea in building function in template and reuse to if you import to different project.

Most of pass value are coming from `choices` at `architecture.yaml`
## Sample syntax
This function syntax will work on `*.tpl{ext file}` otherwise it will be ignore in execution.

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
|condition | creating your conditional statement | Dev |
|end       | Else statement in the template | Dev |
|content   | Content of template function that you want to render | Dev |
|load      | Load/import the *.tpl{file extension} file | Pending |

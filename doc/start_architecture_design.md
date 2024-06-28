# Structuring your template

## How to import the Library

In a browser :
```html
name: bottle
choices:
  - name: name
    question: What is your name
    type: input
  - name: database
    question: What is your Database choice?
    type: single_choice
    option:
      - postgres
      - mysql
      - none
  - name: redis
    question: Do you want Redis?
    type: single_choice
    option:
      - "yes"
      - "no"
  - name: docker
    question: Do you want Dockerfile?
    type: single_choice
    option:
      - "yes"
      - "no"
dependencies:
  default:
  - bottle==0.12.25
  optional:
    - condition: database == "postgres"
      dependent:
      - SQLAlchemy==2.0.23
      - psycopg[binary,pool]==3.1.14
    - condition: database == "mysql"
      dependent:
      - SQLAlchemy==2.0.23
      - PyMySQL==1.1.0
    - condition: redis == "yes"
      dependent:
      - redis==5.0.4
script:
  pip_install:
    description: Install package
    command:
    - pip install -r requirements.txt
  start:
    command:
    - python main.py
files:
  default:
    - file: main.tpl
    - file: __init__.tpl
    - file: README.md
  optional:
    - condition: database != "none"
      dependent:
      - file: db.tpl
    - condition: docker == "yes"
      dependent:
      - file: Dockerfile

```
### Group action in yaml architecture

|Action type | Description |
|------------- | ------------- |
|name | Project name |
|choices | Executing command using plutonkit |
|dependencies | Installing packages and to save at requirements.txt |
|script | command argument that to be save at command.yaml |
|files | List of files that you will copy in project directory |



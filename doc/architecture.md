# Architecture

## What is architecture
It is a set of guidelines that you want or how your project template will function base on our needs in the application, with the help of `architecture.yaml` you define the characteristics of your application before starting for your upcomming project.

## Sample of code in yaml for setting in architecture.yaml

In a browser :
```html
name: bottle
settings:
  install_type: pip
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
      - "No plan"
      - "python"
      - "nginx"
      - "apache2"
dependencies:
  default:
  - bottle==0.12.25
  optional:
    - condition: database == "postgres"
      dependent:
      - SQLAlchemy==2.0.23
      - psycopg[binary,pool]==3.1.14
      - psycopg2-binary==2.9.9
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
    - file: main.tplpy
    - file: __init__.tplpy
    - file: README.md
  optional:
    - condition: database != "none"
      dependent:
      - file: db.tplpy
    - condition: docker != "No plan"
      dependent:
      - file: Dockerfile.tpl

bootscript:
  - command: pip install -r requirements.txt
    exec_position: start


```
### Action in yaml architecture

|Action type | Description |
|------------- | ------------- |
|name | Project name |
|settings | Project setting details |
|choices | Executing command using plutonkit |
|dependencies | Installing packages and to save at requirements.txt |
|script | command argument that to be save at command.yaml |
|files | List of files that you will copy in project directory |
|bootscript | Script you want to run before and after was created |

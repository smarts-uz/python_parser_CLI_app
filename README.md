# Parser CLI app

## Quick Start

https://github.com/smarts-uz/python_parser_CLI_app/assets/117033000/7ece9fd3-27a2-4f7a-9072-423f5978bf51


Also check video [explanation](https://t.me/c/1608280866/742?thread=567):
```python
git clone https://github.com/smarts-uz/python_parser_CLI_app
```
 Firstly create venv 
 ```python
py -m venv venv
```
 Then install requirements
```python
pip install -r requirements.txt
```
be sure you have .env file with it credentials

First step

```python
py main.py parsing
```

Second step

```python
py main.py update-db-content
```


Third step

```python
py main.py create-folders
```


## How to change db
change .env credentials
then move to django_orm/settings.py file
Comment line 54
```python
#INSTALLED_APPS = ("django_orm.db",)
```
and uncomment line 55
```python
INSTALLED_APPS = ("db",)
```

then delete this file django_orm/db/migrations/0001_initial.py
after this do this
```python
python manage.py makemigrations
python manage.py migrate
```
Congrats you have change the db

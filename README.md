# Parser CLI app

## Quick Start



Also check video [explanation](https://t.me/c/1608280866/742?thread=567):


https://github.com/smarts-uz/python_parser_CLI_app/assets/117033000/74e9e009-4cd3-4c9c-9181-2f7e21d1dcbf


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

## Collector
Collector command collects all html files folders and runs execute command
```python
py main.py collector --path=file_path --name=channel_name
```


Example:  "py main.py collector --path="h:\Exports\SmartTech Learning Group" --name="SmartTech Learning"




## Execute
Execute command checks execution's status and runs parsing or file copy commands 
```python
py main.py execute --ex_id=execution_id
```
Example: "py main.py execute --ex_id=475"


## Parsing

The parsing command parses all html files that starts with messages
```python
py main.py parsing --ex_id=execution_id
```

Example: "py main.py parsing --ex_id=475"

## File-Copy

The file-copy command copies files from base dir to path_to_save which given from .env  
```python
py main.py file-copy --ex_id=execution_id
```




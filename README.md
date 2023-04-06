Skypro Homework
==
Lesson 24. Typing and additional topics.
-
___
**In this project:** 

A flask-based web server was made which "replicates" the Linux command line functionality for file processing 
(cat otherfile | grep 'something'):
1. Available at the path _"/perform_query"_
2. Accepts 5 parameters: where 1, 2, 3, 4 - query, 5th - file name 
_Example_: {
  'file_name': 'apache_logs.txt',
  'cmd1': 'filter',
  'value1': 'GET',
  'cmd2': 'map',
  'value2': '0',
}
3. Query contains several commands: filter, map, unique, sort, limit, regex
4. Only 2 commands are always executed


**Skills practiced with:** 

1. Use of functional programming
2. Writing lambda functions
3. Using List Comprehensions
4. Project typing (typing framework)
___
**How to start a project:**

1. Clone a project from GiHub into your own project
2. Create a virtual environment (venv)
3. Install all files from requirements.txt
4. Check location of all files
5. Run file "app.py" (Run app.py) or open file app.py and press key combination "control" + "R" (macOS)
___
_created by [morinch](https://github.com/mor1nch)_

# python_examples

gpa.py is a python script to parse json format grades inputs into GPA into csv format

* __note__ Tested on python 2.7, python 3.0

### execution through online Python compiler
* open Online Python compiler (i.e https://repl.it/languages/python3) in web browser
* click `+new repl` to import from GitHub https://github.com/qxconsultant/python_examples.git
* from console, 
 * check imported files list via `ls -l`
 * check Git branch via `git branch -a`
 * switch to feature/new_csv branch via `git checkout -b feature/new_csv origini/feature/new_csv`
 * update gpa.json input file via `vi gpa.json`
 * execute `python gpa.py`, generates gps.csv
 * check the content of gpa.csv via `cat gpa.csv`

example of CSV to Markdown

|Term       |Course    |Credit|Grade|TERM GPA|CUM GPA|
|-----------|----------|------|-----|--------|-------|
|FALL 2017  | BIOL200  | 3    | B+  |        |       |
|FALL 2017  | MATH203  | 3    | B+  |        |       |
|FALL 2017  | MIMM211  | 3    | B   |        |       |
|FALL 2017  | MIMM212  | 3    | A   |        |       |
|FALL 2017  |          |      |     | 3.4    |       |
|WINTER 2018| CHEM181  | 3    | A   |        |       |
|WINTER 2018|          |      |     | 4.0    |       |
|FALL 2018  | BIOL300  | 3    | B   |        |       |
|FALL 2018  | BIOL306  | 3    | B   |        |       |
|FALL 2018  | ESAT204D1| 4.5  | A-  |        |       |
|FALL 2018  |          |      |     | 3.3    |       |
|WINTER 2019| BIOL201  | 3    | B+  |        |       |
|WINTER 2019| BIOL303  | 3    | B-  |        |       |
|WINTER 2019| BIOL313  | 3    | B+  |        |       |
|WINTER 2019| ESAT204D2| 4.5  | A-  |        |       |
|WINTER 2019|          |      |     | 3.3    |       |
|SUMMER 2019| BIOL202  | 3    | C+  |        |       |
|SUMMER 2019|          |      |     | 2.3    |       |
|           |          |      |     |        | 3.31  |

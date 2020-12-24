### How to Start Python and Jupyter if Doesn't recognized in Terminal?

Problem is pathing. It doesn't registered in your terminal.

``` zsh
# this is to redirect your current working directory to python folder
cd "C:\Users\Dhruvin Gandhi\AppData\Local\Programs\Python\Python39"

# this is python executable
python.exe -- version

python.exe -m pip list

python.exe -m pip install jupyter

# redirect current working directory to where jupyter is installed
cd "C:\Users\Dhruvin Gandhi\AppData\Local\Programs\Python\Python39\Scripts"

# start the notebook in assignment folder
jupyter.exe notebook "C:\Users\Dhruvin Gandhi\OneDrive\Documents\GitHub\assignment-1-dgandhi4"
```

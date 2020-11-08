# Week 2

We will go over on IDEs, creating environments, having multiple versions, of python, test driven development, debugging python code, continous integration tools, and much much more.

### Installing Python

- [ ] Install python to your computer.

- [From python downloads](https://www.python.org/downloads/)
- [Pyenv](https://github.com/pyenv/pyenv)
- [Pyenv for Windows](https://github.com/pyenv-win/pyenv-win)
- [Command line tool to manage multiple runtimes, not only Python](https://asdf-vm.com/#/)
- [Covers a lot of things about shells, emulators, python version management, python environments, package managers](https://realpython.com/effective-python-environment/)

### Multiple Python Versions

#### Why not the system python?

Some operating systems have python already. In Linux or OSX, typing `python` into console will bring you to python2 REPL. 

- Since python2 is out of support by Python Community, using python2 is discouraged.
- System python could be customized by the provider.
- Since some system application might be using it, it is not a good practice to mess up with this python interpreter.

#### Why to have multiple versions?

- If you work on multiple projects, each project might have a different version and to run those projects, you need seperate versions.
- You may develop a package, where you want to target multiple versions of python.
- You may want to test a feature that is available on the latest version of python.
- Many other python distros ([Anaconda](https://www.anaconda.com/products/individual), and [others](https://www.python.org/download/alternatives/)) also adopts convention of installing different version of python.
- 
### IDEs

Various text editors you can code. Some of them features great tools for coding!

#### IDLE

Python's default code editor. [IDLE](https://docs.python.org/3/library/idle.html) is Python’s Integrated Development and Learning Environment.

#### JupyterHub

- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/en/stable/)

#### Jupyter Notebook 

- [Notebook](https://jupyter-notebook.readthedocs.io/en/stable/) a representation of all content visible in the web application, including inputs and outputs of the computations, explanatory text, mathematics, images, and rich media representations of objects.
  
#### VSCode

- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- Great for development, enterprise grade tools!
- Many useful extensions available, such as 
  - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf), etc.
  - [Live Code](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) to interact with each other.

#### Interactive Shells

- [A powerful interactive shell, iPython](https://ipython.org/)
- [Python Shell](https://www.python.org/shell/)

### Environments

<!-- TODO -->

### Test Driven Development (TTD)

![test driven development](assets/tdd-red-green-refactoring-v3.png)

[Test Driven Development ](https://en.wikipedia.org/wiki/Test-driven_development) is a softwrare development process of designing the code in a way that will let you write very specific test cases. With test cases on hand, you will tweak the code so that your tests passes and you will build a test-proof code.

1. Read, understand, and process the feature or bug request.
2. Translate the requirement by writing a unit test. If you have hot reloading set up, the unit test will run and fail as no code is implemented yet.
3. Write and implement the code that fulfills the requirement. Run all tests and they should pass, if not repeat this step.
4. Clean up your code by refactoring.
5. Rinse, lather and repeat.

#### Why not to use TDD in Data Science?

- When you do data exploration
- Simple implementation of some strait ideas
- You may be the only one working on a project and you think it won't be used by no one else but you.

### When to use TDD in Data Science?

- When building data pipelines
- Complicated project with multiple levels, clean data, etc.
- You work in a team that other people are also using the same code.

**Example 1**

One example from [Timo Böhm](https://medium.com/@timoboehm) in his article on [How to use Test Driven Development in a Data Science Workflow](https://towardsdatascience.com/tdd-datascience-689c98492fcc) is analysis of tweets. He divides this task into four subproblems:

1. Clean tweets from mentions of other accounts.
2. Filter out retweets.
3. Clean special characters from the tweets.
4. Filter out empty strings.

Looking at these sub problems, one has to write multiple functions and orchastre these in order to achieve a clean dataset. However, a problem can occur in any of these steps that will will waste a lot of your time.

What to do, as Timo did, write test functions to proof your cleanup code so that you make sure some parts of your code actually work.

**Example 2**

[Step-by-step TDD in a data science task](https://nbviewer.jupyter.org/github/agostontorok/tdd_data_analysis/blob/master/TDD%20in%20data%20analysis%20-%20Step-by-step%20tutorial.ipynb#Step-by-step-TDD-in-a-data-science-task).


**Example 3**

You are building an ETL pipeline, where you have to make sure the custom functions you built should work as expected. You maybe doing a lot of table operations, which requires sort of confirmation method so that your code can be future-proof.

<sub>Image source is from an [article](https://developer.ibm.com/articles/5-steps-of-test-driven-development/) at IBM Developer.</sub>

### Debuging Python Code

A debugger or debugging tool is a computer program used to test and debug other programs. The main use of a debugger is to run the target program under controlled conditions that permit the programmer to track its operations in progress and monitor changes in computer resources that may indicate malfunctioning code. [Wikipedia](https://en.wikipedia.org/wiki/Debugger)

- [The Python Debugger](https://docs.python.org/3/library/pdb.html)

``` py
import pdb; pdb.set_trace()
```

- [Configure and run the debugger](https://code.visualstudio.com/docs/python/debugging)

``` js
{
    "name": "Python: Current File (Integrated Terminal)",
    "type": "python",
    "request": "launch",
    "program": "${file}",
    "console": "integratedTerminal"
}
```

- [IPython pdb](https://github.com/gotcha/ipdb) debugger.
``` py
import ipdb
ipdb.set_trace(context=5)  # will show five lines of code
                           # instead of the default three lines
                           # or you can set it via IPDB_CONTEXT_SIZE env variable
                           # or setup.cfg file
```
### CI

<!-- TODO -->

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

<!-- TODO -->
<!-- Explain why multiple versions are useful, how to install, etc. -->

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
  - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), 
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), 
  - [Markdown PDF],(https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf), etc.

#### Interactive Shells

- [A powerful interactive shell, iPython](https://ipython.org/)
- [Python Shell](https://www.python.org/shell/)

### Environments

<!-- TODO -->

### Test Driven Development

<!-- TODO -->

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

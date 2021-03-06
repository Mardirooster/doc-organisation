# doc-organisation


## Installation instructions:


### Requirements:

- [Python 3, pip](https://www.python.org/downloads/release/python-361/)

- virtualenv: `pip install virtualenv`

- [Visual C++ Build Tools](http://landinghub.visualstudio.com/visual-cpp-build-tools).


### Installation (Windows):

- Clone this repository:
```
> git clone https://github.com/Mardirooster/doc-organisation.git
```
- Set up virtualenv:
```
> virtualenv env
> .\env\Scripts\activate
> pip install -r requirements.txt
```

- Install [numpy+mkl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy) and [scipy](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy), in that order. Download the linked .whl packages to install directory and run `pip install [package-name]`. 

- Install other requirements:

```
> pip install -r requirements.txt 
```

- Run `python main.py [--arguments]`
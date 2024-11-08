# PyBrowser 🌎

A basic web browser made with Python. Using the PyQt5 and PyWebEngine libraries.

## Before anything else! ⚠️

Beacuase of the size of the PyWebEngine library this time before executing the program we need to create a **Virtual Environment**.

To create a python virtual environment and install the dependencies, inside the project's main folder follow these steps.

```
Linux/MacOS:

# Create the virtual environmernt
python -m venv browser

# Activate the virtual envronment
source browser/bin/activate

# Install the dependencies
pip PyQt5
pip install PyQtWebEngine
```

```
Windows:

# Create the virtual environmernt
python -m venv browser

# Activate the virtual envronment
browser\Scripts\activate

# Install the dependencies
pip PyQt5
pip install PyQtWebEngine
```

Now that we have all up to date, just execute the program.

`python main.py`

## How to use it? 🤔

Like any other web browser, simply type in the main search bar or URL bar to visit the site you want.

![img](screenshots/img01.png)

The browser also allows you to go back, move forward, return to the main page (which defaults to DuckDuckGo), and reload the current web page.

By default, the controls are located at the bottom of the app, but you can manually move and place them on other sides of the app if you prefer.

![img](screenshots/img02.png)

![img](screenshots/img03.png)

![img](screenshots/img04.png)


### Important ⚠️

This browser was made just for fun and learning purposes. It is not meant to be a fully functional browser, so I do not recommend using it as your main browser due to potential security issues and compatibility limitations with some websites.

## Free Usage 🆓

I made this basic program with educational purpouses.

I relied to [Python Geeks](https://pythongeeks.org/create-web-browser-python-pyqt/) and [Programming Hero](https://youtu.be/z-5bZ8EoKu4?si=d5ftS2YDfN-PsHzI) as the main guides for developing this program.

Feel free to clone this repository, modify the code, and make changes 😁.
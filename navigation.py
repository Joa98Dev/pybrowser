# Libraries
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QAction

def add_nav_button(window, toolbar, label, callback):
    # Create and add a navigation button
    button = QAction(label, window)
    button.triggered.connect(callback)
    toolbar.addAction(button)

def navigate_home(window):
    # Navigate to the home page
    window.browser.setUrl(QUrl('https://duckduckgo.com/'))

def navigate_url(window):
    # Navigate to the URL in the URL bar
    url = window.url_bar.text()
    window.browser.setUrl(QUrl(url))

def update_url(window, url):
    # Update the URL to display the current URL
    window.url_bar.setText(url.toString())
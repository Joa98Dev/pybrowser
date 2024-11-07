# Libraries
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QMainWindow, QToolBar, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon
from navigation import add_nav_button, navigate_home, navigate_url, update_url

# GUI
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.init_ui()
    
    def init_ui(self):
        # Set up the browser view
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Set window icon
        #self.setWindowIcon(QIcon('icon.ico'))

        # Set up the navigation bar
        self.create_navbar()

        # Connect URL bar to browser
        self.url_bar.returnPressed.connect(lambda: navigate_url(self))
        self.browser.urlChanged.connect(lambda url: update_url(self, url))

    def create_navbar(self):
        # Create and set up the navigation bar
        navigation_bar = QToolBar()
        self.addToolBar(Qt.BottomToolBarArea, navigation_bar)

        # Add navigation buttons
        add_nav_button(self, navigation_bar, 'Back', self.browser.back)
        add_nav_button(self, navigation_bar, 'Forward', self.browser.forward)
        add_nav_button(self, navigation_bar, 'Refresh', self.browser.reload)
        add_nav_button(self, navigation_bar, 'Home', lambda: navigate_home(self))

        # Create and add the URL bar
        self.url_bar = QLineEdit()
        navigation_bar.addWidget(self.url_bar)
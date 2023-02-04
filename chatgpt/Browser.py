import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QHBoxLayout, QAction, QToolBar, QStatusBar
from PyQt5.QtCore import Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Web Browser")
        self.setGeometry(0, 0, 800, 600)

        # Create a QWebEngineView widget
        self.view = QWebEngineView(self)
        self.view.load(QUrl("https://www.google.com"))
        self.setCentralWidget(self.view)

        # Create a QLineEdit widget for the URL bar
        self.url_bar = QLineEdit(self)
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # Create a toolbar
        self.navigation_bar = QToolBar(self)
        self.navigation_bar.setMovable(False)
        self.addToolBar(Qt.TopToolBarArea, self.navigation_bar)

        # Add buttons to the toolbar
        self.back_button = QAction("<", self)
        self.back_button.triggered.connect(self.view.back)
        self.navigation_bar.addAction(self.back_button)

        self.forward_button = QAction(">", self)
        self.forward_button.triggered.connect(self.view.forward)
        self.navigation_bar.addAction(self.forward_button)

        self.navigation_bar.addWidget(self.url_bar)
        self.view.urlChanged.connect(self.update_url_bar)

        # Add a status bar
        self.status = QStatusBar(self)
        self.setStatusBar(self.status)
        self.view.loadFinished.connect(self.on_load_finished)

        # Show the main window
        self.show()

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.view.load(q)

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)
        
    def on_load_finished(self, status):
        if status:
            self.status.showMessage("Load finished", 5000)
        else:
            self.status.showMessage("Load failed", 5000)

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    browser = Browser()
    sys.exit(app.exec_())

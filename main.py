import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit,QPushButton, QListWidget


class BookFinderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Book Finder")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()

        self.searchLineEdit = QLineEdit(self)
        self.searchLineEdit.setPlaceholderText("Enter book title")
        layout.addWidget(self.searchLineEdit)

        self.searchButton = QPushButton("Search", self)
        self.searchButton.clicked.connect(self.search_books)
        layout.addWidget(self.searchButton)

        self.resultsListWidget = QListWidget(self)
        layout.addWidget(self.resultsListWidget)

        central_widget.setLayout(layout)

    def search_books(self):
        query = self.searchLineEdit.text()
        if query:
            self.resultsListWidget.clear()
            books = self.fetch_books(query)
            for book in books:
                self.resultsListWidget.addItem(book)

    def fetch_books(self, query):
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [item['volumeInfo']['title'] for item in data.get('items', [])]
        else:
            return []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BookFinderApp()
    window.show()
    sys.exit(app.exec_())

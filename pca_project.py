import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Set the window title
        self.setWindowTitle("PCA Application")
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow {font-size: 30px;}")
        #self.setWindowIcon(QIcon('logo.png'))
        # Create a combo box for the separator
        self.separator_combo = QComboBox(self)
        self.separator_combo.addItems(['Comma', 'Tab', 'Semicolon'])
        self.separator_combo.setCurrentIndex(0)

        # Create a "Open File" button
        self.open_file_button = QPushButton("Open File", self)
        self.open_file_button.clicked.connect(self.open_file)

        # Create a label to display the file name
        self.file_label = QLabel(self)

        # Create a placeholder for the scatter plot
        self.scatter_plot = QLabel(self)

        # Set the layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.separator_combo)
        layout.addWidget(self.open_file_button)
        layout.addWidget(self.file_label)
        layout.addWidget(self.scatter_plot)

        # Create a widget to hold the layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)

        # Set the central widget
        self.setCentralWidget(central_widget)

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","CSV Files (*.csv);;All Files (*)", options=options)
        if file_name:
            self.file_label.setText(file_name)
            separator = ','
            if self.separator_combo.currentText() == 'Tab':
                separator = '\t'
            elif self.separator_combo.currentText() == 'Semicolon':
                separator = ';'
            df = pd.read_csv(file_name, sep=separator)
            pca = PCA(n_components=2)
            principal_components = pca.fit_transform(df)
            explained_variance = pca.explained_variance_ratio_.sum()
            principal_df = pd.DataFrame(data = principal_components, columns = ['PC1', 'PC2'])
            plt.scatter(principal_df['PC1'], principal_df['PC2'])
            plt.xlabel('PC1')
            plt.ylabel('PC2')
            plt.title(f'Scatter Plot of Principal Components (Dataset Reduced by {explained_variance:.2f}%)')
            plt.legend(['Dataset'])
            plt.savefig('scatter_plot.png')
            self.scatter_plot.setPixmap(QPixmap("scatter_plot.png"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("#MainWindow {font-size: 30px; font-weight: bold; font-family: Tahoma; color: blue;}")
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
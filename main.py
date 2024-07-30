import sys
import numpy as np
import librosa.display
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class SpectrogramApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spectrogram Viewer")

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        self.button = QPushButton('Open Audio File')
        self.button.clicked.connect(self.open_file)

        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.canvas)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Audio File")
        if file_name:
            y, sr = librosa.load(file_name)
            self.ax.clear()
            S = librosa.feature.melspectrogram(y=y, sr=sr)
            librosa.display.specshow(librosa.power_to_db(S, ref=np.max), ax=self.ax, sr=sr)
            self.ax.set_title('Mel-frequency spectrogram')
            self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpectrogramApp()
    window.show()
    sys.exit(app.exec_())

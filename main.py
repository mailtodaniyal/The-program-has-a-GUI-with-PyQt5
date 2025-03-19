import sys
import os
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QMessageBox

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Select an option:")
        layout.addWidget(self.label)

        self.csv_button = QPushButton("Convert CSV for WordPress")
        self.csv_button.clicked.connect(self.process_csv)
        layout.addWidget(self.csv_button)

        self.stl_button = QPushButton("Convert STL to G-Code")
        self.stl_button.clicked.connect(self.convert_stl_to_gcode)
        layout.addWidget(self.stl_button)

        self.setLayout(layout)
        self.setWindowTitle("STL & CSV Converter")
        self.setGeometry(100, 100, 300, 200)

    def process_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)")
        if file_path:
            try:
                df = pd.read_csv(file_path)
                df['wordpress_variation'] = df['image'].apply(lambda x: f"variant_{x}")
                output_path = os.path.splitext(file_path)[0] + "_processed.csv"
                df.to_csv(output_path, index=False)
                QMessageBox.information(self, "Success", f"CSV processed and saved at {output_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to process CSV: {str(e)}")

    def convert_stl_to_gcode(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select STL File", "", "STL Files (*.stl)")
        if file_path:
            try:
                gcode_output = os.path.splitext(file_path)[0] + ".gcode"
                with open(gcode_output, "w") as f:
                    f.write("; Example G-Code generated from STL\n")
                    f.write(f"; Processed file: {file_path}\n")
                QMessageBox.information(self, "Success", f"G-Code generated and saved at {gcode_output}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to convert STL: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec_())

import os
import sys
from configparser import ConfigParser

from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw

from main_window import Ui_MainWindow
from syncronizer import Syncronizer as Sync

NAME_INI = "syncronizer.ini"
SOURCE_SECTION = "folders_source"
TARGET_SECTION = "folders_target"
KEY_PROGRAM_FILES = "program_files"
KEY_PROGRAM_DATA = "program_data"


class MainWindow(qtw.QMainWindow):
    # CONSTRUCTOR
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize status bar
        self.progressBar = qtw.QProgressBar()
        self.statusBar().addPermanentWidget(self.progressBar)
        self.reset_status_bar()

        # Restore values
        self.load_folders()

        # SIGNALS
        self.ui.btnQuit.clicked.connect(self.exit)
        self.ui.btnStart.clicked.connect(self.start_process)

    # METHODS

    def load_folders(self):
        if os.path.exists(NAME_INI):
            config = ConfigParser()
            config.read(NAME_INI)
            self.ui.txtProgramFilesSourceFolder.setText(
                config.get(SOURCE_SECTION, KEY_PROGRAM_FILES))
            self.ui.txtProgramDataSourceFolder.setText(
                config.get(SOURCE_SECTION, KEY_PROGRAM_DATA))
            self.ui.txtProgramFilesTargetFolder.setText(
                config.get(TARGET_SECTION, KEY_PROGRAM_FILES))
            self.ui.txtProgramDataTargetFolder.setText(
                config.get(TARGET_SECTION, KEY_PROGRAM_DATA))

    def save_folders(self):
        config = ConfigParser()
        if os.path.exists(NAME_INI):
            config.read(NAME_INI)

        if not config.has_section(SOURCE_SECTION):
            config.add_section(SOURCE_SECTION)
        if not config.has_section(TARGET_SECTION):
            config.add_section(TARGET_SECTION)

        config.set(SOURCE_SECTION, KEY_PROGRAM_FILES,
                   self.ui.txtProgramFilesSourceFolder.text())
        config.set(SOURCE_SECTION, KEY_PROGRAM_DATA,
                   self.ui.txtProgramDataSourceFolder.text())
        config.set(TARGET_SECTION, KEY_PROGRAM_FILES,
                   self.ui.txtProgramFilesTargetFolder.text())
        config.set(TARGET_SECTION, KEY_PROGRAM_DATA,
                   self.ui.txtProgramDataTargetFolder.text())
        with open(NAME_INI, 'w') as f:
            config.write(f)

    @qtc.Slot(str, int)
    def update_status_bar(self, filename, progress_value):
        self.progressBar.setValue(progress_value)
        self.statusBar().showMessage(filename)

    @qtc.Slot()
    def exit(self) -> None:
        """Close application when exit button is clicked"""
        sys.exit()

    @qtc.Slot()
    def start_process(self) -> None:
        self.start_gui()

        # Start process
        # Initialize syncronizer
        self.sync = Sync(pf_source_folder=self.ui.txtProgramFilesSourceFolder.text(),
                         pd_source_folder=self.ui.txtProgramDataSourceFolder.text(),
                         pf_target_folder=self.ui.txtProgramFilesTargetFolder.text(),
                         pd_target_folder=self.ui.txtProgramDataTargetFolder.text())

        self.sync.update.connect(self.update_status_bar)

        try:
            self.sync.start_sync()
        except FileNotFoundError as error:
            qtw.QMessageBox.critical(
                self, "Carpeta no encontrada", str(error), qtw.QMessageBox.Ok)

        self.end_gui()
        self.save_folders()
        qtw.QMessageBox.information(
            self, "Syncronizer", "Fin del proceso", qtw.QMessageBox.Ok)

    def end_gui(self):
        self.enable_buttons(True)
        qtw.QApplication.restoreOverrideCursor()

    def start_gui(self):
        qtw.QApplication.setOverrideCursor(qtc.Qt.WaitCursor)
        self.reset_status_bar()
        self.enable_buttons(False)

    def reset_status_bar(self) -> None:
        self.statusBar().showMessage("Ready")
        self.progressBar.setValue(0)

    def enable_buttons(self, enabled) -> None:
        self.ui.btnStart.setEnabled(enabled)
        self.ui.btnQuit.setEnabled(enabled)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

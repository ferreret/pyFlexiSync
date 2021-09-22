import os
import shutil

from PySide6.QtCore import Signal, QObject


class Syncronizer(QObject):

    update = Signal(str, int)

    def __init__(self, pf_source_folder: str,
                 pd_source_folder: str,
                 pf_target_folder: str,
                 pd_target_folder: str):
        super().__init__()

        self.folders = {
            "pf_source_folder": pf_source_folder,
            "pd_source_folder": pd_source_folder,
            "pf_target_folder": pf_target_folder,
            "pd_target_folder": pd_target_folder
        }

    def start_sync(self):
        self.validate_folders()
        self.counter = 0
        self.total_of_files = self.total_of_files()
        print(self.total_of_files)
        self.loop_files(self.folders["pf_source_folder"],
                        self.folders["pf_target_folder"])
        self.loop_files(self.folders["pd_source_folder"],
                        self.folders["pd_target_folder"])

    def loop_files(self, source_folder, target_folder):
        index_diff = len(source_folder)
        for root, dirs, files in os.walk(source_folder):
            # Create folders if needed
            self.checkFolders(index_diff, root, dirs, target_folder)
            # Copy/Overwrite files if needed
            self.checkFiles(index_diff, root, files, target_folder)

    def checkFolders(self, index_diff, root, dirs, target_folder):
        for dir in dirs:
            subs_dir = root[index_diff:]
            target = os.path.join(
                target_folder, subs_dir.lstrip("\\/"), dir)
            os.makedirs(target, exist_ok=True)

    def checkFiles(self, index_diff, root, files, target_folder):
        for file in files:
            self.counter += 1
            value = int((self.counter / self.total_of_files)*100)
            self.update.emit(file, value)
            source_file = os.path.join(root, file)
            # print(source_file)
            subs_dir = root[index_diff:]
            target_file = os.path.join(
                target_folder, subs_dir.lstrip("\\/"), file)
            if not os.path.exists(target_file) or self.check_time_file(source_file, target_file):
                print(target_file)
                shutil.copy(source_file, target_file)

    def check_time_file(self, source_file, target_file) -> bool:
        return os.path.getmtime(source_file) > os.path.getmtime(target_file)

    def validate_folders(self):
        for dir_path in self.folders.values():
            if not os.path.exists(dir_path):
                raise FileNotFoundError(
                    f"No se ha encontrado el directorio {dir_path}")

    def total_of_files(self):
        total = 0
        total = self.files_in_folder(self.folders["pf_source_folder"])
        total += self.files_in_folder(self.folders["pd_source_folder"])
        return total

    def files_in_folder(self, folder) -> int:
        counter = 0
        for _, _, files in os.walk(folder):
            counter += len(files)
        return counter

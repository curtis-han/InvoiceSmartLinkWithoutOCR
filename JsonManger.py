import json

class JsonManager:
    FILE_PATH = './config.json'

    def __init__(self):
        self.file_path = JsonManager.FILE_PATH
        self.data = self.read_json()

    def read_json(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {self.file_path}.")
            return None

    def write_json(self, data):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error writing JSON to file {self.file_path}: {e}")

# Example usage:
# manager = JsonManager()
# data = manager.read_json()
# print(data)
# manager.write_json({"key": "value"})
#把一个目录下的图片改名，并移动到另一个目录下
import os
import shutil
def move_file(from_dir, to_dir):
    for root, dirs, files in os.walk(from_dir):
        for file in files:
            file_path = os.path.join(root, file)
            new_file_path = os.path.join(to_dir, file)
            shutil.move(file_path, new_file_path)
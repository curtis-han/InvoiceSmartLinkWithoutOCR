import shutil
import os
from tkinter import Canvas, Tk
from PIL import Image, ImageTk

class ImageNavigator:
    def __init__(self):
        self.image_files = []
        self.current_index = -1
        self.photo = None  # 画像を保持するための属性

    def get_all_image_files(self, folder_path):
        image_files = []
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    image_files.append(os.path.join(root, file_name))
        return image_files

    def set_folder_path(self, folder_path):
        self.image_files = self.get_all_image_files(folder_path)

    def next_image(self):
        if not self.image_files:
            return None
        self.current_index = (self.current_index + 1) % len(self.image_files)
        return self.image_files[self.current_index]

    def previous_image(self):
        if not self.image_files:
            return None
        self.current_index = (self.current_index - 1) % len(self.image_files)
        return self.image_files[self.current_index]

    def show_image(self, canvas, image_path):
        self.current_image_path = image_path  # 現在の画像パスを更新
        self._draw_image(canvas, image_path)

    def show_image_from_image(self, canvas, image):
        self._draw_image_from_image(canvas, image)

    def _draw_image(self, canvas, image_path):
        image = Image.open(image_path)
        self._draw_image_from_image(canvas, image)

    def _draw_image_from_image(self, canvas, image):
        # Canvasのサイズを取得
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        print(f"Canvas size: {canvas_width}x{canvas_height}")

        # 画像のサイズを取得
        image_width, image_height = image.size
        print(f"Image size: {image_width}x{image_height}")

        # 画像のアスペクト比を保持しつつ、Canvasに収まるようにリサイズ
        scale = min(canvas_width / image_width, canvas_height / image_height)
        new_width = int(image_width * scale)
        new_height = int(image_height * scale)
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        print(f"Resized image size: {new_width}x{new_height}")

        # 画像をCanvasに表示できる形式に変換
        self.photo = ImageTk.PhotoImage(resized_image)

        # Canvasをクリア
        canvas.delete("all")

        # 画像をCanvasに描画
        canvas.create_image(0, 0, anchor='nw', image=self.photo)
        canvas.config(scrollregion=canvas.bbox("all"))
        print("Image drawn on canvas")

    def redraw_image(self, canvas):
        if self.current_image_path:
            self._draw_image(canvas, self.current_image_path)

###################################################
def move_file(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    dest_file_path = os.path.join(dest, os.path.basename(src))
    if os.path.exists(dest_file_path):
        #os.remove(dest_file_path)
        return
    shutil.move(src, dest)

if __name__ == "__main__":
    folder_path = "path/to/your/image/folder"
    navigator = ImageNavigator()
    navigator.set_folder_path(folder_path)
    
    root = Tk()
    
    # Canvasを作成
    canvas = Canvas(root, bg="#aaa")
    canvas.place(relx=0.0375, rely=0.2400, relwidth=0.6000, relheight=0.6000)
    
    # 最初の画像を表示
    first_image = navigator.next_image()
    if first_image:
        navigator.show_image(canvas, first_image)
    
    root.mainloop()
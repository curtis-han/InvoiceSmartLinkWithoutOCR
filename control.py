import os
from ImageNavigator import ImageNavigator, move_file
from JsonManger import JsonManager 
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from csvMgr import write2csv

image_navigator = ImageNavigator()
current_image_path = None
config_json = JsonManager()

WORKOUT_PATH = "./output/photo"


class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object

    def __init__(self):
        pass

    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
        self.image_navigator = ImageNavigator()
        self.current_image = None  # 現在の画像を保持するための属性
        self.ui.tk_select_box_AccountKind.config(values=config_json.data["勘定種別"])

    def redraw_image(self):
        self.image_navigator.redraw_image(self.ui.tk_canvas_SHOW_PICTURE)

    def reset_all_items(self):
        self.ui.tk_input_DATE_INPUT.delete(0, 'end')
        self.ui.tk_input_PRICE_INPUT.delete(0, 'end')
        self.ui.tk_input_COMMENT_INPUTG.delete(0, 'end')
        #self.ui.tk_select_box_AccountKind.set("")
        #self.ui.tk_select_box_AccountItem.set("")
        self.ui.tk_label_SHOW_PIC_PATH.config(text="")
        self.ui.tk_canvas_SHOW_PICTURE.delete("all")
        self.ui.tk_canvas_SHOW_PICTURE.update()  # Refresh the canvas to ensure it is cleared
        self.ui.tk_select_box_AccountKind.config(values=config_json.data["勘定種別"])
        global current_image_path
        current_image_path = None
        print("All items reset")

    def chooseFolder(self, evt):
        global current_image_path
        folder_path = filedialog.askdirectory()
        image_navigator.set_folder_path(folder_path)
        current_image_path = image_navigator.next_image()
        if current_image_path:
            self.current_image = Image.open(current_image_path)  # 画像を読み込む
            image_navigator.show_image(self.ui.tk_canvas_SHOW_PICTURE, current_image_path)
            self.ui.tk_label_SHOW_PIC_PATH.config(text=current_image_path)

    def showPrePic(self, evt):
        global current_image_path
        current_image_path = image_navigator.previous_image()
        print("Selected folder:", current_image_path)
        if current_image_path:
            # デバッグプリントを追加
            print(f"Attempting to open image at path: {current_image_path}")
            
            # パスの区切り文字を修正
            current_image_path = current_image_path.replace("\\", "/")
            
            # ファイルの存在確認
            if not os.path.exists(current_image_path):
                messagebox.showerror("エラー", f"ファイルが存在しません: {current_image_path}")
                return
            
            self.current_image = Image.open(current_image_path)  # 画像を読み込む
            image_navigator.show_image(self.ui.tk_canvas_SHOW_PICTURE, current_image_path)
            self.ui.tk_label_SHOW_PIC_PATH.config(text=current_image_path)
        else:
            messagebox.showinfo("提示", "すでに最初の一枚です")
            return
        print("<Button-1>事件未处理:", evt)

    def showNextPic(self, evt):
        global current_image_path
        current_image_path = image_navigator.next_image()
        print("Selected folder:", current_image_path)
        if current_image_path:
            # デバッグプリントを追加
            print(f"Attempting to open image at path: {current_image_path}")
            
            # パスの区切り文字を修正
            current_image_path = current_image_path.replace("\\", "/")
            
            # ファイルの存在確認
            if not os.path.exists(current_image_path):
                messagebox.showerror("エラー", f"ファイルが存在しません: {current_image_path}")
                return
            
            #self.current_image = Image.open(current_image_path)  # 画像を読み込む
            with Image.open(current_image_path) as img:
                self.current_image = img.copy()  # 复制图像到内存中
            image_navigator.show_image(self.ui.tk_canvas_SHOW_PICTURE, current_image_path)
            self.ui.tk_label_SHOW_PIC_PATH.config(text=current_image_path)
        else:
            messagebox.showinfo("提示", "すでに最後の一枚です")
            return
        print("<Button-1>事件未处理:", evt)

    def picOCR(self, evt):
        print("<Button-1>事件未处理:", evt)

    def WriteData2Excel(self, evt):
        global current_image_path
        writeDate = config_json.data["THIS_YEAR"] + self.ui.tk_input_DATE_INPUT.get()
        writePrice = self.ui.tk_input_PRICE_INPUT.get()
        writeComment = self.ui.tk_input_COMMENT_INPUTG.get()
        writeAccountItem = self.ui.tk_select_box_AccountItem.get()
        write_year_month = writeDate[:6]
        output_folder_path = WORKOUT_PATH + "/" + write_year_month
        #write_filename = current_image_path.split("/")[-1]
        filename_with_extension = os.path.split(current_image_path)[-1]
        filename_without_extension = os.path.splitext(filename_with_extension)[0]
        #--------------------------------------------------------
        message = f"请确认数据:\n日期: {writeDate}\n价格: {writePrice}\n评论: {writeComment}\n勘定項目: {writeAccountItem}"
        response = messagebox.askyesno("确认数据", message)
        if not response:
            return
        write2csv(writeDate, writePrice, writeComment, writeAccountItem, filename_without_extension)
        self.current_image.close()
        move_file(current_image_path, output_folder_path)
        self.reset_all_items()

        print("<Button-1>事件未处理: reset_all_items", evt)

    def on_account_kind_change(self, evt):
        self.ui.tk_select_box_AccountItem.config(values=config_json.data[self.ui.tk_select_box_AccountKind.get()])
        print("<Button-1>事件未处理:", evt)

    def rotateImage(self, evt):
        if self.current_image:
            self.current_image = self.current_image.rotate(90, expand=True)  # 画像を90度回転
            self.image_navigator.show_image_from_image(self.ui.tk_canvas_SHOW_PICTURE, self.current_image)
        print("<Button-1>事件未处理:", evt)
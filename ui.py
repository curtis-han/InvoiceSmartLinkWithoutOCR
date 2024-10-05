"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_OPEN_FOLDER_BTN = self.__tk_button_OPEN_FOLDER_BTN(self)
        self.tk_canvas_SHOW_PICTURE = self.__tk_canvas_SHOW_PICTURE(self)
        self.tk_select_box_OS_CHOICE = self.__tk_select_box_OS_CHOICE(self)
        self.tk_label_m1lpeeg9 = self.__tk_label_m1lpeeg9(self)
        self.tk_label_SHOW_PIC_PATH = self.__tk_label_SHOW_PIC_PATH(self)
        self.tk_button_PRE_PIC_BTN = self.__tk_button_PRE_PIC_BTN(self)
        self.tk_button_NEXT_PIC_BTN = self.__tk_button_NEXT_PIC_BTN(self)
        self.tk_button_OCR_BTN = self.__tk_button_OCR_BTN(self)
        self.tk_label_frame_CATEGORY_CONTAINER = self.__tk_label_frame_CATEGORY_CONTAINER(self)
        self.tk_select_box_AccountKind = self.__tk_select_box_AccountKind( self.tk_label_frame_CATEGORY_CONTAINER) 
        self.tk_label_m1lqqmcv = self.__tk_label_m1lqqmcv( self.tk_label_frame_CATEGORY_CONTAINER) 
        self.tk_label_m1lqr407 = self.__tk_label_m1lqr407( self.tk_label_frame_CATEGORY_CONTAINER) 
        self.tk_select_box_AccountItem = self.__tk_select_box_AccountItem( self.tk_label_frame_CATEGORY_CONTAINER) 
        self.tk_button_WRITE_EXCEL_BTN = self.__tk_button_WRITE_EXCEL_BTN(self)
        self.tk_label_frame_MD_CONTAINER = self.__tk_label_frame_MD_CONTAINER(self)
        self.tk_label_m1vqsi1l = self.__tk_label_m1vqsi1l( self.tk_label_frame_MD_CONTAINER) 
        self.tk_label_m1vqswfo = self.__tk_label_m1vqswfo( self.tk_label_frame_MD_CONTAINER) 
        self.tk_input_PRICE_INPUT = self.__tk_input_PRICE_INPUT( self.tk_label_frame_MD_CONTAINER) 
        self.tk_input_DATE_INPUT = self.__tk_input_DATE_INPUT( self.tk_label_frame_MD_CONTAINER) 
        self.tk_label_frame_m1vrfz9j = self.__tk_label_frame_m1vrfz9j(self)
        self.tk_input_COMMENT_INPUTG = self.__tk_input_COMMENT_INPUTG( self.tk_label_frame_m1vrfz9j) 
        self.tk_button_ROTATE_BTN = self.__tk_button_ROTATE_BTN(self)
    def __win(self):
        self.title("InvoiceSmartLink")
        # 设置窗口大小、居中
        width = 800
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.minsize(width=width, height=height)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_button_OPEN_FOLDER_BTN(self,parent):
        btn = Button(parent, text="画像フォルダを選択", takefocus=False,)
        btn.place(relx=0.4250, rely=0.0100, relwidth=0.1688, relheight=0.0500)
        return btn
    def __tk_canvas_SHOW_PICTURE(self,parent):
        canvas = Canvas(parent,bg="#aaa")
        canvas.place(relx=0.0375, rely=0.1200, relwidth=0.6000, relheight=0.8000)
        # サイズ変更イベントをバインド
        canvas.bind("<Configure>", self.on_canvas_resize)
        
        self.canvas = canvas  # Canvasをインスタンス変数として保持
        return canvas
    def on_canvas_resize(self, event):
        # Canvasのサイズが変更されたときに画像を再描画
        if hasattr(self, 'controller') and self.controller:
            self.controller.redraw_image()

    def __tk_select_box_OS_CHOICE(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("windows","mac os")
        cb.place(relx=0.1750, rely=0.0100, relwidth=0.1875, relheight=0.0400)
        return cb
    def __tk_label_m1lpeeg9(self,parent):
        label = Label(parent,text="システム選択",anchor="center", )
        label.place(relx=0.0375, rely=0.0100, relwidth=0.1250, relheight=0.0400)
        return label
    def __tk_label_SHOW_PIC_PATH(self,parent):
        label = Label(parent,text="パスが指定されていません",anchor="center", )
        label.place(relx=0.0375, rely=0.0700, relwidth=0.6000, relheight=0.0400)
        return label
    def __tk_button_PRE_PIC_BTN(self,parent):
        btn = Button(parent, text="pre", takefocus=False,)
        btn.place(relx=0.0688, rely=0.9400, relwidth=0.0625, relheight=0.0400)
        return btn
    def __tk_button_NEXT_PIC_BTN(self,parent):
        btn = Button(parent, text="next", takefocus=False,)
        btn.place(relx=0.3625, rely=0.9400, relwidth=0.0625, relheight=0.0400)
        return btn
    def __tk_button_OCR_BTN(self,parent):
        btn = Button(parent, text="画像を識別", takefocus=False,)
        btn.place(relx=0.1663, rely=0.9400, relwidth=0.1675, relheight=0.0400)
        return btn
    def __tk_label_frame_CATEGORY_CONTAINER(self,parent):
        frame = LabelFrame(parent,text="勘定科目",)
        frame.place(relx=0.6500, rely=0.0200, relwidth=0.3125, relheight=0.3400)
        return frame
    def __tk_select_box_AccountKind(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("")
        cb.place(relx=0.0400, rely=0.2353, relwidth=0.9200, relheight=0.1765)
        return cb
    def __tk_label_m1lqqmcv(self,parent):
        label = Label(parent,text="種類",anchor="center", )
        label.place(relx=0.0400, rely=0.0294, relwidth=0.2000, relheight=0.1765)
        return label
    def __tk_label_m1lqr407(self,parent):
        label = Label(parent,text="項目",anchor="center", )
        label.place(relx=0.0400, rely=0.4412, relwidth=0.2000, relheight=0.1765)
        return label
    def __tk_select_box_AccountItem(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("")
        cb.place(relx=0.0400, rely=0.6471, relwidth=0.9200, relheight=0.1765)
        return cb
    def __tk_button_WRITE_EXCEL_BTN(self,parent):
        btn = Button(parent, text="書き込み", takefocus=False,)
        btn.place(relx=0.6875, rely=0.8400, relwidth=0.1250, relheight=0.0600)
        return btn
    def __tk_label_frame_MD_CONTAINER(self,parent):
        frame = LabelFrame(parent,text="レシート情報",)
        frame.place(relx=0.6500, rely=0.4000, relwidth=0.3125, relheight=0.2000)
        return frame
    def __tk_label_m1vqsi1l(self,parent):
        label = Label(parent,text="価額",anchor="center", )
        label.place(relx=0.0160, rely=0.0500, relwidth=0.2000, relheight=0.3000)
        return label
    def __tk_label_m1vqswfo(self,parent):
        label = Label(parent,text="日付",anchor="center", )
        label.place(relx=0.0200, rely=0.4000, relwidth=0.2000, relheight=0.3000)
        return label
    def __tk_input_PRICE_INPUT(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.2400, rely=0.0500, relwidth=0.7200, relheight=0.3000)
        return ipt
    def __tk_input_DATE_INPUT(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.2400, rely=0.4000, relwidth=0.7200, relheight=0.3000)
        return ipt
    def __tk_label_frame_m1vrfz9j(self,parent):
        frame = LabelFrame(parent,text="Comment",)
        frame.place(relx=0.6500, rely=0.6200, relwidth=0.3125, relheight=0.1600)
        return frame
    def __tk_input_COMMENT_INPUTG(self,parent):
        ipt = Entry(parent, )
        ipt.place(relx=0.0600, rely=0.0250, relwidth=0.9200, relheight=0.3750)
        return ipt
    def __tk_button_ROTATE_BTN(self,parent):
        btn = Button(parent, text="回転", takefocus=False,)
        btn.place(relx=0.5125, rely=0.9400, relwidth=0.0625, relheight=0.0400)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_OPEN_FOLDER_BTN.bind('<Button-1>',self.ctl.chooseFolder)
        self.tk_button_PRE_PIC_BTN.bind('<Button-1>',self.ctl.showPrePic)
        self.tk_button_NEXT_PIC_BTN.bind('<Button-1>',self.ctl.showNextPic)
        self.tk_button_OCR_BTN.bind('<Button-1>',self.ctl.picOCR)
        self.tk_button_WRITE_EXCEL_BTN.bind('<Button-1>',self.ctl.WriteData2Excel)
        self.tk_select_box_AccountKind.bind("<<ComboboxSelected>>", self.ctl.on_account_kind_change)
        self.tk_button_ROTATE_BTN.bind('<Button-1>',self.ctl.rotateImage)
        pass
    def __style_config(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
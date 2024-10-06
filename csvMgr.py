import csv
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox 

OUTPUT_DIR = './output'

def write2csv(date, price, comment, account_item, voucher_number):
    year_month = date[:6]
    filename = f"仕訳帳_{year_month}.csv"
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    filepath = os.path.join(OUTPUT_DIR, filename)
    if not os.path.exists(filepath):
        # 使用 utf-8-sig 编码创建文件
        with open(filepath, 'w', newline='', encoding='utf-8-sig') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['日付', '金額', '借方科目', '概要', '貸方科目', '金額', '伝票番号'])
    
    # Read existing rows
    rows = []
    if os.path.exists(filepath):
        with open(filepath, 'r', newline='', encoding='utf-8-sig') as csvfile:
            csvreader = csv.reader(csvfile)
            rows = list(csvreader)
    
    # Check if the voucher_number already exists in the CSV
    if any(row[6] == voucher_number for row in rows[1:]):  # Skip header row
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        messagebox.showwarning("Duplicate Voucher Number", f"The voucher number {voucher_number} already exists in the CSV file.")
        return
    
    # Check for duplicates
    for row in rows[1:]:  # Skip header row
        if row[0] == date and row[1] == price:
            root = tk.Tk()
            root.withdraw()  # Hide the main window
            messagebox.showwarning("Duplicate Data", "The data with the same date and price already exists in the CSV file.")
            return
    
    # Append the new row
    new_row = [date, price, account_item, comment, '現金', price, voucher_number]
    rows.append(new_row)

    # Separate header and data rows
    header = rows[0]
    data_rows = rows[1:]

    # Sort data rows by date
    data_rows.sort(key=lambda x: datetime.strptime(x[0], '%Y%m%d'))

    # Write rows back to the CSV
    with open(filepath, 'w', newline='', encoding='utf-8-sig') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(data_rows)

    root = tk.Tk()
    root.withdraw()  # Hide the main window

    message = f"Row appended and sorted in CSV file: {filepath}\nContent: {new_row}"
    messagebox.showinfo("CSV Update", message)
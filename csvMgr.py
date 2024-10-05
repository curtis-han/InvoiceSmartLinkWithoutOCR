import csv
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def write2csv(date, price, comment, account_item, voucher_number):
    year_month = date[:6]
    filename = f"{year_month}.csv"
    filepath = os.path.join('./output', filename)
    if not os.path.exists(filepath):
        with open(filepath, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['日 付', '金 額', '借り方科目', '概要', '貸方科目', '金額','伝票番号'])
    # Read existing rows
    rows = []
    if os.path.exists(filepath):
        with open(filepath, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            rows = list(csvreader)

    # Append the new row
    new_row = [date, price, account_item, comment, '現金', price, voucher_number]
    rows.append(new_row)

    # Separate header and data rows
    header = rows[0]
    data_rows = rows[1:]

    # Sort data rows by date
    data_rows.sort(key=lambda x: datetime.strptime(x[0], '%Y%m%d'))

    # Write rows back to the CSV
    with open(filepath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(data_rows)

    root = tk.Tk()
    root.withdraw()  # Hide the main window

    message = f"Row appended and sorted in CSV file: {filepath}\nContent: {new_row}"
    messagebox.showinfo("CSV Update", message)
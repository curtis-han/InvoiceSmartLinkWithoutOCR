import csv
import os
from collections import defaultdict

"""
说明:
    这个是通过InvoiceSmartLink_withoutOCR软件生成的 仕訳帳 继续生成　総勘定元帳 和　試算表的
运行方法:
    python createGeneraLedgerANDTrialBalance.py
    然后输入 仕訳帳 的地址即可

"""

def create_general_ledger_from_csv(input_csv):
    # 提取输入文件名中的日期部分 (假设日期在文件名最后的格式是 YYYYMM)
    input_filename = os.path.basename(input_csv)
    date_part = input_filename.split('_')[-1].split('.')[0]  # 提取文件名中的日期部分

    # 创建一个字典来存储每个科目的明细
    ledger = defaultdict(list)

    # 读取CSV文件
    with open(input_csv, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            # 将借方科目的记录存储到字典中，并在借方列记录金额
            ledger[row['借方科目']].append({
                '日付': row['日付'],
                '借方': row['金額'],  # 借方金额
                '貸方': '',  # 貸方为空
                '伝票番号': row['伝票番号']
            })
            # 将貸方科目的记录存储到字典中，并在貸方列记录金额
            ledger[row['貸方科目']].append({
                '日付': row['日付'],
                '借方': '',  # 借方为空
                '貸方': row['金額'],  # 貸方金额
                '伝票番号': row['伝票番号']
            })

    # 创建输出目录
    output_dir = "総勘定元帳and試算表"
    os.makedirs(output_dir, exist_ok=True)

    # 按科目保存到文件，并将日期部分追加到文件名
    for account, transactions in ledger.items():
        file_path = os.path.join(output_dir, f"{account}_{date_part}.csv")
        with open(file_path, mode='w', encoding='utf-8-sig', newline='') as output_file:
            writer = csv.writer(output_file)
            # 写入表头，分成借方和貸方列
            writer.writerow(['日付', '借方', '貸方', '伝票番号'])
            # 写入每笔交易记录
            for transaction in transactions:
                writer.writerow([transaction['日付'], transaction['借方'], transaction['貸方'], transaction['伝票番号']])

    print(f"ファイルが作成されました: {output_dir} ディレクトリ内にあります。")

    # 返回生成的文件列表
    return os.listdir(output_dir), date_part

def generate_trial_balance_from_ledgers(ledger_files, date_part):
    trial_balance = {}

    # 读取每个総勘定元帳文件
    for ledger_file in ledger_files:
        # 从文件名提取勘定科目
        account_name = os.path.splitext(os.path.basename(ledger_file))[0].split('_')[0]

        with open(ledger_file, mode='r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # 提取借方和贷方金额，保持为空而不是设置为0
                debit_amount = row['借方'].strip() if '借方' in row else ''
                credit_amount = row['貸方'].strip() if '貸方' in row else ''

                # 如果科目已经存在于试算表中，则更新其借方和贷方总额
                if account_name not in trial_balance:
                    trial_balance[account_name] = {'借方': 0.0, '貸方': 0.0}

                # 如果借方金额不为空，则累加
                if debit_amount:
                    trial_balance[account_name]['借方'] += float(debit_amount)

                # 如果贷方金额不为空，则累加
                if credit_amount:
                    trial_balance[account_name]['貸方'] += float(credit_amount)

    # 创建试算表的输出文件
    output_file_name = f"試算表_{date_part}.csv"  # 修改输出文件名
    output_file_path = os.path.join("総勘定元帳and試算表", output_file_name)  # 确保文件在新的目录中

    with open(output_file_path, mode='w', encoding='utf-8-sig', newline='') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(['科目', '借方', '貸方'])  # 添加表头

        total_debit = 0.0  # 初始化借方总和
        total_credit = 0.0  # 初始化贷方总和

        for account, amounts in trial_balance.items():
            # 只保留非零的借方和贷方金额
            debit_total = amounts['借方'] if amounts['借方'] != 0 else ''
            credit_total = amounts['貸方'] if amounts['貸方'] != 0 else ''
            writer.writerow([account, debit_total, credit_total])

            # 累加借方和贷方金额
            if isinstance(amounts['借方'], (float, int)):
                total_debit += amounts['借方']
            if isinstance(amounts['貸方'], (float, int)):
                total_credit += amounts['貸方']

        # 写入借方和贷方总和
        writer.writerow(['合計', total_debit if total_debit else '', total_credit if total_credit else ''])

    print(f"試算表已生成: {output_file_path}")


if __name__ == "__main__":
    # 先创建総勘定元帳
    input_file_name = input("请输入CSV文件名（例如：仕訳帳.csv）: ")
    ledger_files, date_part = create_general_ledger_from_csv(input_file_name)

    # 然后生成试算表
    ledger_files = [os.path.join("総勘定元帳and試算表", file) for file in ledger_files]  # 构造完整路径
    generate_trial_balance_from_ledgers(ledger_files, date_part)

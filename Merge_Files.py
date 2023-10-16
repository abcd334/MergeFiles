import pandas as pd
import os
import sys

# 抓取路徑
script_path = sys.argv[0]

# 抓取folder
folder_path = os.path.dirname(script_path)

# 抓取所有文件
files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx') or f.endswith('.xls')]

# 新增合併檔
output_file = 'merged_data.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl', mode='w') as writer:

    for file in files:
        file_path = os.path.join(folder_path, file)
        xls = pd.ExcelFile(file_path)

        for sheet_name in xls.sheet_names:
            data = pd.read_excel(file_path, sheet_name=sheet_name)

            if sheet_name in writer.sheets:
                # 將資料往下新增
                start_row = writer.sheets[sheet_name].max_row
                data.to_excel(writer, sheet_name=sheet_name, index=False, header=False, startrow=start_row)
            else:
                # 新增工作頁
                data.to_excel(writer, sheet_name=sheet_name, index=False)

#print("合併完成，已儲存為merged_data.xlsx")
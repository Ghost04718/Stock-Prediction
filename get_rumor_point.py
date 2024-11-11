import pandas as pd
import re
import os

folder_path = r'C:\User\Desktop\new guba' 
df_dic = {}


for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.txt'):  # 检查是否为TXT文件
          file_path = os.path.join(root, file_name)
          data = []
          with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
          pattern = r"(\d{2}-\d{2} \d{2}:\d{2})"
          split_content = re.split(pattern, content)
          split_content = split_content[3:]
          for i in range(0, len(split_content), 2):  # 从0开始
            date_time = split_content[i].strip()

            # 确保 date_time 不为空
            if date_time:
                parts = date_time.split(' ')
                if len(parts) == 2:  # 检查是否有两个部分
                    date, time = parts
                    date = f"2024-{date}"
                    if date >= "2024-10-26" and date <= "2024-11-08":
                    
                        if i + 1 < len(split_content):
                           comment_lines= split_content[i + 1].strip().split('\n')
                        if len(comment_lines) >= 3:  # 检查是否有足够的行
                            comment = comment_lines[2].strip()
                            data.append({
                                'date': date,
                                'time': time,
                                'comment': comment
                            })
          df_dic[file_name] = pd.DataFrame(data)
print(df_dic)

import torch
from transformers import BertTokenizer, BertForSequenceClassification



import os
os.chdir('finBERT')

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="ProsusAI/finbert")
# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

import pandas as pd
from datetime import datetime, timedelta

weekends = ['2024-11-02','2024-11-03']

weekends = pd.to_datetime(weekends)
all_dates = pd.date_range(start='2024-10-28', end='2024-11-08')
trading_days = all_dates[~all_dates.isin(weekends)]

def adjust_date(row):
    date = pd.to_datetime(row['date'])
    time_obj = datetime.strptime(row['time'], '%H:%M')

    next_trading_day = trading_days[trading_days > date]
    if pd.to_datetime(row['date']) in weekends:
        if not next_trading_day.empty:
            row['date'] = next_trading_day[0].date()
            row['time'] = '00:00'

    return row

for name,df in df_dic.items():
  df = df.apply(adjust_date,axis =1)
  df['date'] = pd.to_datetime(df['date'])
  df= df.sort_values(by='date').reset_index(drop=True)
  sentiment_pipeline = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)


  results = df['comment'].apply(sentiment_pipeline)
  df['sentiment'] = results.apply(lambda x: x[0]['label'])
  df['score'] = results.apply(lambda x: x[0]['score'])
  df.to_csv(f"{name}.csv",index = False)
  print(f"{name} done")
    

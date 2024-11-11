import pandas as pd
import re
import os

folder_path =  r'C:\User\Desktop\news'  # 替换为实际文件夹名
df_dic = {}

for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith('.txt') :  # 检查是否为TXT文件
            print(file_name)
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.read()
            pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})\n(.*?)\n(.*?)\n'
            news = re.findall(pattern, lines, re.DOTALL)

            data = []
            for new in news:
                    date = new[0]
                    time = new[1]  # 提取时刻
                    summary = new[2].strip()  # 提取概要
                    if date >= "2024-10-26" and date <= "2024-11-08":
                        data.append({
                            'date': date,
                            'time': time,
                            'comment': summary
                        })
            df = pd.DataFrame(data)
            df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.strftime('%H:%M')
            df_dic[file_name] = df
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

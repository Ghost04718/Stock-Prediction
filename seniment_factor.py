import numpy as np
import pandas as pd
from datetime import datetime
import os
import re
basic = pd.read_csv('basic.csv')
basic['ts_code'] = basic['ts_code'].str.replace('.SZ', '').str.replace('.SH', '')


folder_path = r'C:\Users\sakura\Desktop\news score'
df_news = {}
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        filename_clean = filename.replace(".txt.csv", "")
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        score = df['score']
        score_scaled =  (score - score.min()) / (score.max() - score.min())
        df["score_scaled"] = score_scaled
        # stock_code = basic.loc[basic['name'] == filename_clean, 'ts_code'].iloc[0]
        # df_news[stock_code] = df
        stock_code_series = basic.loc[basic['name'] == filename_clean, 'ts_code']
        if not stock_code_series.empty:
            stock_code = stock_code_series.iloc[0]
            df_news[stock_code] = df
        else:
            print(f"没有找到匹配项: {filename_clean}")


folder_path = r'C:\Users\sakura\Desktop\rumor_score_final'
df_rumors = {}
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        filename_clean =filename.replace(".txt.csv", "")
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        score = df['score']
        score_scaled =  (score - score.min()) / (score.max() - score.min())
        df["score_scaled"] = score_scaled
        df_rumors[filename_clean] = df

stock_code = set(df_news.keys()) & set(df_rumors.keys())

for name in stock_code:
    df_new = df_news[name]
    df_new['date'] = pd.to_datetime(df_new['date'])  # 确保 date 列为日期格式
    df_new = df_new[df_new['date'] < '2024-11-09'] 
    df_rumor = df_rumors[name]
    df_rumor['date'] = pd.to_datetime(df_rumor['date'])  # 确保 date 列为日期格式
    df_rumor = df_rumor[df_rumor['date'] < '2024-11-09'] 
    
    
    #计算总情绪分数：
    merged_df = pd.concat([df_new, df_rumor])
    all_df = merged_df.groupby('date', as_index=False)['score_scaled'].sum()
    all_dates = pd.Series(pd.concat([df_new['date'], df_rumor['date']]).unique())
   
    #创建最终df:
    total_scores = all_df['score_scaled'].tolist()
    result = pd.DataFrame({
        "date": all_dates,
    })
    result = result.merge(all_df, on='date', how='left').fillna(0)
# 如果需要重命名列
    result.rename(columns={'score_scaled': 'total_score'}, inplace=True)
    
    #1.当日评论总量：
    factor1 = merged_df.groupby('date').size().reindex(result['date']).fillna(0).tolist()
    result['total_num'] = factor1

    #2.当日情绪分数均值：
    mean_scores = merged_df.groupby('date')['score_scaled'].mean().reindex(result['date']).fillna(0).tolist()
    result['senti_mean'] = mean_scores
    #3.当日情绪得分标准差
    factor3 = all_df['score_scaled'].std()
    result['senti_std'] = factor3
    #4.前后两个交易日情绪得分变化率
    result['per_chg'] = result['total_score'].diff()/result['total_score'].shift(1)
    
    #5.6.情绪的最大值和最小值
    # 计算最大和最小情绪分数
    def calculate_max(date):
    # 计算对应日期的最大值
        max_value = merged_df.loc[merged_df['date'] == date, 'score_scaled'].max()
        return max_value if pd.notna(max_value) else None  # 返回最大值或None

    def calculate_min(date):
        # 计算对应日期的最小值
        min_value = merged_df.loc[merged_df['date'] == date, 'score_scaled'].min()
        return min_value if pd.notna(min_value) else None 

    result['max_sen'] = result['date'].apply(calculate_max)
    result['min_sen'] = result['date'].apply(calculate_min)


    #7，8情绪得分过去三天/五天的滑动平均
    result['moving_avg_3'] = result['total_score'].rolling(window=3).mean()
    result['moving_avg_5'] = result['total_score'].rolling(window=5).mean()
    # #11股吧信息时间加权累计值：假定越早的评论对收盘价影响越大，权重为早上：中午：晚上 = 1：0.8:0.6

    # weights = {'00:00': 1, '11：30': 0.8, '15:00': 0.6}

    # # 将时间转换为权重
    # df_rumor['weight'] = df_rumor['time'].map(weights)

    # # 按日期分组并计算加权累计值
    # df_rumor['weighted_score'] = df_rumor['score_scaled'] * df_rumor['weight']
    # cumulative_scores = df_rumor.groupby('date')['weighted_score'].sum().reset_index()
    # result['time_weighted_score'] = cumulative_scores['weighted_score']
    # print(result)
    #用均值填充缺失值
    numeric_cols = result.select_dtypes(include='number').columns
    result[numeric_cols] = result[numeric_cols].fillna(result[numeric_cols].mean())

    result.to_csv(f'{name}_senti_factor.csv', index=False)
    print(f"Saved {name}_senti_factor.csv")

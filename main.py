import pandas as pd
import numpy as np
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import os

def predict_for_all_stocks(directory_path, start_date=None, end_date=None):
    # 找到所有的CSV文件
    all_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.csv')]
    # print("Files in directory:", all_files)

    predictions = []  # 存储每个股票的预测结果
    for file in all_files:
        # print(f"Processing file: {file}")
        
        # 读取并准备数据
        data = load_and_prepare_data(file, start_date, end_date)
        # print("111:",data.shape)
        
        # 如果数据为空，跳过此文件
        if data.empty:
            print(f"No valid data in {file}. Skipping.")
            continue

        # 训练模型并得到预测结果
        predicted_price = train_and_evaluate_lightgbm(data)
        predictions.append(predicted_price)
        print(f"Predicted price for {file}: {predicted_price}")
        with open('1110result_1.txt', 'a') as f:
            f.write(f"Predicted price for {file}: {predicted_price}\n")

    return predictions

def load_and_prepare_data(file_path, start_date=None, end_date=None):
    # 读取单个CSV文件
    data = pd.read_csv(file_path)
    # print(data.shape)
    
    # 确保 'trade_date' 是 pandas 的 datetime 类型
    data['trade_date'] = pd.to_datetime(data['trade_date'], format='%Y%m%d')
    # data['trade_date'] = pd.to_datetime(data['trade_date'], format='%Y-%m-%d')

    # 计算收益率并向前移两天
    data['return'] = data['close_qfq'].pct_change(1).shift(-2)

    # 删除缺失值
    data = data.dropna(subset=['return'])

    # 按交易日期排序
    data = data.sort_values(by='trade_date')

    # 如果指定了时间范围，进行过滤
    if start_date and end_date:
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        # 使用 between() 方法进行过滤
        data = data[data['trade_date'].between(start_date, end_date)]

    return data

def train_and_evaluate_lightgbm(data):
    # 构建滞后特征
    data['return_lag1'] = data['return'].shift(1)

    # 删除滞后特征中的NaN值
    data = data.dropna(subset=['return_lag1'])

    # 提取特征和标签
    X = data.drop(columns=['ts_code', 'trade_date', 'close_qfq', 'return'])
    y = data['return'].shift(-1).dropna()

    X = X.iloc[:-1]

    # 划分训练集和测试集
    train_size = int(len(X) * 0.8)
    X_train, X_test = X.iloc[:train_size], X.iloc[train_size:]
    y_train, y_test = y.iloc[:train_size], y.iloc[train_size:]

    if X_train.empty or y_train.empty:
        raise ValueError("X_train or y_train is empty after processing.")

    # 初始化LightGBM回归模型并训练
    model = LGBMRegressor(verbose=-1)
    model.fit(X_train, y_train)

    # 在测试集上预测
    y_pred = model.predict(X_test)

    # 打印评估指标
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    # print(f'Mean Squared Error: {mse}, Mean Absolute Error: {mae}')

    # 使用全部数据训练并预测下一个交易日
    model_full = LGBMRegressor(verbose=-1)
    model_full.fit(X, y)
    future_data = X.iloc[-1:].copy()  # 假设预测下一个交易日
    future_pred = model_full.predict(future_data)
    # print(future_pred)

    previous_close = data.iloc[-1]['close_qfq']
    predicted_price = previous_close * (1 + future_pred[0])

    # print(predicted_price)
    return predicted_price

# 1.2 输出预测结果到CSV文件
def output_to_csv(new_pred, file_name):
    # 检查 new_pred 是否是单个值
    if isinstance(new_pred, (int, float, np.float64)):  # 包括 numpy 的标量类型
        new_pred = [new_pred]  # 如果是单个值，转换为列表
    
    # 创建 DataFrame
    output = pd.DataFrame({'Predicted_Price': new_pred})
    
    # 输出到CSV文件
    output.to_csv(file_name, index=False)


# 2. 读取加入了非零factors的数据集，加入时间过滤
def train_with_non_zero_factors(directory_path_2, start_date=None, end_date=None):
    # 从目录中读取并准备数据（可选时间范围）
    data = load_and_prepare_data(directory_path_2, start_date, end_date)
    
    # 按照82分的方式进行数据划分，训练并预测
    non_zero_pred = train_and_evaluate_lightgbm(data)
    
    return non_zero_pred


# 3. 读取加入了情绪因子和factors的最近两个月的数据集，新增时间过滤
def train_with_sentiment_factors(directory_path_3, start_date, end_date):
    # 从目录中读取并准备两个月时间范围内的数据
    data = load_and_prepare_data(directory_path_3, start_date, end_date)
    # print("222:",data)
    # print(data['trade_date'].head())  # 查看前几行的日期格式

    # 按照82分的方式进行数据划分，训练并预测
    sentiment_pred = train_and_evaluate_lightgbm(data)
    # print(sentiment_pred)

    return sentiment_pred


if __name__ == "__main__":

    # # 第一次训练和预测（可以指定时间范围）
    # directory_path = "data01"
    # start_date_1 = '2005-04-08'  # 需要修改为你想要的开始日期
    # end_date_1 = '2024-11-08'    # 需要修改为你想要的结束日期

    # # 获取所有股票的预测结果
    # predictions_1 = predict_for_all_stocks(directory_path, start_date_1, end_date_1)

    # # 输出所有预测结果
    # # print("Predictions for all stocks_1:", predictions_1)

    
    # # 第二次训练和预测：非零factors（可以指定时间范围）
    # directory_path_2 = "data02"
    # start_date_2 = '2005-04-08'  # 需要修改为你想要的开始日期
    # end_date_2 = '2024-11-08'    # 需要修改为你想要的结束日期

    # # 获取所有股票的预测结果
    # predictions_2 = predict_for_all_stocks(directory_path_2, start_date_2, end_date_2)
    
    # 输出所有预测结果
    # print("Predictions for all stocks_2:", predictions_2)

    # 第三次训练和预测：情绪因子和非零factors（指定两个月的时间范围）
    directory_path_3 = "data03"
    start_date_3 = '2024-09-01'  # 替换为实际需要的开始日期
    end_date_3 = '2024-11-08'    # 替换为实际需要的结束日期

    # 获取所有股票的预测结果
    predictions_3 = predict_for_all_stocks(directory_path_3, start_date_3, end_date_3)
    
    # 输出所有预测结果
    # print("Predictions for all stocks_3:", predictions_3)

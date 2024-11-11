import pandas as pd
import numpy as np

def log(df):
    return np.log(df)

def abs(df):
    return np.abs(df)

def sign(df):
    return np.sign(df)

def add(df1,df2):
    return df1+df2

def sub(df1,df2):
    return df1-df2

def div(df1,df2):
    return df1/df2

def mul(df1,df2):
    return df1*df2

def ts_ffill(df,limit=None):
    return df.ffill(limit=limit,axis=0)

def ts_ref(df,win:int):
    return df.shift(win)

def ts_pct_chg(df,win:int=1):
    return df.pct_change(win)

def ts_delta(df,win:int=1):
    return df.diff(win)

def ts_mean(df,win:int):
    return df.rolling(window=win,min_periods=int(win*2/3)).mean()

def ts_sum(df,win:int):
    return df.rolling(window=win,min_periods=int(win*2/3)).sum()

def ts_min(df,win:int):
    return df.rolling(window=win,min_periods=int(win*2/3)).min()

def ts_max(df,win:int):
    return df.rolling(window=win,min_periods=int(win*2/3)).max()

def ts_median(df,win:int):
    return df.rolling(window=win,min_periods=int(win*2/3)).median()

def ts_rank(df,win:int):
    return df.rolling(window=win,min_periods=int(win*2/3)).rank(pct=True)

def ts_std(df,win:int):
    return df.rolling(window=win,min_periods=int(win*2/3)).std()

def ts_var(df,win:int):
    return df.rolling(window=win,min_periods=int(win*2/3)).var()

def ts_skew(df,win:int):
    return df.rolling(window=win,min_periods=int(win*2/3)).skew()

def ts_kurt(df,win:int):
    return df.rolling(window=win,min_periods=int(win*2/3)).kurt()

def cs_rank(df):
    return df.rank(axis=1,method='dense',pct=True)

def ts_corr(df1,df2,win:int):
    idx = list(set(list(df2.index) + list(df1.index)))
    idx.sort()
    min_periods = int(win/2)
    res = {}
    df3 = df1.reindex(index=idx)
    df4 = df2.reindex(index=idx)
    for x1,x2 in zip(df3.rolling(win),df4.rolling(win)):
        if (x1.shape[0] < min_periods) or (x1.shape[0] < min_periods):
            continue
        res[x1.index[-1]] = x1.corrwith(x2,axis=0)
    df=pd.concat(res,axis=1).T
    return df

def ts_cov(df1,df2,win:int):
    idx = list(set(list(df2.index) + list(df1.index)))
    idx.sort()
    min_periods = int(win/2)
    res = {}
    df3 = df1.reindex(index=idx)
    df4 = df2.reindex(index=idx)
    for x1,x2 in zip(df3.rolling(win),df4.rolling(win)):
        if (x1.shape[0] < min_periods) or (x1.shape[0] < min_periods):
            continue
        res[x1.index[-1]] = (x1.sub(x1.mean(axis=0),axis=1) * x2.sub(x2.mean(axis=0),axis=1)).mean(axis=0)
    df=pd.concat(res,axis=1).T
    return df

def zScore(df):
    return df.sub(df.mean(axis=1),axis=0).div(df.std(axis=1),axis=0)

def min_max(df):
    return df.sub(df.min(axis=1),axis=0).div(df.max(axis=1)-df.min(axis=1),axis=0)

def winsorize(df,q=0.025):
    return df.clip(df.quantile(q,axis=1),df.quantile(1-q,axis=1),axis=0)

def purify(df):
    df[np.isinf(df.astype(float))]=np.nan
    return df

def demean(df):
    return df.sub(df.mean(axis=1),axis=0)
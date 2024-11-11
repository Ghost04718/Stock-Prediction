import os
import pandas as pd
from factor_utils import *

def read_data(column_name):
    if column_name not in DATA.columns:
        DATA[column_name] = 0
    return DATA[column_name]

def get_Factor_0(start_date,end_date):
    pb1=read_data(column_name='pb')
    rolling0=ts_delta(pb1,10)
    return rolling0

def get_Factor_1(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_2(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_3(start_date,end_date):
    pe_leading4=read_data(column_name='pe_leading')
    rolling3=ts_delta(pe_leading4,10)
    una2=abs(rolling3)
    bin0=sub(0,una2)
    return bin0

def get_Factor_4(start_date,end_date):
    ps_leading1=read_data(column_name='ps_leading')
    rolling0=ts_delta(ps_leading1,10)
    return rolling0

def get_Factor_5(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_6(start_date,end_date):
    pe_trailing1=read_data(column_name='pe_trailing')
    rolling0=ts_delta(pe_trailing1,22)
    return rolling0

def get_Factor_7(start_date,end_date):
    pb4=read_data(column_name='pb')
    pb6=read_data(column_name='pb')
    rolling5=ts_delta(pb6,22)
    bin3=sub(pb4,rolling5)
    una2=abs(bin3)
    bin0=sub(0,una2)
    return bin0

def get_Factor_8(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_9(start_date,end_date):
    ps_ttm3=read_data(column_name='ps_ttm')
    rolling2=ts_std(ps_ttm3,22)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_10(start_date,end_date):
    pe_leading1=read_data(column_name='pe_leading')
    rolling0=ts_delta(pe_leading1,10)
    return rolling0

def get_Factor_11(start_date,end_date):
    ps_leading6=read_data(column_name='ps_leading')
    ps_trailing7=read_data(column_name='ps_trailing')
    bin5=mul(ps_leading6,ps_trailing7)
    pe_trailing6=read_data(column_name='pe_trailing')
    bin4=mul(bin5,pe_trailing6)
    una3=abs(bin4)
    rolling2=ts_std(una3,10)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_12(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_13(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_14(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_15(start_date,end_date):
    hf_volume_std2=read_data(column_name='hf_volume_std')
    una1=abs(hf_volume_std2)
    hf_net_inflow_volume_rate4=read_data(column_name='hf_net_inflow_volume_rate')
    hf_volume_std5=read_data(column_name='hf_volume_std')
    bin3=sub(hf_net_inflow_volume_rate4,hf_volume_std5)
    rolling2=ts_ref(bin3,10)
    bin0=div(una1,rolling2)
    return bin0

def get_Factor_16(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_17(start_date,end_date):
    hf_real_std3=read_data(column_name='hf_real_std')
    rolling2=ts_std(hf_real_std3,22)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_18(start_date,end_date):
    hf_volume_var_5m4=read_data(column_name='hf_volume_var_5m')
    rolling3=ts_max(hf_volume_var_5m4,5)
    hf_volume_std5=read_data(column_name='hf_volume_std')
    una4=abs(hf_volume_std5)
    bin2=div(rolling3,una4)
    bin0=sub(0,bin2)
    return bin0

def get_Factor_19(start_date,end_date):
    return read_data(column_name='hf_net_inflow_value_rate')

def get_Factor_20(start_date,end_date):
    return read_data(column_name='hf_volume_var_5m')

def get_Factor_21(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_22(start_date,end_date):
    hf_volume_std3=read_data(column_name='hf_volume_std')
    rolling2=ts_max(hf_volume_std3,44)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_23(start_date,end_date):
    return read_data(column_name='hf_close_net_inflow_volume_rate')

def get_Factor_24(start_date,end_date):
    return read_data(column_name='hf_close_netinflow_rate_small_order_act')

def get_Factor_25(start_date,end_date):
    pct_chg3=read_data(column_name='pct_chg')
    rolling2=ts_sum(pct_chg3,5)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_26(start_date,end_date):
    pct_chg3=read_data(column_name='pct_chg')
    rolling2=ts_std(pct_chg3,10)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_27(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_28(start_date,end_date):
    vol_hfq3=read_data(column_name='vol_hfq')
    rolling2=ts_std(vol_hfq3,5)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_29(start_date,end_date):
    pct_chg1=read_data(column_name='pct_chg')
    rolling0=ts_delta(pct_chg1,22)
    return rolling0

def get_Factor_30(start_date,end_date):
    pct_chg2=read_data(column_name='pct_chg')
    rolling1=ts_delta(pct_chg2,5)
    rolling0=ts_mean(rolling1,5)
    return rolling0

def get_Factor_31(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_32(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_33(start_date,end_date):
    amount1=read_data(column_name='amount')
    rolling0=ts_delta(amount1,44)
    return rolling0

def get_Factor_34(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_35(start_date,end_date):
    close_hfq1=read_data(column_name='close_hfq')
    rolling0=ts_delta(close_hfq1,10)
    return rolling0

def get_Factor_36(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_37(start_date,end_date):
    close_hfq3=read_data(column_name='close_hfq')
    rolling2=ts_skew(close_hfq3,5)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_38(start_date,end_date):
    pct_chg3=read_data(column_name='pct_chg')
    rolling2=ts_min(pct_chg3,5)
    pct_chg4=read_data(column_name='pct_chg')
    rolling3=ts_var(pct_chg4,5)
    bin1=add(rolling2,rolling3)
    rolling0=ts_min(bin1,10)
    return rolling0

def get_Factor_39(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_40(start_date,end_date):
    pb1=read_data(column_name='pb')
    rolling0=ts_delta(pb1,10)
    return rolling0

def get_Factor_41(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_42(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_43(start_date,end_date):
    pe_leading4=read_data(column_name='pe_leading')
    rolling3=ts_delta(pe_leading4,10)
    una2=abs(rolling3)
    bin0=sub(0,una2)
    return bin0

def get_Factor_44(start_date,end_date):
    ps_leading1=read_data(column_name='ps_leading')
    rolling0=ts_delta(ps_leading1,10)
    return rolling0

def get_Factor_45(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_46(start_date,end_date):
    pe_trailing1=read_data(column_name='pe_trailing')
    rolling0=ts_delta(pe_trailing1,22)
    return rolling0

def get_Factor_47(start_date,end_date):
    pb4=read_data(column_name='pb')
    pb6=read_data(column_name='pb')
    rolling5=ts_delta(pb6,22)
    bin3=sub(pb4,rolling5)
    una2=abs(bin3)
    bin0=sub(0,una2)
    return bin0

def get_Factor_48(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_49(start_date,end_date):
    ps_ttm3=read_data(column_name='ps_ttm')
    rolling2=ts_std(ps_ttm3,22)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_50(start_date,end_date):
    pe_leading1=read_data(column_name='pe_leading')
    rolling0=ts_delta(pe_leading1,10)
    return rolling0

def get_Factor_51(start_date,end_date):
    ps_leading6=read_data(column_name='ps_leading')
    ps_trailing7=read_data(column_name='ps_trailing')
    bin5=mul(ps_leading6,ps_trailing7)
    pe_trailing6=read_data(column_name='pe_trailing')
    bin4=mul(bin5,pe_trailing6)
    una3=abs(bin4)
    rolling2=ts_std(una3,10)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_52(start_date,end_date):
    pct_chg3=read_data(column_name='pct_chg')
    rolling2=ts_sum(pct_chg3,10)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_53(start_date,end_date):
    pct_chg3=read_data(column_name='pct_chg')
    rolling2=ts_mean(pct_chg3,22)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_54(start_date,end_date):
    amount3=read_data(column_name='amount')
    rolling2=ts_std(amount3,5)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_55(start_date,end_date):
    pct_chg4=read_data(column_name='pct_chg')
    rolling3=ts_std(pct_chg4,44)
    rolling2=ts_max(rolling3,10)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_56(start_date,end_date):
    pct_chg1=read_data(column_name='pct_chg')
    rolling0=ts_delta(pct_chg1,5)
    return rolling0

def get_Factor_57(start_date,end_date):
    vol_hfq5=read_data(column_name='vol_hfq')
    rolling4=ts_median(vol_hfq5,10)
    rolling3=ts_std(rolling4,5)
    una2=abs(rolling3)
    bin0=sub(0,una2)
    return bin0

def get_Factor_58(start_date,end_date):
    pct_chg1=read_data(column_name='pct_chg')
    rolling0=ts_delta(pct_chg1,44)
    return rolling0

def get_Factor_59(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_60(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_61(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_62(start_date,end_date):
    low_hfq1=read_data(column_name='low_hfq')
    rolling0=ts_delta(low_hfq1,5)
    return rolling0

def get_Factor_63(start_date,end_date):
    pct_chg4=read_data(column_name='pct_chg')
    rolling3=ts_sum(pct_chg4,44)
    una2=abs(rolling3)
    bin0=sub(0,una2)
    return bin0

def get_Factor_64(start_date,end_date):
    low_hfq3=read_data(column_name='low_hfq')
    rolling2=ts_rank(low_hfq3,5)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_65(start_date,end_date):
    amount2=read_data(column_name='amount')
    rolling1=ts_median(amount2,5)
    rolling0=ts_delta(rolling1,22)
    return rolling0

def get_Factor_66(start_date,end_date):
    return read_data(column_name='pcf_op_leading')

def get_Factor_67(start_date,end_date):
    close_hfq4=read_data(column_name='close_hfq')
    rolling3=ts_delta(close_hfq4,10)
    rolling2=ts_delta(rolling3,5)
    bin0=sub(0,rolling2)
    return bin0

def get_Factor_68(start_date,end_date):
    close_hfq4=read_data(column_name='close_hfq')
    rolling3=ts_std(close_hfq4,22)
    rolling2=ts_sum(rolling3,44)
    rolling1=ts_rank(rolling2,44)
    amount3=read_data(column_name='amount')
    rolling2=ts_max(amount3,44)
    bin0=sub(rolling1,rolling2)
    return bin0

def save_features_to_csv(start_date, end_date, output_file):
    features = {'trade_date': DATA['trade_date']}
    for i in range(69):
        func_name = f"get_Factor_{i}"
        if func_name in globals():
            features[f"Factor_{i}"] = globals()[func_name](start_date, end_date)
            if features[f"Factor_{i}"] is None or features[f"Factor_{i}"].empty:
                features[f"Factor_{i}"] = 0
    print(f'{output_file} processed')
    
    # Convert features to DataFrame
    features_df = pd.DataFrame(features)
    
    # Remove columns where all values are 0 or None
    features_df.dropna(axis=1, how='all', inplace=True)
    features_df = features_df.loc[:, (features_df != 0).any(axis=0)]
    merged_data = pd.merge(DATA, features_df, on='trade_date', how='right')
    merged_data.to_csv(output_file, index=False)

# Example usage
input_folder = "data01"
for filename in os.listdir(input_folder):
    if filename.endswith('.csv'):
        filepath = os.path.join(input_folder, filename)
        with open(filepath) as f:
            DATA = pd.read_csv(f)
            save_features_to_csv('2024-09-01', '2024-09-31', f'data02/{filename}')
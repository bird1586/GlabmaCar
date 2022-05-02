# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:51:30 2022

@author: bird1586
"""

import pandas as pd
import streamlit as st

@st.cache
def convert_df(df):
    return df.to_excel('df.xlsx', index=False)

def expand_columns(df, goal_columns):
    diff = int(goal_columns) - len(df.columns)
    if diff > 0:
        df[list(range(diff))] = ''
    return df

uploaded_file = st.file_uploader("請上傳EXCEL", type=["xlsx", 'xls'])
if uploaded_file is not None:

    df = pd.read_excel(uploaded_file)
    
    if len(df.columns) == 16:
        df = expand_columns(df, 31)
        df[['用車時間_date', '用車時間_time']] = df['用车时间'].str.split(' ', expand = True)
        
        df.columns = ["1", "状态", "下单时间", "服务类型", "城市", "6", '用车时间', "3", "4", "18", 
                      "服务司机", "中标时间(accept time)", "取消时间", 
                      "11", "12", "9", "2", "5", "7", "8", "13", "14", "15", "16", 
                      "17", "19", "20", "22", "23", "24", "25", "21", "10"]
        df['用车时间'] = pd.to_datetime(df['用车时间'])
        df = df.sort_values('用车时间')
        df = df.drop('用车时间', axis=1)
        df['4'] = '/' + df['4']
        df = df[["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", 
                "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", 
                "下单时间", "中标时间(accept time)", "状态", "取消时间", "服务司机", "服务类型", "城市"]]
        

    elif len(df.columns) == 15:
        df = expand_columns(df, 31)
        df[['用車時間_date', '用車時間_time']] = df['用车时间'].str.split(' ', expand = True)
        
        df.columns = ["1", "下单时间", "用车时间", "城市", "服务类型", "6", "22", 
                      "23", "24", "25", "订单币种", "17", "订单状态", "司机ID", 
                      "司机名称", "2", "3", "4", "5", "7", "8", "9", "11", "12", 
                      "13", "14", "15", "16", "18", "19", "20", "21", "10"]
        df['用车时间'] = pd.to_datetime(df['用车时间'])
        df = df.sort_values('用车时间')
        df = df.drop('用车时间', axis=1)
        df['11'] = df['22'] + df['23']
        df['12'] = df['24'] + df['25']
        df = df[["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", 
                 "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", 
                 "23", "24", "25", "下单时间", "订单币种", "订单状态", "司机ID", 
                 "司机名称", "服务类型", "城市"]]


    excel = convert_df(df)
    st.download_button(
         label="Download data as excel",
         data=open("df.xlsx", "rb"),
         file_name='df.xlsx',
         mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
         )
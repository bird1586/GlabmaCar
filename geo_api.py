# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:10:57 2022

@author: bird1586
"""

import requests
import streamlit as st

@st.cache
def get_place_id(address, key):
    res = requests.get(r"https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(address, key))
    info = res.json()
    place_id = info['results'][0]['place_id']
    return place_id
    
    
airport_geo = {
     'ChIJ19_3qSJnHTERGxzCAZNLHLo': '蘇凡納布國際機場',
     'ChIJLaasHYiC4jARoP8LPbMAAQ8': '廊曼國際機場',
     'ChIJCQ93jJhIUDAR0DDUaWtBtOU': '布吉國際機場',
     'ChIJifGY5ogw2jARl0WT_eN0JKA': '清邁國際機場',
     'ChIJtxhNQDnwVDAR8DlfC70jAg8': '蘇梅國際機場',
     'ChIJuX0BcVzzAjERwmdj6C18_Mc': '烏塔保國際機場',
     'ChIJUTiTiTiSUTARsDpfC70jAg8': '甲米機場',
     'ChIJY3uQgQLZTDARwDpfC70jAg8': '合艾國際機場'
     }



address = st.text_input('請輸入地址', '')
if address:
    place_id = get_place_id(address, 'AIzaSyBhOwEgmj0xEkdFeDIp4BIG6-Cm89UCt30')
    if place_id in airport_geo:
        st.write('你輸入的是: {}'.format(airport_geo[place_id]))
    else:
        st.write('我不認識這裡欸...')


    
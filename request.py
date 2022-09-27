# -*- coding: utf-8 -*-


import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url, json={'Hour (0 to 23)': 10, 'Temperature (°C)': 10, 'Humidity (%)': 60, 'Wind Speed (m/s)': 3,
                             'Visibility (10m)': 1000
    , 'Solar radiation (MJ/m2)': 0, 'Rainfall (mm)': 0, 'Snowfall (cm)': 2
    , 'WeekDay (1 to 7)': 1, 'Month': 12
                             }
                  )

print(r.json())

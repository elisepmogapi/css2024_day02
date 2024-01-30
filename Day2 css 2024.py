# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:48:39 2024

@author: user
"""

import pandas as pd

file = pd.read_csv("data_02/iris.csv")

"""
Absolute Path:
C:/Users/user/Desktop/2024/css2024 day 2/data_02/iris.csv

Relative Path:
iris.csv 
"""

file = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

file = pd.read_csv(url)

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal width', 'class']

file = pd.read_csv(url, header=None, names = column_names)

file = pd.read_csv("data_02/Geospatial Data.txt", sep=";")

file = pd.read_excel("data_02/residentdoctors.xlsx")

file = pd.read_json("data_02/student_data.json")

print(file)
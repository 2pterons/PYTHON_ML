# -*- coding: utf-8 -*-
"""3-10.XGBoost(boston).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MGDQhuCSqplvGu7xkLvYymwsRd1_QZ-r
"""

# XGBoost로 Boston Housing 데이터를 학습한다.
# XGBoost for regression
# -----------------------------------------
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

# Boston housing data set을 읽어온다
boston = load_boston()

# Train 데이터 세트와 Test 데이터 세트를 구성한다
trainX, testX, trainY, testY = train_test_split(boston['data'], boston['target'], test_size = 0.2)

trainX.shape, trainY.shape

# XGBoost (regressor)로 Train 데이터 세트를 학습한다.
model = XGBRegressor(objective='reg:squarederror')  # default로 학습
model.fit(trainX, trainY)

# testX[n]에 해당하는 target (price)을 추정한다.
n = 1

df = pd.DataFrame([testX[n]])
df.columns = boston['feature_names']
print(df)

price = model.predict(testX[n].reshape(1,-1))
print('\n추정 price = %.2f' % (price))
print('실제 price = %.2f' % (testY[n]))
print('추정 오류 = rmse(추정 price - 실제 price) = %.2f' % np.sqrt(np.square(price - testY[n])))

# 시험 데이터 전체의 오류를 R-square로 표시한다.
print('시험 데이터 전체 오류 (R2-score) = %.4f' % model.score(testX, testY))


# -*- coding: utf-8 -*-
"""3-7.GBM(house_price_1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hDg1IYj_2_Lt5BM0cDX_MxzsraNCf1B1
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Commented out IPython magic to ensure Python compatibility.
# %cd '/content/drive/My Drive/Colab Notebooks'

# 데이터를 읽어온다.
house_df = pd.read_csv('data/house_price.csv')
house_df.head()

house_df.shape
house_df.dtypes.value_counts()
isnull = house_df.isnull().sum()
isnull[isnull > 0].sort_values(ascending = False)

# 전처리
df = house_df.copy()   # 원본 데이터는 보관해 둔다.

# 불필요한 컬럼과 Null 값이 많은 컬럼을 삭제한다.
df.drop(['Id', 'PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 'LotFrontage'], axis=1, inplace=True)

# 숫자형이 아니면 categorical로 변환하고, 숫자형은 결측치를 평균으로 대체한다.
enc = {}
for feat in df.columns:
    # categorical로 변환한다. 역변환이 가능하도록 LabelEncoder를 딕셔너리에 보관해 둔다.
    if df[feat].dtype == object:
        enc[feat] = LabelEncoder()
        df[feat] = enc[feat].fit_transform(df[feat].astype(str))
    
    # 결측치를 평균으로 대체한다.
    # elif df[feat].dtype == 'int64' or df[feat].dtype == 'float64':
    else:
        df[feat].fillna(df[feat].mean(), inplace = True)
df.head()

# 학습 데이터와 시험 데이터를 생성한다.
y_target = df['SalePrice']
x_features = df.drop('SalePrice', axis=1)
trainX, testX, trainY, testY = train_test_split(x_features, y_target, test_size = 0.2)

# Gradient Boosting (regressor)로 Train 데이터 세트를 학습한다.
# default:
# loss = least square
# learning_rate = 0.01
# n_estimators = 500
# max_depth = 5
model = GradientBoostingRegressor(loss='ls', learning_rate=0.01, n_estimators=500, max_depth=5)
model.fit(trainX, trainY)

# testX[n]에 해당하는 target (price)을 추정한다.
n = 0
price = model.predict(np.array(testX.iloc[n]).reshape(1, -1))
print('\n추정 price = %.2f' % (price))
print('실제 price = %.2f' % (testY.iloc[n]))
print('추정 오류 = rmse(추정 price - 실제 price) = %.2f' % np.sqrt(np.square(price - testY.iloc[n])))

# 테스트 데이터 전체의 R-sequare
print('R-square = %.4f' % model.score(testX, testY))


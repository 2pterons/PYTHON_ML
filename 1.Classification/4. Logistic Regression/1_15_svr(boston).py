# -*- coding: utf-8 -*-
"""1-15.SVR(boston).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DyrsBuRN1xHDv220CRtnImnWZ2i5jVzd
"""

import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

# 데이터를 읽어온다.
boston = load_boston()

# 데이터를 표준화한다.
scaleX = StandardScaler()
scaleY = StandardScaler()

feature_data = scaleX.fit_transform(boston.data)
target_data = scaleY.fit_transform(boston.target.reshape(-1, 1))

# 학습 데이터와 시험 데이터로 분리한다.
x_train,x_test,y_train,y_test = train_test_split(feature_data, target_data, test_size=0.2)

linear_svr = SVR(kernel='linear')
linear_svr.fit(x_train, y_train)

poly_svr = SVR(kernel='poly')
poly_svr.fit(x_train,y_train)

rbf_svr = SVR(kernel='rbf')
rbf_svr.fit(x_train,y_train)

# 임의의 textX의 target value를 추정한다.
n = 2

d = x_test[n].reshape(1, -1)
linear_pred = linear_svr.predict(d)
poly_pred = poly_svr.predict(d)
rbf_pred = rbf_svr.predict(d)

print('Actual price =', np.round(scaleY.inverse_transform(y_test[n])[0], 3))
print('Predicted :')
print('linear     =', np.round(scaleY.inverse_transform(linear_pred)[0], 3))
print('polynomial =', np.round(scaleY.inverse_transform(poly_pred)[0], 3))
print('RBF        =', np.round(scaleY.inverse_transform(rbf_pred)[0], 3))

print('R-square :')
print('linear     =', np.round(linear_svr.score(x_test,y_test), 3))
print('polynomial =', np.round(poly_svr.score(x_test,y_test), 3))
print('RBF        =', np.round(rbf_svr.score(x_test,y_test), 3))


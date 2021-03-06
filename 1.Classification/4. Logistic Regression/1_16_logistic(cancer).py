# -*- coding: utf-8 -*-
"""1-16.Logistic(cancer).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NF3uIA3NLwT22xwAjEmGXSulq3yjQhPj
"""

# KNN으로 Breast Cancer 데이터를 학습한다.
# ---------------------------------------
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.preprocessing import StandardScaler

# breast cancer 데이터를 가져온다.
cancer = load_breast_cancer()

# Z-score normalization
z_cancer = StandardScaler().fit_transform(cancer['data'])

# Train 데이터 세트와 Test 데이터 세트를 구성한다
trainX, testX, trainY, testY = train_test_split(z_cancer, cancer['target'], test_size = 0.2)

# Logistic Regression으로 Train 데이터 세트를 학습한다.
model = LogisticRegression()
model.fit(trainX, trainY)

# Test 세트의 Feature에 대한 class를 추정하고, 정확도를 계산한다
print("* 시험용 데이터로 측정한 정확도 = %.4f" % model.score(testX, testY))

# 수동으로 계산
predY = model.predict(testX)
accuracy = (testY == predY).mean()
print("* 시험용 데이터로 측정한 정확도 = %.4f" % accuracy)

# 학습된 w, b를 확인해 본다.
print('\nw :')
print(model.coef_)
print('\nb :')
print(model.intercept_)

# textX[0]의 class를 추정한다.
print('\ntestX[0]의 class :')
print('prob = ', model.predict_proba(testX)[0])

# manual로 testX[0]의 class를 추정해 본다. 각 파라메터의 기능을 확인한다.
theta = np.dot(model.coef_[0], testX[0]) + model.intercept_
prob = 1.0 / (1.0 + np.exp(-theta))
print('prob = ', prob)

# textX의 전체 class 확률를 추정한다.
predY_prob = model.predict_proba(testX)
predY_prob[:10]

# 확률로 class를 추정한다.
predY2 = np.argmax(predY_prob, axis=1)

predY2

# 이전 결과와 비교한다.
predY == predY2


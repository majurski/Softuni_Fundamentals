import csv
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

tests = []
cases = []

with open('covid-dataset-7-08-2020.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tests.append(row['Тестове за денонощие'])
        cases.append(row['Нови случаи за денонощие'])

tests = list(map(int, tests))
cases = list(map(int, cases))



cases_done = np.array(cases).reshape((-1, 1))
tests_done = np.array(tests)


model = LinearRegression().fit(cases_done, tests_done)
r_sq = model.score(cases_done, tests_done)
new_model = LinearRegression().fit(cases_done, tests_done.reshape((-1, 1)))

y_pred = model.predict(cases_done)

y_pred = model.intercept_ + model.coef_ * cases_done
print('predicted response:', y_pred, sep='\n')


# plt.plot(cases_done)
plt.plot(y_pred)
plt.ylabel('some numbers')
plt.show()

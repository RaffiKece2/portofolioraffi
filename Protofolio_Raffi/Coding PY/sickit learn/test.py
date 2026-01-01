from sklearn.datasets import load_diabetes
from sklearn.datasets import load_digits


data = load_diabetes()
print("dataset diabetes")
print(data.keys())

data1 = load_digits()
print("dataset digits")
print(data1.keys())
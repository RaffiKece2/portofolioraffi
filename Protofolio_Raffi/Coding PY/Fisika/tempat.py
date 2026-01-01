
from sklearn.preprocessing import LabelEncoder

user = input("Isi: ")

user_total = user.split()

y_encode = LabelEncoder()

total = y_encode.transform(user_total)
print(total)

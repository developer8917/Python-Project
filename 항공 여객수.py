# 가정 1. 코로나19 이후로 비행기를 이용하는 고객이 줄어들 것이다.

import matplotlib.pyplot as plt
import pandas as pd

# 파일 불러옴
data = pd.read_csv("/content/Passenger.csv")

# 년도에 따른 공항 여객수 표
plt.title("Changes in the number of air passengers after COVID-19")
plt.plot(data["Year"], data["Passenger"])
plt.xlabel("Year")
plt.ylabel("Passenger, 100 Million")

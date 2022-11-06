# 가정 3. 코로나로 인해 외식 산업에 악영향이 있었을 것이다.
# 외식산업 경기동향 지수표를 참고

import matplotlib.pyplot as plt
import pandas as pd

# 파일 불러옴
data = pd.read_csv("/content/CateringIndustry.csv")

# 년도에 따른 공항 화물표
plt.title("Changes in the food service industry after COVID-19")
plt.plot(data["Year"], data["EconomicTrendIndex"])
plt.xlabel("Year")
plt.ylabel("EconomicTrendIndex")

# 가정 2. 코로나19 이후로 실내에 있는 사람이 늘어나면서
#         직접 매장에 가서 구매하는 것보다 인터넷 구매를 하는 사람이 늘었을 것이다.
#         따라서 해외 구매도 코로나 이후로 늘어났을 것이다.

import matplotlib.pyplot as plt
import pandas as pd

# 파일 불러옴
data = pd.read_csv("/content/Freight.csv")

# 년도에 따른 공항 화물표
plt.title("Changes in the number of air cargo after COVID-19")
plt.plot(data["Year"], data["Freight"])
plt.xlabel("Year")
plt.ylabel("Freight")

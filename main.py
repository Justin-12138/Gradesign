import numpy as np
import pandas as pd
data=pd.DataFrame(data=np.arange(16).reshape(4,4),columns=list('ABCD'),dtype=float,copy=True)
print(data)
b=data.iloc[0]
print(b)
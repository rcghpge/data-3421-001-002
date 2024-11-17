import numpy as np
import pandas as pd

# Example: Create a random Dataframe
data = np.random.randn(10,3)
df = pd.DataFrame(data, columns=["A", "B", "C"])
print("DataFrame:")
print(df)

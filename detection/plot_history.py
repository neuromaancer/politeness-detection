import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../data/w2v_history.csv", index_col=False)
ax = df.plot()
ax.set_xlabel("Epoch")
ax.set_ylabel("Accuracy (%)")
fig = ax.get_figure()
fig.savefig("w2v.png")
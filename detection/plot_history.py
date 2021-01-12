import matplotlib.pyplot as plt
import pandas as pd

df_w2v = pd.read_csv("../data/w2v_history.csv", index_col=False)
df_bert = pd.read_csv("../data/bert_history.csv", index_col=False)
df_history = pd.concat([df_w2v, df_bert], axis=1)
df_history.to_csv("../data/history.csv", index=False)

# plot accuracy graph
accu_history = df_history[["w2v_epochs_accu_history", "bert_epochs_accu_history"]]
ax_accu = accu_history.plot()
ax_accu.set_xlabel("Epoch")
ax_accu.set_ylabel("Accuracy (%)")
fig_accu = ax_accu.get_figure()
fig_accu.savefig("../diagrams/accuracy_history.png")

# plot loss graph

loss_history = df_history[["w2v_epochs_loss_history", "bert_epochs_loss_history"]]
ax_loss = loss_history.plot()
ax_loss.set_xlabel("Epoch")
ax_loss.set_ylabel("Loss")
fig_loss = ax_loss.get_figure()
fig_loss.savefig("../diagrams/loss_history.png")
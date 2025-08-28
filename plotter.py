import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("adaptive_timeline.csv")


plt.figure(figsize=(10,6))
plt.plot(df["t_start"], df["pool"], marker="o", label="Pool (repliche)", color="red")
plt.plot(df["t_start"], df["intensity"], marker="s", label="Intensità workload", color="blue")
plt.xlabel("Tempo (s)")
plt.ylabel("Valore")
plt.title("Adattamento Pool vs Intensità del Workload")
plt.legend()
plt.grid(True)
plt.savefig("report_pool_vs_intensity.png")
plt.close()


plt.figure(figsize=(10,6))
plt.plot(df["t_start"], df["rejection_pred"], marker="o", label="Rejection predetta", color="green")
plt.axhline(0.01, color="red", linestyle="--", label="SLO = 0.01")
plt.xlabel("Tempo (s)")
plt.ylabel("Tasso di rejection")
plt.title("Qualità del Servizio (QoS)")
plt.legend()
plt.grid(True)
plt.savefig("report_rejection.png")
plt.close()


plt.figure(figsize=(10,6))
plt.plot(df["t_start"], df["idle_mean"], marker="o", label="Idle mean (repliche inattive)", color="orange")
plt.xlabel("Tempo (s)")
plt.ylabel("Idle medio")
plt.title("Efficienza nell'Uso delle Risorse")
plt.legend()
plt.grid(True)
plt.savefig("report_idle.png")
plt.close()


plt.figure(figsize=(10,6))
plt.step(df["t_start"], df["phase"], where="post", label="Phase (risacca)", color="purple")
plt.xlabel("Tempo (s)")
plt.ylabel("Fase")
plt.title("Fase della Risacca")
plt.legend()
plt.grid(True)
plt.savefig("report_phase.png")
plt.close()

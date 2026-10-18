
import pandas as pd
import tkinter as tk
from tkinter import ttk


df = pd.DataFrame({
    "Etudiant": ["E1", "E2", "E3", "E4", "E5"],
    "HEVR": [5, 10, 2, 12, 6],
    "NOTE": [10, 15, 8, 18, 12]
})


X = df["HEVR"].tolist()
Y = df["NOTE"].tolist()
n = len(X)

moy_X = sum(X) / n
moy_Y = sum(Y) / n

ver_X = sum((x - moy_X) ** 2 for x in X) / n
ver_Y = sum((y - moy_Y) ** 2 for y in Y) / n

conv_XY = sum(
    (X[i] - moy_X) * (Y[i] - moy_Y)
    for i in range(n)
) / n

corr_XY = conv_XY / (ver_X * ver_Y) ** 0.5

tab = [
    ("Moyenne", moy_X, moy_Y),
    ("Variance", ver_X, ver_Y),
    ("Covariance", ver_X, conv_XY),
    ("Correlation", corr_XY, 1.0),
]


a1 = tk.Tk()
a1.title("TP1 - Analyse de donnees")
a1.geometry("600x450")
a1.minsize(500, 400)


style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background="#FFFFFF",
    foreground="#1E293B",
    fieldbackground="#FFFFFF",
    rowheight=36,
    font=("Arial", 11),
    borderwidth=0
)

style.configure(
    "Treeview.Heading",
    background="#172554",
    foreground="#FFFFFF",
    font=("Arial", 10, "bold"),
    padding=10
)

style.map(
    "Treeview",
    background=[("selected", "#DBEAFE")],
    foreground=[("selected", "#172554")]
)


cadre = ttk.Frame(a1, padding=10)
cadre.pack(fill="both", expand=True)


ttk.Label(
    cadre,
    text="Donnees des etudiants",
    font=("Arial", 14, "bold")
).pack(pady=(0, 8))


zone_tableau = ttk.Frame(cadre)
zone_tableau.pack(fill="both", expand=True)

tableau = ttk.Treeview(
    zone_tableau,
    columns=list(df.columns),
    show="headings",
    height=5
)

barre = ttk.Scrollbar(
    zone_tableau,
    orient="vertical",
    command=tableau.yview
)

tableau.configure(yscrollcommand=barre.set)

tableau.pack(side="left", fill="both", expand=True)
barre.pack(side="right", fill="y")

for colonne in df.columns:
    tableau.heading(colonne, text=colonne)
    tableau.column(colonne, anchor="center", width=150)

for ligne in df.itertuples(index=False, name=None):
    tableau.insert("", "end", values=ligne)


stats = ttk.LabelFrame(
    cadre,
    text="Statistiques ",
    padding=8
)
stats.pack(fill="x", pady=(12, 0))

tableau_stats = ttk.Treeview(
    stats,
    columns=("Mesure", "HEVR", "NOTE"),
    show="headings",
    height=4
)

for colonne in ("Mesure", "HEVR", "NOTE"):
    tableau_stats.heading(colonne, text=colonne)
    tableau_stats.column(colonne, anchor="center", width=150)

tableau_stats.pack(fill="x", expand=True)

for mesure, valeur_hevr, valeur_note in tab:
    tableau_stats.insert(
        "",
        "end",
        values=(
            mesure,
            f"{valeur_hevr:.4f}",
            f"{valeur_note:.4f}"
        )
    )

a1.mainloop()

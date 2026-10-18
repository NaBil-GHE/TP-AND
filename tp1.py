
import pandas as pd
import tkinter as tk
from tkinter import ttk
import numpy as np



def dsEcld(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def dsManh(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)



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

ver_X = sum(
    (x - moy_X) ** 2 for x in X
) / n

ver_Y = sum(
    (y - moy_Y) ** 2 for y in Y
) / n

conv_XY = sum(
    (X[i] - moy_X) * (Y[i] - moy_Y)
    for i in range(n)
) / n

corr_XY = conv_XY / (ver_X * ver_Y) ** 0.5



mat_eucl = np.zeros((n, n))
mat_manh = np.zeros((n, n))

for i in range(n):
    for j in range(n):

        mat_eucl[i, j] = dsEcld(
            X[i], Y[i],
            X[j], Y[j]
        )

        mat_manh[i, j] = dsManh(
            X[i], Y[i],
            X[j], Y[j]
        )


print("Matrice des distances euclidiennes :")
print(
    pd.DataFrame(
        mat_eucl,
        index=df["Etudiant"],
        columns=df["Etudiant"]
    ).round(3)
)

print("\nMatrice des distances de Manhattan :")
print(
    pd.DataFrame(
        mat_manh,
        index=df["Etudiant"],
        columns=df["Etudiant"]
    ).round(3)
)



a1 = tk.Tk()
a1.title("TP1 - Analyse de donnees")
a1.geometry("850x550")
a1.minsize(650, 450)


style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background="#FFFFFF",
    foreground="#1E293B",
    fieldbackground="#FFFFFF",
    rowheight=32,
    font=("Arial", 10),
    borderwidth=0
)

style.configure(
    "Treeview.Heading",
    background="#172554",
    foreground="#FFFFFF",
    font=("Arial", 10, "bold"),
    padding=8
)

style.map(
    "Treeview",
    background=[("selected", "#DBEAFE")],
    foreground=[("selected", "#172554")]
)

style.configure(
    "TNotebook.Tab",
    padding=(12, 8),
    font=("Arial", 10, "bold")
)


titre = ttk.Label(
    a1,
    text="TP1 - Analyse de donnees",
    font=("Arial", 17, "bold")
)
titre.pack(pady=(12, 5))



notebook = ttk.Notebook(a1)
notebook.pack(
    fill="both",
    expand=True,
    padx=12,
    pady=10
)

page_donnees = ttk.Frame(notebook, padding=12)
page_stats = ttk.Frame(notebook, padding=12)
page_eucl = ttk.Frame(notebook, padding=12)
page_manh = ttk.Frame(notebook, padding=12)

notebook.add(page_donnees, text="Donnees")
notebook.add(page_stats, text="Statistiques")
notebook.add(page_eucl, text="Distance euclidienne")
notebook.add(page_manh, text="Distance Manhattan")




def creer_tableau(parent, colonnes, lignes):

    cadre = ttk.Frame(parent)
    cadre.pack(fill="both", expand=True)

    tableau = ttk.Treeview(
        cadre,
        columns=colonnes,
        show="headings"
    )

    scroll_y = ttk.Scrollbar(
        cadre,
        orient="vertical",
        command=tableau.yview
    )

    scroll_x = ttk.Scrollbar(
        cadre,
        orient="horizontal",
        command=tableau.xview
    )

    tableau.configure(
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set
    )

    tableau.grid(
        row=0,
        column=0,
        sticky="nsew"
    )

    scroll_y.grid(
        row=0,
        column=1,
        sticky="ns"
    )

    scroll_x.grid(
        row=1,
        column=0,
        sticky="ew"
    )

    cadre.rowconfigure(0, weight=1)
    cadre.columnconfigure(0, weight=1)

    for colonne in colonnes:
        tableau.heading(colonne, text=colonne)

        tableau.column(
            colonne,
            anchor="center",
            width=120,
            minwidth=80
        )

    for ligne in lignes:
        tableau.insert(
            "",
            "end",
            values=ligne
        )

    return tableau



ttk.Label(
    page_donnees,
    text="Donnees des etudiants",
    font=("Arial", 14, "bold")
).pack(anchor="w", pady=(0, 10))

creer_tableau(
    page_donnees,
    list(df.columns),
    list(df.itertuples(index=False, name=None))
)



ttk.Label(
    page_stats,
    text="Statistiques descriptives",
    font=("Arial", 14, "bold")
).pack(anchor="w", pady=(0, 10))

lignes_stats = [
    ("Moyenne", f"{moy_X:.4f}", f"{moy_Y:.4f}"),
    ("Variance", f"{ver_X:.4f}", f"{ver_Y:.4f}"),
    ("Covariance XY", f"{conv_XY:.4f}", "-"),
    ("Correlation Pearson", f"{corr_XY:.4f}", "-")
]

creer_tableau(
    page_stats,
    ["Mesure", "HEVR", "NOTE"],
    lignes_stats
)



ttk.Label(
    page_eucl,
    text="Matrice des distances euclidiennes",
    font=("Arial", 14, "bold")
).pack(anchor="w", pady=(0, 10))

lignes_eucl = [
    (
        nom,
        *[f"{valeur:.3f}" for valeur in ligne]
    )
    for nom, ligne in zip(
        df["Etudiant"],
        mat_eucl
    )
]

creer_tableau(
    page_eucl,
    ["Etudiant"] + df["Etudiant"].tolist(),
    lignes_eucl
)



ttk.Label(
    page_manh,
    text="Matrice des distances de Manhattan",
    font=("Arial", 14, "bold")
).pack(anchor="w", pady=(0, 10))

lignes_manh = [
    (
        nom,
        *[f"{valeur:.3f}" for valeur in ligne]
    )
    for nom, ligne in zip(
        df["Etudiant"],
        mat_manh
    )
]

creer_tableau(
    page_manh,
    ["Etudiant"] + df["Etudiant"].tolist(),
    lignes_manh
)


a1.mainloop()

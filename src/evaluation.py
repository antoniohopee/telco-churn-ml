import matplotlib.pyplot as plt
from sklearn.metrics import (
    f1_score, precision_score, recall_score,
    confusion_matrix, ConfusionMatrixDisplay
)


def build_comparison_row(name: str, y_test, y_pred) -> dict:
    """
    Calcola le metriche di valutazione per un singolo modello.
    Restituisce un dizionario compatibile con pd.DataFrame per la tabella comparativa.

    Parameters:
        name   : nome del modello (etichetta nella tabella)
        y_test : valori reali del test set
        y_pred : predizioni del modello

    Returns:
        dict con Precision, Recall, F1 sulla classe churned (1) e Macro F1
    """
    return {
        "Modello":        name,
        "Precision (1)":  round(precision_score(y_test, y_pred, pos_label=1, zero_division=0), 3),
        "Recall (1)":     round(recall_score(y_test, y_pred, pos_label=1, zero_division=0), 3),
        "F1 (1)":         round(f1_score(y_test, y_pred, pos_label=1, zero_division=0), 3),
        "Macro F1":       round(f1_score(y_test, y_pred, average="macro", zero_division=0), 3),
    }


def plot_confusion_matrix(y_test, y_pred, title: str, ax=None, save_path: str = None):
    """
    Visualizza la matrice di confusione per un classificatore binario churn/rimasto.

    Parameters:
        y_test     : valori reali del test set
        y_pred     : predizioni del modello
        title      : titolo del grafico
        ax         : asse matplotlib opzionale — se None crea una nuova figura
        save_path  : percorso dove salvare la figura (solo se ax=None)
    """
    cm = confusion_matrix(y_test, y_pred)
    own_figure = ax is None
    if own_figure:
        fig, ax = plt.subplots(figsize=(5, 4))

    ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Rimasto", "Churned"]
    ).plot(cmap="Blues", ax=ax, colorbar=False)

    ax.set_title(title, fontsize=12, fontweight="bold")

    if own_figure:
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches="tight")
        plt.show()

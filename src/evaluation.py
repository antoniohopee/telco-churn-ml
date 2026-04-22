from sklearn.metrics import f1_score, precision_score, recall_score


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

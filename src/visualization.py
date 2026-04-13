## US-08 DISTRIBUZIONE VARIABILI NUMERICHE PER CLASSE TARGET

import matplotlib.pyplot as plt
import seaborn as sns

def plot_numeric_distributions(df, variables, target_col, save_path=None):
    """
    Visualizza la distribuzione di variabili numeriche separata per classe target.

    Parameters:
        df         : DataFrame pandas
        variables  : lista di nomi di colonne numeriche da visualizzare
        target_col : nome della colonna target (es. 'churn')
        save_path  : percorso opzionale per salvare la figura
    """
    n = len(variables)
    cols = 2
    rows = (n + 1) // 2

    fig, axes = plt.subplots(rows, cols, figsize=(14, 5 * rows))
    axes = axes.flatten()

    for i, var in enumerate(variables):
        sns.histplot(
            data=df,
            x=var,
            hue=target_col,
            kde=True,
            stat='density',
            common_norm=False,
            ax=axes[i]
        )
        axes[i].set_title(f'Distribuzione di {var} per classe churn')
        axes[i].set_xlabel(var)
        axes[i].set_ylabel('Densità')

    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"✅ Grafico salvato in: {save_path}")

    plt.show()
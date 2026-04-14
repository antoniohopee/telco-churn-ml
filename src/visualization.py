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


def plot_categorical_churn_rates(df, variables, target_col, save_path=None):
    """
    Visualizza il tasso di churn percentuale per le principali variabili categoriche.
    Ogni subplot mostra un grafico a barre orizzontali ordinato per tasso decrescente.
    """
    n = len(variables)
    fig, axes = plt.subplots(1, n, figsize=(5 * n, 5))

    for ax, var in zip(axes, variables):
        churn_rate = (
            df.groupby(var)[target_col]
            .mean()
            .mul(100)
            .round(1)
            .sort_values(ascending=True)  # ascending per barh
        )

        bars = ax.barh(churn_rate.index, churn_rate.values, color='steelblue')

        # Annotazione percentuale su ogni barra
        for bar, val in zip(bars, churn_rate.values):
            ax.text(
                val + 0.5, bar.get_y() + bar.get_height() / 2,
                f'{val}%', va='center', fontsize=9
            )

        ax.set_title(var.replace('_', ' ').title(), fontsize=12, fontweight='bold')
        ax.set_xlabel('Churn Rate (%)')
        ax.set_xlim(0, churn_rate.max() + 10)
        ax.spines[['top', 'right']].set_visible(False)

    plt.suptitle('Tasso di Churn per Variabile Categorica', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Grafico salvato in: {save_path}")

    plt.show()
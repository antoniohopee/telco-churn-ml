## RINOMINA COLONNE IN SNAKE_CASE

import pandas as pd

COLUMN_RENAME_MAP = {
    'Age': 'age',
    'Avg Monthly GB Download': 'avg_monthly_gb_download',
    'Avg Monthly Long Distance Charges': 'avg_monthly_ld_charges',
    'Churn': 'churn',
    'CLTV': 'cltv',
    'Contract': 'contract',
    'Dependents': 'dependents',
    'Device Protection Plan': 'device_protection_plan',
    'Gender': 'gender',
    'Internet Service': 'internet_service',
    'Internet Type': 'internet_type',
    'Married': 'married',
    'Monthly Charge': 'monthly_charge',
    'Multiple Lines': 'multiple_lines',
    'Number of Dependents': 'num_dependents',
    'Number of Referrals': 'num_referrals',
    'Offer': 'offer',
    'Online Backup': 'online_backup',
    'Online Security': 'online_security',
    'Paperless Billing': 'paperless_billing',
    'Partner': 'partner',
    'Payment Method': 'payment_method',
    'Phone Service': 'phone_service',
    'Population': 'population',
    'Premium Tech Support': 'premium_tech_support',
    'Referred a Friend': 'referred_a_friend',
    'Senior Citizen': 'senior_citizen',
    'Streaming Movies': 'streaming_movies',
    'Streaming Music': 'streaming_music',
    'Streaming TV': 'streaming_tv',
    'Tenure in Months': 'tenure_months',
    'Total Charges': 'total_charges',
    'Total Extra Data Charges': 'total_extra_data_charges',
    'Total Long Distance Charges': 'total_ld_charges',
    'Total Refunds': 'total_refunds',
    'Total Revenue': 'total_revenue',
    'Unlimited Data': 'unlimited_data',
}

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rinomina le colonne del dataframe in snake_case
    usando il dizionario COLUMN_RENAME_MAP.
    """
    return df.rename(columns=COLUMN_RENAME_MAP)


## GESTIONE MISSING VALUES
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Gestisce i missing values del dataframe.
    - offer: NaN → 'No Offer' (cliente senza offerta attiva)
    - internet_type: NaN → 'No Internet' (cliente senza contratto internet)
    """
    df['offer'] = df['offer'].fillna('No Offer')
    df['internet_type'] = df['internet_type'].fillna('No Internet')
    return df


def detect_outliers_std(df: pd.DataFrame, columns: list, soglia: float = 3.0) -> pd.DataFrame:
    """
    Identifica gli outlier usando il metodo della deviazione standard.
    Un valore è outlier se si trova a più di `soglia` deviazioni standard dalla media.
    
    Parameters:
        df      : DataFrame pandas
        columns : lista di colonne numeriche da analizzare
        soglia  : numero di deviazioni standard (default: 3)
    
    Returns:
        DataFrame con statistiche e conteggio outlier per ogni colonna
    """
    risultati = []
    for col in columns:
        media = df[col].mean()
        std = df[col].std()
        outliers = df[(df[col] < media - soglia * std) | 
                      (df[col] > media + soglia * std)]
        risultati.append({
            'Variabile': col,
            'Media': round(media, 2),
            'Dev. Std.': round(std, 2),
            'Limite inferiore': round(media - soglia * std, 2),
            'Limite superiore': round(media + soglia * std, 2),
            'N. Outlier': len(outliers),
            '% Outlier': round(len(outliers) / len(df) * 100, 2)
        })
    return pd.DataFrame(risultati).sort_values('N. Outlier', ascending=False)
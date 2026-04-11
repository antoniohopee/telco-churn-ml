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
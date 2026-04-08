# 📱 Telco Customer Churn — Progetto ML

Progetto di Machine Learning per prevedere il churn dei clienti di una compagnia telefonica californiana.

## 📋 Descrizione

Il dataset contiene informazioni su 7.043 clienti (49 colonne). L'obiettivo è predire se un cliente
abbandonerà il servizio (`Churn Value`: 0 = rimasto, 1 = abbandonato).

## 👥 Team

- Antonio
- Davide
- Giada

## 🗂️ Struttura del progetto
```
telco-churn-ml/
├── data/
│   ├── raw/          # Dataset originale — NON modificare
│   └── processed/    # Dataset dopo pulizia
├── notebooks/        # Jupyter notebook per ogni sprint
├── src/              # Funzioni riutilizzabili
│   ├── preprocessing.py
│   ├── visualization.py
│   └── evaluation.py
├── outputs/figures/  # Grafici salvati
├── presentation/     # Slide finali
└── requirements.txt
```
## ⚙️ Installazione

```bash
# Clona la repository
git clone https://github.com/antoniohopee/telco-churn-ml.git
cd telco-churn-ml

# Crea e attiva il virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux

# Installa le dipendenze
pip install -r requirements.txt

# Avvia Jupyter
jupyter notebook
```

## 📊 Dataset

Disponibile su Hugging Face:
https://huggingface.co/datasets/aai510-group1/telco-customer-churn

## 🗓️ Sprint

| Sprint | Settimana | Contenuto |
|--------|-----------|-----------|
| Sprint 1 | Settimana 1 | Setup, caricamento dati, pulizia, analisi preliminare |
| Sprint 2 | Settimana 2 | EDA, analisi outlier, encoding |
| Sprint 3 | Settimana 3 | Feature selection, modelli ML, confronto finale |
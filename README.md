# 🧠 Analisi Radiomica e Classificazione di Immagini MRI Cerebrali (Sano vs Demente)

Pipeline riproducibile end-to-end in Python e MATLAB per l'estrazione di feature quantitative (Radiomica) da risonanze magnetiche cerebrali e la classificazione supervisionata di pazienti dementi e non dementi.

---

## 🔬 Panoramica del Progetto
Il progetto affronta la classificazione clinica partendo dalla segmentazione anatomica fino alla decisione computazionale[span_2](start_span)[span_2](end_span):
1. **Segmentazione & Controllo:** Definizione della Regione di Interesse (ROI) sulla sostanza bianca frontale (`Left-Frontal-White-Matter`) tramite **3D Slicer**[span_3](start_span)[span_3](end_span).
2. **Preprocessing & Resampling geometrico (Python):** Gestione di immagini volumetriche `.nrrd` con **SimpleITK** e **NumPy**, risolvendo problemi di disallineamento spaziale (*Image/Mask geometry mismatch*) tramite resampling[span_4](start_span)[span_4](end_span).
3. **Feature Extraction (PyRadiomics):** Estrazione automatizzata di marker quantitativi di forma, primi ordini e texture, organizzati tramite **Pandas** ed esportati in dataset tabulari Excel[span_5](start_span)[span_5](end_span).
4. **Machine Learning & Feature Selection (MATLAB):** Importazione dei dataset, split rigoroso 70/30 (training/validation), applicazione dell'algoritmo **ReliefF** sul solo training set per prevenire il data leakage, e addestramento di classificatori supervisionati (**Fine KNN**)[span_6](start_span)[span_6](end_span).

---

## 🛠️ Tech Stack & Strumenti
* **Linguaggi:** Python, MATLAB[span_7](start_span)[span_7](end_span)
* **Software Clinici:** 3D Slicer (segmentazione multi-piano e controllo volumetrico)[span_8](start_span)[span_8](end_span)
* **Elaborazione Immagini & Radiomica (Python):** SimpleITK, PyRadiomics, NumPy, Matplotlib[span_9](start_span)[span_9](end_span)
* **Data Management:** Pandas (strutturazione dataset ed export `.xlsx`)[span_10](start_span)[span_10](end_span)
* **Machine Learning & Statistica (MATLAB):** Classification Learner, ReliefF (Feature Selection), Fine KNN (Classificazione), Matrici di confusione[span_11](start_span)[span_11](end_span)

---

## ⚙️ Fasi della Pipeline
1. **Controllo Geometrico e Resampling:** Gestione di `origin`, `spacing` e `direction` per garantire la compatibilità geometrica tra maschera e MRI di riferimento in PyRadiomics[span_12](start_span)[span_12](end_span).
2. **Estrazione di Statistiche (Primo Ordine & Texture):** Calcolo di metriche descrittive (media, mediana, varianza, deviazione standard, *skewness*, *kurtosis*) circoscritte alla ROI[span_13](start_span)[span_13](end_span).
3. **Prevenzione del Data Leakage:** Suddivisione dei dati in training (70%) e validation (30%) *prima* dell'esecuzione di ReliefF e validazione esterna cieca sul modello esportato[span_14](start_span)[span_14](end_span).
4. **Valutazione e Confronto:** Analisi delle performance al variare delle feature selezionate (es. confronto tra 15 e 30 feature con classificatore Fine KNN, valutando accuratezza, sensibilità e matrici di confusione)[span_15](start_span)[span_15](end_span).

---

## 📊 Risultati Principali
* L'adozione di un approccio strutturato a 30 feature selezionate tramite ReliefF ha portato l'accuratezza di validazione al **63.33%**, migliorando significativamente il riconoscimento dei soggetti non dementi rispetto alla configurazione a 15 feature[span_16](start_span)[span_16](end_span).
* *Nota metodologica:* Il progetto costituisce una pipeline dimostrativa e riproducibile; i risultati preliminari evidenziano l'efficacia del preprocessing geometrico e richiedono dataset ampliati per una validazione clinica definitiva[span_17](start_span)[span_17](end_span).

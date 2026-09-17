#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 12:32:38 2026

@author: marble
"""

import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt
from radiomics import featureextractor 
import pandas as pd

# =============================================================================
# 1. PAZIENTE SANO
# =============================================================================
print("--- ELABORAZIONE PAZIENTE SANO ---")

image_path = '/Users/marble/Desktop/cartelle project/Project6/MRI_non_demente.nrrd'
mask_path = '/Users/marble/Desktop/cartelle project/Project6/Left-Frontal-White-Matter_non_demente.nrrd'

image_sitk = sitk.ReadImage(image_path)
mask_sitk = sitk.ReadImage(mask_path)

# Forziamo la maschera ad avere la stessa identica geometria dell'immagine
mask_sitk.CopyInformation(image_sitk)  

print("dimensione immagine MRI sano: ", image_sitk.GetSize())
print("dimensione maschera MRI sano: ", mask_sitk.GetSize())

image_np = sitk.GetArrayFromImage(image_sitk)
mask_np = sitk.GetArrayFromImage(mask_sitk)

print("Dimensione array immagine MRI sano: ", image_np.shape)
print("Dimensione array maschera MRI sano: ", mask_np.shape)

# Estrazione della slice centrale lungo l'asse Z
slice_idx = image_np.shape[2] // 2
print(f"visualizza la slice {slice_idx}")

image_slice = image_np[:, :, slice_idx]
mask_slice = mask_np[:, :, slice_idx]

# Orientamento per visualizzazione (Stile 3D Slicer / ITK-SNAP)
image_visualizzazione = image_slice.T[:, ::-1]
mask_visualizzazione = mask_slice.T[:, ::-1]

# Immagine originale sano
plt.figure()
plt.imshow(image_visualizzazione, cmap="gray")
plt.title("immagine MRI originale sano")
plt.axis("off")
plt.show()

# Maschera sano
plt.figure()
plt.imshow(mask_visualizzazione, cmap="Reds")
plt.title("maschera immagine MRI sano")
plt.axis("off")
plt.show()

# Immagine mascherata (solo ROI attiva)
image_masked = image_visualizzazione * mask_visualizzazione
plt.figure()
plt.imshow(image_masked, cmap="gray")
plt.title("immagine MRI mascherata sano")
plt.axis("off")
plt.show()

# Calcolo manuale delle caratteristiche del primo ordine
roi_pixels = image_np[mask_np > 0]

mean_val = np.mean(roi_pixels)
median_val = np.median(roi_pixels)
min_val = np.min(roi_pixels)
max_val = np.max(roi_pixels)
range_val = max_val - min_val
varianza = np.var(roi_pixels)
std_val = np.std(roi_pixels)
skewness_val = np.mean((roi_pixels - mean_val)**3) / (std_val ** 3)
kurtosis_val = np.mean((roi_pixels - mean_val)**4) / (std_val ** 4)

print("\nCaratteristiche radiomiche del primo ordine Sano: ")
print("Minimo:", min_val.round(3))
print(f"Massimo: {max_val:.3f}")

# Estrazione automatizzata con PyRadiomics
extractor = featureextractor.RadiomicsFeatureExtractor()
results = extractor.execute(image_sitk, mask_sitk)

for k, v in results.items():
    print(k, v)
    
df = pd.DataFrame([results])
df.to_excel("featureradiomicheSano.xlsx", index=False)


# =============================================================================
# 2. PAZIENTE MALATO
# =============================================================================
print("\n--- ELABORAZIONE PAZIENTE MALATO ---")

image_path_malato = '/Users/marble/Desktop/cartelle project/Project6/MRI_demente.nrrd'
mask_path_malato = '/Users/marble/Desktop/cartelle project/Project6/Left-Frontal-White-Matter_demente.nrrd'

image_sitk_malato = sitk.ReadImage(image_path_malato)
mask_sitk_malato = sitk.ReadImage(mask_path_malato)

# Forziamo la maschera ad avere la stessa identica geometria dell'immagine
mask_sitk_malato.CopyInformation(image_sitk_malato)  

print("dimensione immagine MRI malato: ", image_sitk_malato.GetSize())
print("dimensione maschera MRI malato: ", mask_sitk_malato.GetSize())

image_np_malato = sitk.GetArrayFromImage(image_sitk_malato)
mask_np_malato = sitk.GetArrayFromImage(mask_sitk_malato)

print("Dimensione array immagine MRI malato: ", image_np_malato.shape)
print("Dimensione array maschera MRI malato: ", mask_np_malato.shape)

# Estrazione della slice centrale lungo l'asse Z
slice_idx_malato = image_np_malato.shape[2] // 2
print(f"visualizza la slice {slice_idx_malato}")

image_slice_malato = image_np_malato[:, :, slice_idx_malato]
mask_slice_malato = mask_np_malato[:, :, slice_idx_malato]

# Orientamento per visualizzazione (Stile 3D Slicer / ITK-SNAP)
image_visualizzazione_malato = image_slice_malato.T[:, ::-1]
mask_visualizzazione_malato = mask_slice_malato.T[:, ::-1]

# Immagine originale malato
plt.figure()
plt.imshow(image_visualizzazione_malato, cmap="gray")
plt.title("immagine MRI originale malato")
plt.axis("off")
plt.show()

# Maschera malato
plt.figure()
plt.imshow(mask_visualizzazione_malato, cmap="Reds")
plt.title("maschera immagine MRI malato")
plt.axis("off")
plt.show()

# Immagine mascherata malato (solo ROI attiva)
image_masked_malato = image_visualizzazione_malato * mask_visualizzazione_malato
plt.figure()
plt.imshow(image_masked_malato, cmap="gray")
plt.title("immagine MRI mascherata malato")
plt.axis("off")
plt.show()

# Calcolo manuale delle caratteristiche del primo ordine Malato
roi_pixels_malato = image_np_malato[mask_np_malato > 0]

mean_val_m = np.mean(roi_pixels_malato)
median_val_m = np.median(roi_pixels_malato)
min_val_m = np.min(roi_pixels_malato)
max_val_m = np.max(roi_pixels_malato)
range_val_m = max_val_m - min_val_m
varianza_m = np.var(roi_pixels_malato)
std_val_m = np.std(roi_pixels_malato)
skewness_val_m = np.mean((roi_pixels_malato - mean_val_m)**3) / (std_val_m ** 3)
kurtosis_val_m = np.mean((roi_pixels_malato - mean_val_m)**4) / (std_val_m ** 4)

print("\nCaratteristiche radiomiche del primo ordine malato: ")
print("Minimo:", min_val_m.round(3))
print(f"Massimo: {max_val_m:.3f}")

# Estrazione automatizzata con PyRadiomics Malato
extractor_malato = featureextractor.RadiomicsFeatureExtractor()
results_malato = extractor_malato.execute(image_sitk_malato, mask_sitk_malato)

for k, v in results_malato.items():
    print(k, v)
    
df_malato = pd.DataFrame([results_malato])
df_malato.to_excel("featureradiomicheMalato.xlsx", index=False)

print("\nEsecuzione completata! Output salvati correttamente.")
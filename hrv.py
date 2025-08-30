import numpy as np

def fake_hrv_analysis(ecg_signal):
    mean_val = np.mean(ecg_signal)
    if mean_val < 0.3:
        return "mild"
    elif mean_val < 0.6:
        return "moderate"
    else:
        return "severe"

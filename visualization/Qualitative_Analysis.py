# visualization/Qualitative_Analysis.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from src.hybrid_model import Hybrid_ACO_GWO
from experiments.Quantitative_Benchmark import calculate_fitness

TARGET_SEED = 2734 

if __name__ == "__main__":
    data = load_digits(); X, y = data.data, data.target
    np.random.seed(TARGET_SEED)
    
    # تنفيذ الخوارزمية للهجين فقط لاستخراج القناع البصري
    hyb = Hybrid_ACO_GWO(20, 60)
    _, mask_h = hyb.fit(X, y, calculate_fitness)
    
    # رسم النتائج
    plt.imshow(mask_h.reshape(8, 8), cmap='Blues')
    plt.title(f"Optimal Feature Mask (Hybrid ACO-GWO)\nFeatures: {np.sum(mask_h)}")
    plt.axis('off')
    plt.show()

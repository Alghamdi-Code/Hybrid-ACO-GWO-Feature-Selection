# experiments/Quantitative_Benchmark.py
import numpy as np
import random
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits

# استدعاء الخوارزميات من المجلد المصدر
from src.hybrid_model import ACO_Standard, Standard_GWO, Hybrid_ACO_GWO

# إعدادات التجربة
POPULATION = 20    
ITERATIONS = 60    
NUM_RUNS = 10      

def calculate_fitness(X, y, mask):
    if np.sum(mask) == 0: return 0.0, 0.0
    X_sel = X[:, mask == 1]
    X_train, X_test, y_train, y_test = train_test_split(X_sel, y, test_size=0.3, random_state=42)
    clf = KNeighborsClassifier(n_neighbors=5)
    clf.fit(X_train, y_train)
    acc = accuracy_score(y_test, clf.predict(X_test))
    # دالة اللياقة الموزونة (99% دقة، 1% تقليل أبعاد)
    score = 0.99 * acc + 0.01 * (1 - (np.sum(mask) / X.shape[1]))
    return score, acc

if __name__ == "__main__":
    data = load_digits(); X, y = data.data, data.target
    print("Starting Quantitative Benchmark...")
    
    # هنا يتم استدعاء الخوارزمية الهجينة المقترحة
    hyb = Hybrid_ACO_GWO(POPULATION, ITERATIONS)
    best_score, best_mask = hyb.fit(X, y, calculate_fitness)
    
    print(f"Best Accuracy Achieved: {best_score:.4f}")
    print(f"Selected Features: {np.sum(best_mask)}")

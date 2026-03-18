# src/hybrid_model.py
import numpy as np
import random

class ACO_Standard:
    def __init__(self, n_ants, n_iter, alpha=1.0, rho=0.1):
        self.n_ants = n_ants
        self.n_iter = n_iter
        self.alpha = alpha
        self.rho = rho
        self.best_score = 0.0
        self.best_mask = []

    def fit(self, X, y, fitness_fn):
        n_feat = X.shape[1]
        tau = np.ones(n_feat) * 0.5
        for _ in range(self.n_iter):
            sols = []; scores = []
            for _ in range(self.n_ants):
                mask = np.zeros(n_feat, dtype=int)
                for i in range(n_feat):
                    if random.random() < (1/(1+np.exp(-(tau[i]**self.alpha)))): mask[i] = 1
                if np.sum(mask) == 0: mask[np.random.randint(0, n_feat)] = 1
                score, _ = fitness_fn(X, y, mask)
                sols.append(mask); scores.append(score)
                if score > self.best_score: self.best_score = score; self.best_mask = mask
            tau *= (1 - self.rho)
            for i in range(self.n_ants): tau += (sols[i] * scores[i] * 0.1)
        return self.best_score, self.best_mask

class Standard_GWO:
    def __init__(self, n_wolves, n_iter):
        self.n_wolves = n_wolves
        self.n_iter = n_iter
        self.best_score = 0.0
        self.best_mask = []

    def fit(self, X, y, fitness_fn):
        n_feat = X.shape[1]
        wolves = np.random.uniform(-2, 2, (self.n_wolves, n_feat))
        A_pos=np.zeros(n_feat); A_scr=float('-inf')
        B_pos=np.zeros(n_feat); B_scr=float('-inf')
        D_pos=np.zeros(n_feat); D_scr=float('-inf')
        for it in range(self.n_iter):
            for i in range(self.n_wolves):
                mask = np.where(1/(1+np.exp(-wolves[i])) > 0.5, 1, 0)
                score, _ = fitness_fn(X, y, mask)
                if score > A_scr: A_scr=score; A_pos=wolves[i].copy(); self.best_mask=mask
                elif score > B_scr: B_scr=score; B_pos=wolves[i].copy()
                elif score > D_scr: D_scr=score; D_pos=wolves[i].copy()
            a = 2 - it * (2/self.n_iter)
            for i in range(self.n_wolves):
                for j in range(n_feat):
                    r1=random.random(); r2=random.random(); X1=A_pos[j]-(2*a*r1-a)*abs(2*r2*A_pos[j]-wolves[i,j])
                    r1=random.random(); r2=random.random(); X2=B_pos[j]-(2*a*r1-a)*abs(2*r2*B_pos[j]-wolves[i,j])
                    r1=random.random(); r2=random.random(); X3=D_pos[j]-(2*a*r1-a)*abs(2*r2*D_pos[j]-wolves[i,j])
                    wolves[i,j]=(X1+X2+X3)/3
        self.best_score = A_scr
        return self.best_score, self.best_mask

class Hybrid_ACO_GWO(ACO_Standard):
    def fit(self, X, y, fitness_fn):
        n_feat = X.shape[1]
        tau = np.ones(n_feat) * 0.5
        for _ in range(self.n_iter):
            if len(self.best_mask) > 0: curr = self.best_mask.copy()
            else: curr = np.random.randint(0, 2, n_feat)
            for _ in range(10): 
                idx = np.random.randint(0, n_feat); tmp = curr.copy(); tmp[idx] = 1 - tmp[idx]
                score, _ = fitness_fn(X, y, tmp)
                if score > self.best_score:
                    self.best_score = score; self.best_mask = tmp; curr = tmp; tau += (tmp * 5.0) 
            sols = []; scores = []
            for _ in range(self.n_ants):
                mask = np.zeros(n_feat, dtype=int)
                for i in range(n_feat):
                    if random.random() < (1/(1+np.exp(-(tau[i]**self.alpha)))): mask[i] = 1
                if np.sum(mask) == 0: mask[np.random.randint(0, n_feat)] = 1
                score, _ = fitness_fn(X, y, mask)
                sols.append(mask); scores.append(score)
                if score > self.best_score: self.best_score = score; self.best_mask = mask
            tau *= (1 - self.rho)
            for i in range(self.n_ants):
                if scores[i] >= np.mean(scores): tau += (sols[i] * scores[i] * 0.5)
        return self.best_score, self.best_mask

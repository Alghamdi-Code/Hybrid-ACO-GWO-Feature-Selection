Source Code: Hybrid ACO-GWO for High-Dimensional Feature Selection
This repository provides the computational framework and experimental implementation of a Hybrid Swarm Intelligence algorithm, integrating Ant Colony Optimization (ACO) and the Grey Wolf Optimizer (GWO). The methodology is specifically designed to optimize feature selection in high-dimensional datasets, such as handwritten digit recognition, by balancing global exploration with local search exploitation.

1. Abstract and Methodology
The proposed hybrid mechanism addresses the stagnation in local optima often encountered in single-metaheuristic approaches. By incorporating a "Wolf Mutation" operator within the probabilistic structure of ACO, the algorithm ensures a more refined search toward the optimal feature subset.

The implementation utilizes a wrapper-based approach with a K-Nearest Neighbors (KNN) classifier to evaluate the fitness of selected features.

2. Experimental Results
The algorithm was validated using the Handwritten Digits Dataset (1797 samples, 64 features). Statistical analysis over 10 independent runs confirms the following:

Classification Accuracy: Average of 99.52% (± 0.0019).


Dimensionality Reduction: Mean reduction of 58%, retaining an average of 26.9 features from the original 64.


Robustness: High convergence stability as indicated by a standard deviation of ±1.6 in feature count.


3. Technical Requirements
The environment requires Python 3.x with the following scientific computing libraries:

scikit-learn: For dataset handling and classification.


numpy: For matrix operations and mathematical modeling.
matplotlib: For qualitative visual analysis of feature masks.
4. Implementation Details
main.py: Entry point for executing the hybrid optimization.
optimizer/: Core implementation of ACO pheromone updates and GWO hunting mechanisms.


results/: Visual qualitative analysis showing the structural skeleton of identified digits.


5. Licensing and Attribution
This project is licensed under the MIT License.
Citation
If this implementation contributes to your research, please cite the original work:
Alghamdi, A. (2026). Optimizing Feature Selection for Handwritten Digit Recognition using a Novel Hybrid ACO-GWO Algorithm.
6. Contact Information
Principal Researcher: Abdullah Alghamdi

Affiliation: Technical and Vocational Training Corporation (TVTC)
Correspondence: alghamdia@tvtc.gov.sa

Hybrid ACO-GWO Algorithm for High-Dimensional Feature Selection
This repository contains the primary Python implementation and experimental framework for a Hybrid Swarm Intelligence approach, integrating Ant Colony Optimization (ACO) and the Grey Wolf Optimizer (GWO). The project focuses on optimizing feature selection in high-dimensional datasets, specifically validated on handwritten digit recognition tasks.

1. Research Overview
Feature selection is a critical preprocessing stage in machine learning designed to mitigate the "curse of dimensionality" by eliminating redundant or noisy attributes. This implementation proposes a hybrid mechanism that leverages the global exploration capabilities of ACO and the local search precision (exploitation) of GWO.

Core Methodology:
Hybridization Strategy: Integration of a "Wolf Mutation" operator within the ACO probabilistic framework to prevent stagnation in local optima.


Fitness Evaluation: A wrapper-based approach using a K-Nearest Neighbors (KNN) classifier.


Objective Function: A multi-objective fitness function: $Fitness = 0.99 \times Accuracy + 0.01 \times Reduction$.


2. Experimental Performance
The proposed hybrid algorithm demonstrated superior performance compared to standard metaheuristic implementations:

Classification Accuracy: Achieved a mean accuracy of 99.52% (± 0.0019).


Dimensionality Reduction: Successfully reduced the feature space by 58%, retaining an average of only 26.9 features from the original 64.


Robustness: High convergence stability confirmed through 10 independent statistical runs.


3. Repository Structure
The source code is organized as follows:
Quantitative_Benchmark.py: Script for executing comparative analysis over multiple runs to generate statistical summaries.


Qualitative_Analysis.py: Script for visual verification of feature masks, demonstrating the extraction of the structural skeleton of the data.


LICENSE: MIT License governing the use of this software.
4. Environment and Setup
The implementation requires Python 3.x and the following scientific libraries:

Bash


pip install numpy scikit-learn matplotlib


To replicate the results, execute the benchmark script:

Bash


python Quantitative_Benchmark.py


5. Visual Analysis
Qualitative results indicate that the Hybrid ACO-GWO algorithm effectively identifies essential pixels while discarding approximately 62% of the image as noise, maintaining perfect legibility of the digit "3".

6. Citation and Attribution
If this work facilitates your research, please cite the following:
Alghamdi, A. (2026). Optimizing Feature Selection for Handwritten Digit Recognition using a Novel Hybrid ACO-GWO Algorithm.
7. Contact
Principal Investigator: A. Alghamdi
Affiliation: Technical and Vocational Training Corporation (TVTC)
Email: alghamdia@tvtc.gov.sa
Hybrid ACO-GWO Algorithm for High-Dimensional Feature Selection
This repository contains the primary Python implementation and experimental framework for a Hybrid Swarm Intelligence approach, integrating Ant Colony Optimization (ACO) and the Grey Wolf Optimizer (GWO). The project focuses on optimizing feature selection in high-dimensional datasets, specifically validated on handwritten digit recognition tasks.

1. Research Overview
Feature selection is a critical preprocessing stage in machine learning designed to mitigate the "curse of dimensionality" by eliminating redundant or noisy attributes. This implementation proposes a hybrid mechanism that leverages the global exploration capabilities of ACO and the local search precision (exploitation) of GWO.

Core Methodology:
Hybridization Strategy: Integration of a "Wolf Mutation" operator within the ACO probabilistic framework to prevent stagnation in local optima.


Fitness Evaluation: A wrapper-based approach using a K-Nearest Neighbors (KNN) classifier.


Objective Function: A multi-objective fitness function: $Fitness = 0.99 \times Accuracy + 0.01 \times Reduction$.


2. Experimental Performance
The proposed hybrid algorithm demonstrated superior performance compared to standard metaheuristic implementations:

Classification Accuracy: Achieved a mean accuracy of 99.52% (± 0.0019).


Dimensionality Reduction: Successfully reduced the feature space by 58%, retaining an average of only 26.9 features from the original 64.


Robustness: High convergence stability confirmed through 10 independent statistical runs.


3. Repository Structure
The source code is organized as follows:
Quantitative_Benchmark.py: Script for executing comparative analysis over multiple runs to generate statistical summaries.


Qualitative_Analysis.py: Script for visual verification of feature masks, demonstrating the extraction of the structural skeleton of the data.


LICENSE: MIT License governing the use of this software.
4. Environment and Setup
The implementation requires Python 3.x and the following scientific libraries:

Bash


pip install numpy scikit-learn matplotlib


To replicate the results, execute the benchmark script:

Bash


python Quantitative_Benchmark.py


5. Visual Analysis
Qualitative results indicate that the Hybrid ACO-GWO algorithm effectively identifies essential pixels while discarding approximately 62% of the image as noise, maintaining perfect legibility of the digit "3".

6. Citation and Attribution
If this work facilitates your research, please cite the following:
Alghamdi, A. (2026). Optimizing Feature Selection for Handwritten Digit Recognition using a Novel Hybrid ACO-GWO Algorithm.
7. Contact
Principal Investigator: Abdullah Alghamdi
Affiliation: Technical and Vocational Training Corporation (TVTC)
Email: alghamdia@tvtc.gov.sa

__author__ = "Haim Adrian"

from Functions import *
from matplotlib import pyplot as plt


def main():
    # Prepare the data for PCA (Ex8)
    training_dataset, test_dataset, validation_dataset, training_labels, test_labels, validation_labels = data_preparation('Data')

    # Ex9:
    # Centered data
    A = mean_removal(training_dataset)

    # Get eigen vectors sorted by eigen values in decreasing order
    V = calculate_eigen_vectors(A)

    # Eigen faces = centered matrix * V
    # F = A.dot(V)

    optimization_scores = optimize_eigen_faces(V, training_dataset, test_dataset, training_labels, test_labels)
    optimization_scores = np.array(optimization_scores) * 100

    plt.figure('Assignment 1')
    plt.plot(optimization_scores, 'r')
    plt.title('Optimization scores')
    plt.xlabel('K (amount of eigen vectors)')
    plt.ylabel('Score')
    plt.subplots_adjust(0.1, 0.1, 0.9, 0.95, 0.1, 0.1)
    plt.show()


main()

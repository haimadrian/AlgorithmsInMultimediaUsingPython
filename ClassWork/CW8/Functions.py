__author__ = "Haim Adrian"

import os
import os.path as path
import numpy as np
import cv2


def data_preparation(root_path, train_size=5, test_size=3, validation_size=2, img_dim=92*112):
    """
    Loads data from disk into 3 data sets.
    Each image is 92X112 pixels, and it should be grayscale
    :param root_path: The 'Data' directory, where we load images from.
    :param train_size:
    :param test_size:
    :param validation_size:
    :param img_dim:
    :return: 3 data sets based on the specified sizes and 3 corresponding label vectors
    """
    people_dirs = [d for d in os.listdir(root_path) if path.isdir(path.join(root_path, d))]
    training_dataset = np.zeros((len(people_dirs) * train_size, img_dim), dtype=np.float64)
    training_labels = np.zeros((len(people_dirs) * train_size), dtype=np.float64)
    test_dataset = np.zeros((len(people_dirs) * test_size, img_dim), dtype=np.float64)
    test_labels = np.zeros((len(people_dirs) * test_size), dtype=np.float64)
    validation_dataset = np.zeros((len(people_dirs) * validation_size, img_dim), dtype=np.float64)
    validation_labels = np.zeros((len(people_dirs) * validation_size), dtype=np.float64)

    training_row_index = 0
    test_row_index = 0
    validation_row_index = 0
    for curr_dir in people_dirs:
        full_dir_path = path.join(root_path, curr_dir)
        curr_person_images = [path.join(full_dir_path, f) for f in os.listdir(full_dir_path) if path.isfile(path.join(full_dir_path, f))]

        curr_person_label = curr_dir[1:]
        curr_img_index = 0
        for curr_image in curr_person_images:
            # 0 to load it in grayscale mode
            img = cv2.imread(curr_image, 0)

            # Transform image into vector
            img_vector = np.reshape(img, (1, img_dim))
            if curr_img_index < train_size:
                training_dataset[training_row_index] = img_vector
                training_labels[training_row_index] = float(curr_person_label)
                training_row_index += 1
            elif curr_img_index < (train_size + test_size):
                test_dataset[test_row_index] = img_vector
                test_labels[test_row_index] = float(curr_person_label)
                test_row_index += 1
            else:
                validation_dataset[validation_row_index] = img_vector
                validation_labels[validation_row_index] = float(curr_person_label)
                validation_row_index += 1
            curr_img_index += 1

    return training_dataset, test_dataset, validation_dataset, training_labels, test_labels, validation_labels


def mean_removal(dataset):
    # Calculate the mean vector, whereas each field is the mean of its corresponding column in the dataset
    mean = np.mean(dataset, axis=0)

    # Now subtract the mean vector from all of the rows in the matrix
    return dataset - mean


def calculate_eigen_vectors(A):
    # Small covariance matrix, A*Atranspose
    At = A.transpose()
    C = A.dot(At)

    # Get eigen values and eigen vectors of C
    # eigh sorts the eigen values in ascending order. We need descending order, hence we copy it in reverse order
    eigen_values, Um = np.linalg.eigh(C)
    eigen_values = eigen_values[::-1]
    Um = Um[:, ::-1]  # Each column is an eigen vector

    # Calculate the eigen values of covariant matrix by multiplying C's eigen vectors by Atranspose from left
    Wm = np.dot(At, Um)

    # Normalize the eigen vectors. Do this by getting normals for each vector (each column)
    np.seterr(divide='ignore', invalid='ignore')
    V = np.divide(Wm, np.linalg.norm(Wm, axis=0))

    return V


def optimize_eigen_faces(V, training_dataset, test_dataset, training_labels, test_labels):
    optimization_scores = []

    # Each iteration we will try to match using part of eigen vectors, this way we will find the optimal K value
    for i in range(V.shape[1]):
        # Each time we try with less eigen vectors. Note that each column is an eigen vector and we want to find K optimal eigen ones
        Vk = V[:, :V.shape[1] - i]
        Fa = training_dataset.dot(Vk)
        Fb = test_dataset.dot(Vk)

        # Now check, using euclidean distance (Norm 2), which vector is the closest one
        classified_labels = np.zeros(test_dataset.shape[0])
        for j in range(test_dataset.shape[0]):
            # Calculate distance vector. Use axis=1 to sum the columns in each row, according to the presentation.
            norm = np.sum((Fa - Fb[j, :])**2, axis=1)**0.5

            # Get the label of the closest vector. (based on the minimum distance)
            classified_labels[j] = training_labels[np.argmin(norm)]

        # Now, after test classification, rank it so we can choose optimization
        correct_percentage = float(np.count_nonzero(classified_labels == test_labels)) / float(test_dataset.shape[0])
        optimization_scores += [correct_percentage]

    return optimization_scores[::-1]

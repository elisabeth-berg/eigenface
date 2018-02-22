import imageio
import os
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def load_photos():
    photo_list = os.listdir('img')
    photo_list = [p for p in photo_list if p != '.DS_Store']
    n_samples = len(photo_list)
    pic = imageio.imread('img/{}'.format(photo_list[0]))
    (length, width) = pic.shape
    faces = np.zeros((n_samples, length*width))

    for i, photo in enumerate(photos[1:]):
        pic = imageio.imread('img/{}'.format(photo))
        pic = rgb2gray(pic)
        pic = pic.flatten()
        faces[i] = pic

    # Global centering
    faces_centered = faces - faces.mean(axis=0)
    # Center the columns
    faces_centered -= faces_centered.mean(axis=1).reshape(n_samples, -1)
    return faces_centered


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


def plot_eigenfaces(faces_centered, image_shape, subplot_dim):
    faces_pcd = PCA().fit(faces_centered)
    fig, axs = plt.subplots(subplot_dim[0], subplot_dim[1], figsize=(12, 6))
    for ax, i in zip(axs.flatten(), range(subplot_dim[0]*subplot_dim[1])):
        eigenface = faces_pcd.components_[i, :].reshape(image_shape)
        ax.imshow(eigenface, cmap=plt.cm.gray)
        ax.set_title("{}'th Eigenface".format(i))
        ax.set_xticks(())
        ax.set_yticks(())
    fig.tight_layout()


def plot_reconstructions(face_no, image_shape, subplot_dim):
    faces_pcd = PCA().fit(faces_centered)
    fig, axs = plt.subplots(subplot_dim[0], subplot_dim[1], figsize=(13, 6))
    for ax, dim in zip(axs.flatten(), range(subplot_dim[0]*subplot_dim[1])):
        reduced_data = reduce_face_data(dim)
        face = reduced_data[face_no].reshape(image_shape)
        ax.imshow(face, cmap=plt.cm.gray)
        ax.set_title("Face Reconstructed with {} PCA\nComponents".format(dim))
        ax.set_xticks(())
        ax.set_yticks(())
    fig.tight_layout()


def reduce_face_data(n_dim):
    faces_pcd = PCA().fit(faces_centered)
    eigenvalues = faces_pcd.components_[:n_dim, :].T
    faces_reduced = np.dot(np.dot(faces_centered, eigenvalues), eigenvalues.T)
    return faces_reduced

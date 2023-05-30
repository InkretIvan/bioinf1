from funkcije.helpers import transformData, distance, transformDataMedoids, writeJSON, saveImage
from Bio.Cluster import kcluster
import numpy as np
from Bio import Align
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
aligner = Align.PairwiseAligner()
aligner.mode = 'local'


def kmeans(sequences, filename):
    """
    Function performs k-means clustering (BioPython library) on the given sequences and saves the results and error values.

    Author:
    Mia Jurdana
    """
    matrix = transformData(sequences)
    results = []
    errors = []
    num_clusters = list(range(1, 11))
    for nclusters in num_clusters:
        clusterid, error, nfound = kcluster(
            matrix, nclusters=nclusters, mask=None, weight=None,  transpose=False, method='a', dist='e')
        result = {
            "nClusters": nclusters,
            "clusterId": clusterid.tolist(),
            "error": error,
            "solutionFound": nfound,
        }
        results.append(result)
        errors.append(error)
    writeJSON(results, "./results/json/" + filename)
    saveImage(num_clusters, errors, "./results/errors/" + filename)
    return results


def kmedoids(sequences, filename):
    """
    Function performs k-medoids clustering on the given sequences and saves the results and error values.

    Author:
    Ivan Inkret
    """
    matrix = transformDataMedoids(sequences)
    results = []
    errors = []
    num_clusters = list(range(1, 11))
    for nclusters in num_clusters:
        clusterid, error, nfound = kcluster(
            matrix, nclusters=nclusters, mask=None, weight=None,  transpose=False, npass=10, method='m', dist='e')
        result = {
            "nClusters": nclusters,
            "clusterId": clusterid.tolist(),
            "error": error,
            "solutionFound": nfound,
        }
        results.append(result)
        errors.append(error)
    writeJSON(results, "./results/json/" + filename)
    saveImage(num_clusters, errors, "./results/errors/" + filename)
    return results


def kmeansSklearn(sequences, filename):
    """
    Function performs k-means clustering (Scikit learn library) on the given sequences and saves the results and error values.

    Author:
    Mia Jurdana
    """
    errors = []
    results = []
    vectorizer = CountVectorizer(analyzer='char')
    X = vectorizer.fit_transform(sequences)
    num_clusters = list(range(1, 11))
    for k in num_clusters:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(X)
        result = {
            "nClusters": k,
            "error": kmeans.inertia_,
            "clusterId": kmeans.labels_.tolist(),
        }
        errors.append(kmeans.inertia_)
        results.append(result)
    writeJSON(results, "./results/json/" + filename)
    saveImage(num_clusters, errors, "./results/errors/" + filename)
    return results


def gaussianMixture(sequences, filename):
    """
    This function takes a list of sequences as input and returns a NumPy array containing the converted representation of each sequence.

    Author:
    Mia Jurdana
    """
    errors = []
    results = []
    num_clusters = list(range(1, 11))
    vectorizer = CountVectorizer(analyzer='char')
    X = vectorizer.fit_transform(sequences)
    for k in num_clusters:
        gmm = GaussianMixture(n_components=k)
        gmm.fit(X.toarray())
        labels = gmm.predict(X.toarray())
        error = np.sum(labels != labels[0]) / len(labels)
        result = {
            "nClusters": k,
            "error": error,
            "clusterId": labels.tolist(),
        }
        errors.append(error)
        results.append(result)
    writeJSON(results, "./results/json/" + filename)
    saveImage(num_clusters, errors, "./results/errors/" + filename)
    return results
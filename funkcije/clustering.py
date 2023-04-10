from Bio.Cluster import kcluster
import numpy as np
import json
import matplotlib.pyplot as plt

def transformData(sequences):
    return np.asarray([np.fromstring(s, dtype=np.uint8) for s in sequences])

def writeJSON(results, fileName):
    with open(fileName + ".json", "w") as outfile:
        json.dump(results, outfile)

def saveImage(x,y, fileName):
    plt.plot(x, y)
    plt.grid()
    plt.xlabel("Number of clusters")
    plt.ylabel("Error")
    plt.grid()
    plt.savefig(fileName + ".png")

def kmeans(sequences):
    matrix = transformData(sequences)
    results = []
    errors = []
    num_clusters = list(range(1, 11))
    for nclusters in num_clusters:
        clusterid, error, nfound = kcluster(matrix, nclusters=nclusters)
        result = {
            "nClusters" : nclusters,
            "clusterId": clusterid.tolist(),
            "error": error,
            "solutionFound": nfound,
        }
        results.append(result)
        errors.append(error)
    writeJSON(results, "kmeans_results")
    saveImage(num_clusters, errors, "kmeans_results")

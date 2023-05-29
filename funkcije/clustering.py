from Bio.Cluster import kcluster
import numpy as np
import json
import matplotlib.pyplot as plt
import Levenshtein
from Bio import Align

aligner = Align.PairwiseAligner()
aligner.mode = 'local'

tocno2="GAGCATCTTAAGGCCGAGTGTCATTTCTTCAACGGGACGGAGCGGATGCAGTTCCTGGCGAGATACTTCTATAACGGAGAAGAGTACGCGCGCTTCGACAGCGACGTGGGCGAGTTCCGGGAGCAGCACCGGGCAGAGGTGGACAGGTACTGCAGACACAACTACGGGGTCGGTGAGAGTGCGGTGACCGAGCTGGGGCGGCCGGACGCCAAGTACTGGAACAGCCAGAAGGAGATCCTGTTCACTGTG"

def transformData(sequences):
    #print(len(sequences))
    return np.asarray([np.fromstring(s, dtype=np.uint8) for s in sequences])

def distance(seq,seq2):
    ret=0
    for i,char in enumerate(seq):
        if seq[i]!=seq2[i]:
            ret=ret+1
    return ret

def transformDataMed(sequences): 
    arr=[]
    for i,s in enumerate(sequences):
        arr.append([])
        for c in s:
            if c=='A':
                arr[i].append(1)
            elif c=='D':
                arr[i].append(1)
            elif c=='G':
                arr[i].append(2)
            else:
                arr[i].append(2)
        
    return arr

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
        clusterid, error, nfound = kcluster(matrix, nclusters=nclusters, mask=None, weight=None,  transpose=False, method='a', dist='e')
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
    return results

def kmedoids(sequences): 
    matrix = transformDataMed(sequences)
    results = []
    errors = []
    num_clusters = list(range(1, 11))
    for nclusters in num_clusters:
        clusterid, error, nfound = kcluster(matrix, nclusters=nclusters, mask=None, weight=None,  transpose=False, npass=10, method='m', dist='e')
        result = {
            "nClusters" : nclusters,
            "clusterId": clusterid.tolist(),
            "error": error,
            "solutionFound": nfound,
        }
        results.append(result)
        errors.append(error)
    writeJSON(results, "kmedoids_results")
    saveImage(num_clusters, errors, "kmedoids_results")
    return results


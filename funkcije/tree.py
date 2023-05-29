from Bio.Seq import Seq
from Bio.Cluster import treecluster
import Levenshtein
import numpy as np

def transformData(sequences):

    return np.asarray([np.fromstring(s, dtype=np.uint8) for s in sequences])

def clus(sequences):

    arr=transformData(sequences)

    tree = treecluster(arr)
    print(tree)
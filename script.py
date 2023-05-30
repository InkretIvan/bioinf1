import os
import sys
import json
from funkcije.parse import selectSequences
from funkcije.clustering import kmeans
from funkcije.select_representative import findRepresentatives
from funkcije.count_representatives import count_representatives
from funkcije.helpers import writeJSON


def getResults():
    """
    Function performs data analysis and clustering on sequences extracted from files in the "data" directory.
    It retrieves the list of files in the "data" directory.
    For each file, it selects sequences based on certain criteria (similar lengths or most frequent lengths).
    It performs k-means clustering on the sequences.
    Representatives are identified for each cluster.
    The results, including the errors, number of clusters, and representatives are stored.

    Author:
    Ivan Inkret
    """
    files = os.listdir('data')
    results = []
    for file in files:
        filename = os.path.basename(file)[:-6]
        sequences = selectSequences(file)
        if len(sequences) < 15:
            continue
        result = kmeans(sequences, filename)
        n = 6
        clusterId = result[n-1]['clusterId']
        representatives = findRepresentatives(sequences, clusterId, n)
        print(len(representatives))
        result = {
            "fileName": file,
            "numClusters": len(representatives),
            "representatives": representatives,
        }
        results.append(result)
        print(file+" done")

    writeJSON(results, "results/project_results")


if __name__ == "__main__":
    """
    Running with the "-all" argument: This will execute the getResults() function, which processes all files in the "data" directory.
    To process a specific file, filename is passed as an argument.

    Author:
    Ivan Inkret
    """
    if len(sys.argv) > 1 and sys.argv[1] == "-all":
        getResults()
    else:
        inp = input("Unesi ime datoteke iz koje izvlačimo podatke: ")
        filename = inp[:-6]
        sequences = selectSequences(inp)
        result = kmeans(sequences, filename)

        n = 6
        clusterId = result[n-1]['clusterId']
        representatives = findRepresentatives(sequences, clusterId, n)

    count_representatives("./results/project_results.json")

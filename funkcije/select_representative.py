from collections import Counter


def findRepresentatives(sequences, clusterId, numOfClusters):
    """
    Function takes a list of sequences, their corresponding cluster IDs, and the total number of clusters. 
    Organizes the input sequences based on their cluster IDs, filters out sequences with low occurrences,
    identifies the most frequent sequence for each cluster, and returns a list of representative sequences.

    Author:
    Ivan Inkret
    """

    representatives = []
    seqById = []

    for i in range(numOfClusters):
        seqById.append([])

    for i, seq in enumerate(sequences):
        id = clusterId[i]
        seqById[id].append(seq)

    for s in seqById:
        if len(s) < 10:
            continue
        counts = Counter(s)
        mostOccurences = counts.most_common(1)[0]

        representative = mostOccurences[0]
        representatives.append(representative)

    return representatives


def findRepresentativesMsa(sequences, clusterId, numOfClusters):
    """
    Function takes a list of sequences, their corresponding cluster IDs, and the total number of clusters.
    It aims to find representative sequences for each cluster using a multiple sequence alignment (MSA) approach.

    Author:
    Ivan Inkret
    """

    representatives = []
    seqById = []

    for i in range(numOfClusters):
        seqById.append([])

    for i, seq in enumerate(sequences):
        id = clusterId[i]
        seqById[id].append(seq)

    for s in seqById:
        l = len(s)
        print(l)
        ls = len(s[0])

        rep = ""

        for i in range(ls):
            stupac = []
            for seq in s:
                stupac.append(seq[i])
            counts = Counter(stupac)
            mostOccurences = counts.most_common(1)[0]
            bp = mostOccurences[0]
            rep = rep+bp

        print(rep)
        print(len(rep))
        representatives.append(rep)

    return representatives
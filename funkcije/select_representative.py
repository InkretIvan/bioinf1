from collections import Counter


def findRepresentatives(sequences, clusterId,numOfClusters):
    representatives=[]
    seqById=[]

    for i in range(numOfClusters):
        seqById.append([])

    for i,seq in enumerate(sequences): #podijelimo sekvence svaku u svoje polje po pripadnosti nekom clusteru
        id=clusterId[i]
        seqById[id].append(seq)

    for s in seqById: #vracam najčešću sekvencu, ne koristim msa za sad
        counts = Counter(s)
        mostOccurences = counts.most_common(1)[0]
        print(mostOccurences[0])  # najčešća sekvenca
        representatives.append(mostOccurences[0])

    return representatives

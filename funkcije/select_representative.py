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
        #print(len(s))
        if len(s)<10:
            continue
        counts = Counter(s)
        mostOccurences = counts.most_common(1)[0]
        #print(mostOccurences[0])  # najčešća sekvenca

        representative=mostOccurences[0]#[27:-20]
        #print(representative)
        representatives.append(representative)

    return representatives

def findRepresentativesMsa(sequences, clusterId,numOfClusters): #wip

    representatives=[]
    seqById=[]

    for i in range(numOfClusters):
        seqById.append([])

    for i,seq in enumerate(sequences): #podijelimo sekvence svaku u svoje polje po pripadnosti nekom clusteru
        id=clusterId[i]
        seqById[id].append(seq)

    for s in seqById: 
        l=len(s) #broj sekvenci u clusteru
        print(l)
        ls=len(s[0]) #duljina sekvenci

        rep=""

        #zelimo demokratsku odluku za svaki stupac

        for i in range(ls):
            stupac=[]
            for seq in s:
                stupac.append(seq[i])
            counts = Counter(stupac)
            mostOccurences = counts.most_common(1)[0]
            bp=mostOccurences[0]
            rep=rep+bp

        print(rep)
        print(len(rep))
        representatives.append(rep)


    return representatives
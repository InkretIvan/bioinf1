from funkcije.parse import selectSequences
from funkcije.clustering import kmeans
from funkcije.testing import printMatrix
from funkcije.select_representative import findRepresentatives

def main():
    inp=input("Unesi ime datoteke iz koje izvlačimo podatke: ")
    sequences = selectSequences(inp)
    result=kmeans(sequences)
    
    ### idealni broj clustera, wip
    n=3
    ###

    clusterId=result[n-1]['clusterId']

    representatives=findRepresentatives(sequences,clusterId,n)

    printMatrix(representatives)


main()

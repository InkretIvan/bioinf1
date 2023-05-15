from funkcije.parse import selectSequences
from funkcije.clustering import kmeans
from funkcije.msa import findRepresentatives

def main():
    inp=input("Unesi ime datoteke iz koje izvlačimo podatke: ")
    sequences = selectSequences(inp)
    result=kmeans(sequences)
    
    ### idealni broj clustera, wip
    n=2
    ###

    clusterId=result[n-1].clusterId
    error=result[n-1].error

    representatives=findRepresentatives(sequences,clusterId)



    

main()

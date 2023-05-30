import os
import sys
import json
from funkcije.parse import selectSequences
from funkcije.clustering import kmeans, kmedoids
from funkcije.tree import clus
from funkcije.testing import printMatrix
from funkcije.select_representative import findRepresentatives, findRepresentativesMsa

from funkcije.count_representatives import count_representatives

def writeJSON(results, fileName):
    with open(fileName + ".json", "w") as outfile:
        json.dump(results, outfile)

def getResults():
    files=os.listdir('data')
    results=[]
    for file in files:
        sequences = selectSequences(file)
        if len(sequences) < 15: #ima neki problematični file za kojeg crasha jer je skoro prazni
            continue
        result=kmeans(sequences)
        n=6
        clusterId=result[n-1]['clusterId']
        representatives=findRepresentatives(sequences,clusterId,n)
        #print(len(representatives))
        result={
            "fileName": file,
            "numClusters": len(representatives),
            "representatives": representatives,
        }
        results.append(result)
        print(file+" done")

    writeJSON(results,"project_results")

def main():
    if(len(sys.argv)>1):
        if(sys.argv[1]=="-all"):
            getResults()
            return
        inp=sys.argv[1]
    else:                 
        inp=input("Unesi ime datoteke iz koje izvlačimo podatke: ")
    sequences = selectSequences(inp)
    result=kmeans(sequences)

    #clus(sequences)
    
    ### idealni broj clustera, wip
    n=6
    ###

    clusterId=result[n-1]['clusterId']

    representatives=findRepresentatives(sequences,clusterId,n)
    #representatives=findRepresentativesMsa(sequences,clusterId,n) #ovo radi gore za kmeans

    printMatrix(representatives)
    
    count_representatives("./project_results.json")


main()

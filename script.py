from funkcije.parse import selectSequences
from funkcije.clustering import kmeans

def main():
    inp=input("Unesi ime datoteke iz koje izvlačimo podatke: ")
    sequences = selectSequences(inp)
    kmeans(sequences)

main()

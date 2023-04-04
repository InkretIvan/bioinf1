from funkcije.parse import selectSequences

def main():
    inp=input("Unesi ime datoteke iz koje izvlačimo podatke: ")
    sequences = selectSequences(inp)

main()

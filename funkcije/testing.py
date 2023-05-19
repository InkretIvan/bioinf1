import pandas as pd
from Bio import Align


tocno1="GAGTATGCTAAGAGCGAGTGTCATTTCTCCAACGGGACGCAGCGGGTGCGGTTCCTGGACAGATACTTCTATAACCGGGAAGAGTACGTGCGCTTCGACAGCGACTGGGGCGAGTTCCGGGCGGTGACCGAGCTGGGGCGGCCGTCCGCCAAGTACTGGAACAGCCAGAAGGATTTCATGGAGCAGAAGCGGGCCGAGGTGGACACGGTGTGCAGACACAACTACGGGGTTATTGAGAGTTTCACTGTG"
tocno2="GAGCATCTTAAGGCCGAGTGTCATTTCTTCAACGGGACGGAGCGGATGCAGTTCCTGGCGAGATACTTCTATAACGGAGAAGAGTACGCGCGCTTCGACAGCGACGTGGGCGAGTTCCGGGAGCAGCACCGGGCAGAGGTGGACAGGTACTGCAGACACAACTACGGGGTCGGTGAGAGTGCGGTGACCGAGCTGGGGCGGCCGGACGCCAAGTACTGGAACAGCCAGAAGGAGATCCTGTTCACTGTG"
tocno3="ATGTATACTAAGAAAGAGTGTCATTTCTCCAACGGGACGCAGCGGGTGGGGCTCCTGGACAGATACTTCTATAACGGAGAAGAGTTCGTGCGCTTCGACAGCGACTGGGGCGAGTTCCGGGCGGTGACCGAGCTGGGGCGGCCGGCGGCCGAGGGCTGGAACAGCCAGAAGGAGCTCCTGGAGCAGAGGCGGGCCGCGGTGGACACGTACTGCAGACACAACTACGGGGTTATTGAGAGTTTCACTGTG"

aligner = Align.PairwiseAligner()
rows=[]
columns=['test_predstavnik_1','test_predstavnik_2','test_predstavnik_3']

tocni=[]
tocni.append(tocno1)
tocni.append(tocno2)
tocni.append(tocno3)

def printMatrix(representatives):
    
    #ispisuje edit distance (kao duljinu sekvence - alignment score) izmedu dobivenih i testnih predstavnika da si možemo brzo 
    #provjeriti za sve kombinacije clusteringa i biranja predstavnika.
    #npr. za kmeans sa 3 clustera i birenje najcesce zastupljenog predstavnika dobijem
    #
    #                        test_predstavnik_1  test_predstavnik_2  test_predstavnik_3
    #dobiveni_predstavnik_1                 0.0                53.0                20.0
    #dobiveni_predstavnik_2                 1.0                53.0                21.0
    #dobiveni_predstavnik_3                24.0                41.0                29.0
    #
    #znači dobiveni_1 je jednak testnom_1 i to je dobro ali ostali su loši.
    #nisam siguran da je to najbolji način za izračunati
    #ovo gore su podaci za jelen30

    matrica=[]

    for i,seq in enumerate(representatives):
        matrica.append([])
        rows.append('dobiveni_predstavnik_{0}'.format(i+1))

        for test in tocni:
            
            alignment = aligner.align(seq, test)[0]

            matrica[i].append(249-alignment.score)

    df = pd.DataFrame(matrica, columns = columns, index=rows)
    print(df)

    
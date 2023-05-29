import pandas as pd
from Bio import Align


tocno1="GAGTATGCTAAGAGCGAGTGTCATTTCTCCAACGGGACGCAGCGGGTGCGGTTCCTGGACAGATACTTCTATAACCGGGAAGAGTACGTGCGCTTCGACAGCGACTGGGGCGAGTTCCGGGCGGTGACCGAGCTGGGGCGGCCGTCCGCCAAGTACTGGAACAGCCAGAAGGATTTCATGGAGCAGAAGCGGGCCGAGGTGGACACGGTGTGCAGACACAACTACGGGGTTATTGAGAGTTTCACTGTG"
tocno2="GAGCATCTTAAGGCCGAGTGTCATTTCTTCAACGGGACGGAGCGGATGCAGTTCCTGGCGAGATACTTCTATAACGGAGAAGAGTACGCGCGCTTCGACAGCGACGTGGGCGAGTTCCGGGCGGTGACCGAGCTGGGGCGGCCGGACGCCAAGTACTGGAACAGCCAGAAGGAGATCCTGGAGCAGCACCGGGCAGAGGTGGACAGGTACTGCAGACACAACTACGGGGTCGGTGAGAGTTTCACTGTG"
tocno3="GAGCATCTTAAGGCCGAGTGTCATTTCTTCAACGGGACGGAGCGGATGCAGTTCCTGGCGAGATACTTCTATAACGGAGAAGAGTACGCGCGCTTCGACAGCGACGTGGGCGAGTTCCGGGAGCAGCACCGGGCAGAGGTGGACAGGTACTGCAGACACAACTACGGGGTCGGTGAGAGTGCGGTGACCGAGCTGGGGCGGCCGGACGCCAAGTACTGGAACAGCCAGAAGGAGATCCTGTTCACTGTG"
tocno4="ATGTATACTAAGAAAGAGTGTCATTTCTCCAACGGGACGCAGCGGGTGGGGCTCCTGGACAGATACTTCTATAACGGAGAAGAGTTCGTGCGCTTCGACAGCGACTGGGGCGAGTTCCGGGCGGTGACCGAGCTGGGGCGGCCGGCGGCCGAGGGCTGGAACAGCCAGAAGGAGCTCCTGGAGCAGAGGCGGGCCGCGGTGGACACGTACTGCAGACACAACTACGGGGTTATTGAGAGTTTCACTGTG"
aligner = Align.PairwiseAligner()
aligner.mode = 'local'
rows=[]
columns=['test_predstavnik_1','test_predstavnik_2','test_predstavnik_3','test_predstavnik_4']

tocni=[]
tocni.append(tocno1)
tocni.append(tocno2)
tocni.append(tocno3)
tocni.append(tocno4)

def printMatrix(representatives):
    
    #ispisuje edit distance (kao duljinu sekvence - alignment score) izmedu dobivenih i testnih predstavnika da si možemo brzo 
    #provjeriti za sve kombinacije clusteringa i biranja predstavnika.
    #npr. za kmeans sa 3 clustera i birenje najcesce zastupljenog predstavnika dobijem
    #                        test_predstavnik_1  test_predstavnik_2  test_predstavnik_3
    #dobiveni_predstavnik_1                 0.0                53.0                20.0
    #dobiveni_predstavnik_2                 1.0                53.0                21.0
    #dobiveni_predstavnik_3                24.0                41.0                29.0
    #
    #znači dobiveni_1 je jednak testnom_1 i to je dobro ali ostali su loši.
    #nisam siguran da je to najbolji način za izračunati
    #ovo gore su podaci za jelen30
    #
    # EDIT - daje malo bolje rez ak ne trimmam prije pocetak i kraj sekvenci nego on to sam napravi jer i tak radi lokalno poravnanje valjda
    #
    #                        test_predstavnik_1  test_predstavnik_2  test_predstavnik_3
    #dobiveni_predstavnik_1                 0.0                49.0                18.0
    #dobiveni_predstavnik_2                 1.0                49.0                19.0
    #dobiveni_predstavnik_3                23.0                39.0                26.0
    #
    #Za J29 ovo puno bolje radi, imamo 2 egzaktna glavna predstavnika
    #
    #                        test_predstavnik_1  test_predstavnik_2  test_predstavnik_3
    #dobiveni_predstavnik_1                11.0                 0.0                17.0
    #dobiveni_predstavnik_2                 1.0                12.0                21.0
    #dobiveni_predstavnik_3                 0.0                12.0                20.0
    #
    #

    matrica=[]

    for i,seq in enumerate(representatives):
        matrica.append([])
        rows.append('dobiveni_predstavnik_{0}'.format(i+1))

        for test in tocni:
            
            alignment = aligner.align(test,seq)[0]

            matrica[i].append(249-alignment.score)

    df = pd.DataFrame(matrica, columns = columns, index=rows)
    print(df)

    
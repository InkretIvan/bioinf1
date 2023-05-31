import numpy as np
import json
import matplotlib.pyplot as plt
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


def transformData(sequences):
    """
    This function takes a list of sequences as input and returns a NumPy array containing the converted representation of each sequence.

    Author:
    Mia Jurdana
    """
    return np.asarray([np.fromstring(s, dtype=np.uint8) for s in sequences])


def distance(seq, seq2):
    """
    Calculates the number of positions at which two sequences seq and seq2 differ. It assumes that both sequences have the same length.

    Author:
    Ivan Inkret
    """
    ret = 0
    for i, char in enumerate(seq):
        if seq[i] != seq2[i]:
            ret = ret+1
    return ret


def transformDataMedoids(sequences):
    """
    Converts a list of sequences into a numeric representation using a specific mapping for the characters 'A', 'D', 'G'.

    Author:
    Ivan Inkret
    """
    arr = []
    for i, s in enumerate(sequences):
        arr.append([])
        for c in s:
            if c == 'A':
                arr[i].append(1)
            elif c == 'D':
                arr[i].append(1)
            elif c == 'G':
                arr[i].append(2)
            else:
                arr[i].append(2)

    return arr


def writeJSON(results, fileName):
    """
    Takes a Python object results and writes it to a JSON file

    Author:
    Mia Jurdana
    """
    with open(fileName + ".json", "w") as outfile:
        json.dump(results, outfile)


def saveImage(x, y, fileName):
    """
    Generates and saves a line plot (error for different cluster sizes) as an image file in PNG format.

    Author:
    Mia Jurdana
    """
    plt.clf()
    plt.plot(x, y)
    plt.grid()
    plt.xlabel("Number of clusters")
    plt.ylabel("Error")
    plt.grid()
    plt.savefig(fileName + ".png")

def saveRepresentativesToFastq(representatives, filename):
    """
    Saves all generated sequence representatives of a given sample to a fastq file

    Author:
    Ivan Inkret
    """
    if representatives:
        seq_records = []
        for i,seq in enumerate(representatives):
            seq_obj = Seq(seq)
            seq_record = SeqRecord(seq_obj, id=""+str(i+1), description="representative_"+str(i+1))
            seq_records.append(seq_record)
        output = "results/representatives/"+filename+"_representatives.fasta"
        with open(output, "w") as f:
            SeqIO.write(seq_records, f, "fasta")
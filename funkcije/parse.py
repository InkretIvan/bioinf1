import statistics


def selectSequences(path):
    """
    The function reads a .fastq file from the specified path and returns a list of sequences.
    The sequences in the list have similar lengths if the tolerance is different from 0, 
    or they have the same length that occurs most frequently if the tolerance is set to 0.

    Author:
    Ivan Inkret
    """

    tolerance = 0
    data = []
    newData = []
    dataLen = []

    path = "data/"+path

    with open(path, "r") as f:
        while True:
            _ = f.readline()
            secondLine = f.readline().rstrip()
            _ = f.readline()
            _ = f.readline()

            if not secondLine:
                break

            data.append(secondLine)
            dataLen.append(len(secondLine))

    mode = statistics.mode(dataLen)

    for d in data:
        if (len(d) >= mode-tolerance) and (len(d) <= mode+tolerance):
            newData.append(d)

    return newData
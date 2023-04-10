import statistics

def selectSequences(path):
    """Provide a .fastq file and get a list of sequences with a similar length

    """

    tolerance=0 #Služi za podesiti količinu sekvenci koju želimo, ako je veća tolerancije teže bude ih poravnati

    data=[]
    newData=[]
    dataLen=[]

    path="data/"+path

    with open(path, "r") as f:
        while True:
            _ = f.readline()
            secondLine = f.readline().rstrip() #Jedina linija koja nas zanima
            _ = f.readline() 
            _ = f.readline()
            
            if not secondLine:
                break

            data.append(secondLine)
            dataLen.append(len(secondLine))
    
    print("Broj zapisa prije rezanja: ")
    print(len(data))

    mode = statistics.mode(dataLen) #vrijednost koja se pojavljuje najcesce

    #print(mode)

    for d in data:
        if (len(d)>=mode-tolerance) and (len(d)<=mode+tolerance):
            newData.append(d)
    
    print("Broj zapisa poslije rezanja: ")
    print(len(newData))

    return newData

  

        
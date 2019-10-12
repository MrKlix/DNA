
Eva = ["TGAAGGACCTTC", "AAAACCTCA", "TTAGCTATCGC", "TTGTGGTGGC", "AGGCCTCA"]
Larisa = ["TGAAGGACCTTC", "AAAACCTCA", "GCCAGTGCCG", "AAGTAGTGAC", "AGGCCTCA"]
Matej = ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"]
Miha = ["TGCAGGAACTTC", "AAAACCTCA", "GCCAGTGCCG", "GGGAGGTGGC", "GCCACGG"]

DNA = ["CCAGCAATCGC","GCCAGTGCCG", "TTAGCTATCGC", "GCCACGG", "ACCACAA", "AGGCCTCA", "TTGTGGTGGC", "GGGAGGTGGC",
       "AAGTAGTGAC", "TGAAGGACCTTC", "TGCAGGAACTTC", "AAAACCTCA", "CGACTACAG", "CGCGGGCCG"]

def findDna(criminal):
    summe = 0
    for value in DNA:
        with open('dna.txt') as f:
            if value in f.read() and value in criminal:
                summe += 20
                print("DNA " + value + " stimmt überein")
    return summe


percent = findDna(Miha)
print("Stimmt zu", percent, " % überein")



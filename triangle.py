import math


def main():
    print('Name : Ridwan Mubarok')
    print('Pascal Triangle')

    duds = buat(8)

    popu(duds)

    kiri(duds)
    print("")
    tengah(duds)



def buat(jumlahRow):
    duds = []
    for r in range(1, jumlahRow + 1):
        duds.append([0] * r)
    return duds

def popu(duds):
    for r in range(0, len(duds)):
        for c in range(0, len(duds[r])):
            duds[r][c] = math.factorial(r) / (math.factorial(c) * math.factorial(r - c))


def kiri(duds):
    for r in range(0, len(duds)):
        for c in range(0, len(duds[r])):
            print("%-4d" % duds[r][c], end="")
        print("")
    
           

def tengah(duds):

    inset = int(((((len(duds) * 2) - 1) / 2) * 3))

    for r in range(0, len(duds)):

        print(" " * inset, end="")

        for c in range(0, len(duds[r])):

            print("%-3d   " % duds[r][c], end="")

        print("")

        inset-= 3




main()
from collections import OrderedDict 

def main():
    masalah = 'alagcgcdodol'
    print(remove_duplikat(masalah))


def remove_duplikat(masalah):
    return ''.join(OrderedDict.fromkeys(masalah)) 

        

main()
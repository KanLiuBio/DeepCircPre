def DNA_one_hot(seq):
    '''
    This function encodes the nucleotide {A,C,G,T,N} into one-hot vector. 
    A or a: 10000
    C or c: 01000
    G or g: 00100
    T or t (U or u for RNA): 00010
    N or a: 00001
    seq: string of DNA nucleotides.
    '''

    one_hot=''
    seq=str(seq)
    seq_size=len(seq)

    for i in range (seq_size):
        if seq[i] == 'A' or seq[i] == 'a':
            one_hot=one_hot + '10000'
        elif seq[i] == 'C' or seq[i] == 'c':
            one_hot=one_hot + '01000'
        elif seq[i] == 'G' or seq[i] == 'g':
            one_hot=one_hot + '00100'
        elif seq[i] == 'T' or seq[i] == 't' or seq[i] == 'U' or seq[i] == 'u':
            one_hot=one_hot + '00010'
        elif seq[i] == 'N' or seq[i] == 'n':
            one_hot=one_hot + '00001'
        else:
            print ("Unknown nucleotide found besides: A, C, G, T(U) or N.")
    return one_hot


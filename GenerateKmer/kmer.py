string=raw_input('Enter string:')
kmer_size=input('Kmer_size: ')

print 'Total kmers: ', len(string)-kmer_size+1

for i in range(0,len(string)-kmer_size+1):
    string=list(string)
    kmer=''.join(string[i:i+kmer_size])
    print kmer


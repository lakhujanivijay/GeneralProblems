The term k-mer typically refers to all the possible substrings of length k that are contained in a string. In computational genomics, k-mers refer to all the possible subsequences (of length k) from a read obtained through DNA Sequencing. The amount of k-mers possible given a string of length, L, is L-k+1 whilst the number of possible k-mers given n possibilities (4 in the case of DNA e.g. ACTG) is n^{k}. K-mers are typically used during sequence assembly,[1] but can also be used in sequence alignment. In the context of the human genome, k-mers of various lengths have been used to explain variability in mutation rates

In sequence assembly, k-mers are typically used during the construction of De Bruijn graphs. In order to create a De Bruijn Graph, the strings stored in each edge with length, L, must overlap another string in another edge by L-1 in order to create a vertex

Source: https://en.wikipedia.org/wiki/K-mer

Given a string of certain length and user defined kmer-size, this script gives all possible kmers along with total number of k-mers generated.


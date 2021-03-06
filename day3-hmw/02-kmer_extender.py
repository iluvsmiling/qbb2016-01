#!/usr/bin/env python
"""
Input: xxx.py subset.fa droYak_query.fa k
Output: kmer_seq, sorted
"""
import sys
import fasta_fixed

###
target = open(sys.argv[1]) 
query = open(sys.argv[2])
k_len = int(sys.argv[3])
#stringg = str(sys.argv[4])


query_start = {}
for ident, sequence in fasta_fixed.FASTAReader(query):
    sequence = sequence.upper()
    q_pos = sequence
    for j in range(0, len(sequence) - k_len):
        kmer = sequence[j: j+k_len]
        #if kmer not in query_start:
        #print kmer
        if not query_start.get(kmer,0):
            query_start[kmer] = j


kmer_extend = []
m=0
for ident, sequence in fasta_fixed.FASTAReader(target):
    sequence = sequence.upper()
    t_pos = sequence
    for i in range(0, len(sequence)-k_len):
        if m>0:
            m-=1
            continue    
        kmer = sequence[i : i+k_len]
        longest_kmer=sequence[i : i+k_len]
        t_start = i
        #print kmer, t_start
        #t_end = i + k
        
        if kmer in query_start:
            m=0
            
            while query_start[kmer] + k_len - 1 < len(q_pos) and t_start + k_len +m+3 < len(t_pos):
                m+=1
                if q_pos[query_start[kmer]+k_len+m] == t_pos[i+k_len+m]:
                    #print q_pos[query_start[kmer]+k_len+m], t_pos[i+k_len+m]
                    longest_kmer+=q_pos[query_start[kmer]+k_len+m]
                    
                else:
                    #print longest_kmer
                    m=m-1
                    break
                kmer_extend.append(longest_kmer)
print '\n'.join(sorted (kmer_extend, reverse = True, key=len))
                #print sorted(kmer_extend, reverse=True, key=len)
                #print kmer_extend.sort(...)
            #print '\n'.join(sorted(kmer_extend, reverse=True, key=len))



            

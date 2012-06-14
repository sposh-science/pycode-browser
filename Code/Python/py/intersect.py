def intersect(seq1,seq2):
    result=[]
    for x in seq1:
	if x in seq2:
	   result.append(x)
    return result

if __name__=='__main__':
    a=(1,2,3,4)
    b=(3,4,5,6)
    print intersect(a,b)	
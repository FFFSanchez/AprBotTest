from itertools import permutations
import sys

from time import perf_counter

def average_time(n, perm):
    start = perf_counter()
    perm(n)
    end = perf_counter()
    return (end - start)



def perm(n):

	l = [0 for _ in range(n)] + list(range(1, n + 1))

	#print(l)
	with open('output.txt', 'w', encoding='utf8') as f:
		for i in permutations(l):
			print(i, file=f)
	return 'ready!'

if __name__ == "__main__":
    if len (sys.argv) > 1:
        print('Loading...')
        #print(perm(int(sys.argv[1])))
        print(average_time(int(sys.argv[1]), perm))
    else:
        print ("Enter N parameter")
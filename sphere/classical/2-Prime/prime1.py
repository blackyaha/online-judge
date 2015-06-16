#!usr/bin/env python3

def is_prime(n):
	if n <= 1:
		return 
	
	for i in range(2, n):
		if i ** 2 <= n:
			if n % i == 0:
				return
	print(n)

def prime_brute(n):
	if n <= 1:
		return
	for i in range(2, n):
		if n % i == 0:
			return
	print(n)
            
def input_case():           
	while(True):
		x = int(input())
		if x in range(1, 11):
			return x

def input_num(x):
	n_list = []
	m_list = []
	c = 0
	while(True):
		line = input()
		(m, n) = line.split(" ")
		m = int(m)
		n = int(n)
		if (m >= 1 and m < 1000000000) and (n >= 1 and n < 1000000000):
			if (n > m) and (n - m) <= 100000:
				n_list.append(n)
				m_list.append(m)
				c += 1
			elif (m > n) and (m - n) <= 100000:
				n_list.append(m)
				m_list.append(n)
				c += 1
				
		if c == x:
			return(n_list, m_list)
				

n = int(input_case())
(nl, ml) = input_num(n)

for i in range(n):
	for j in range(ml[i], nl[i] + 1):
		is_prime(j)
		#prime_brute(j)
	print(" ")



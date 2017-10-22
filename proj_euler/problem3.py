import math

TOP_NUM = 600851475143
# TOP_NUM = 13195  # Debug
# TOP_NUM = 10  # Debug
TOP_NUM_INDEX = TOP_NUM + 1

def is_prime(num):
	num_sqrt_floor = math.floor(math.sqrt(num))

	if num > 9:
		last_digit = int(str(num)[-1])
		if last_digit == 0 or last_digit == 2 or last_digit == 5:
			return False
		elif last_digit % 2 == 0:
			return False
		else:
			for i in range(2, num_sqrt_floor, 1):
				if num % i == 0:
					return False
			return True

	elif num in [2, 3, 5, 7]:
		return True

	else:
		return False

if __name__ == '__main__':
	for i in range(math.floor(math.sqrt(TOP_NUM)), 2, -1):
		print("Checking %d..." % i)  # Debug
		if TOP_NUM % i != 0:
			print("  Not a factor of top num! Moving on...")
			continue
		else:
			# print(is_prime(i))  # Debug
			if is_prime(i):
				print("**DING! Answer is: %d" % i)
				break
			else:
				print("  Non-prime factor. Moving on...")
				continue

#
# Ditched exploratory code
#
# def is_prime(num):
# 	if num > 10:
# 		last_digit = int(str(num)[-1])
# 		if last_digit == 0 or last_digit == 2 or last_digit == 5:
# 			return False
# 		elif last_digit % 2 == 0:
# 			return False
# 		else:
# 			has_factor = None
# 			for i in range(2, num):
# 				# print("\t**Checking %d whether factor..." % i)  # Debug
# 				if num != i and num % i == 0:
# 					has_factor = True
# 					return False
# 			if not has_factor:
# 				return True
# 	elif num < 10:  # Shouldn't matter, but just for completeness...
# 		factors = []
# 		for i in range(2, 10):
# 			for j in range(2, 10):
# 				if i % j == 0:
# 					factors.append(j)
# 			if len(factors) == 1:
# 				return True

# if __name__ == '__main__':
	# for i in range(TOP_NUM - 1, 1, -1):
	# 	i = i

	# print("done.")
	# for i in range(TOP_NUM - 1, 1, -1):
	# 	# print("Checking %d..." % i)  # Debug
	# 	if TOP_NUM % 2 != 0:  # If odd, skip even numbers
	# 		if i % 2 == 0:
	# 			continue
	# 		else:
	# 			if TOP_NUM % i == 0:
	# 				if is_prime(i):
	# 					print("Largest prime factor of %d is %d." % (TOP_NUM, i))
	# 					break
	# 			else:
	# 				# print("\tNot prime!")  # Debug
	# 				print("\t%d is not a factor!" % i)  # Debug
	# 				continue

	# 	else:
	# 		if TOP_NUM % i == 0:
	# 			if is_prime(i):
	# 				print("Largest prime factor of %d is %d." % (TOP_NUM, i))
	# 				break
	# 		else:
	# 			# print("\tNot prime!")  # Debug
	# 			print("\t%d is not a factor!" % i)  # Debug
	# 			continue

# # SLOW for 13195!
# # def generate_primes_in_range():
# # 	primes = []  # Seed with first prime number
# # 	tn_index = TOP_NUM + 1
# # 	for i in range(2, tn_index):
# # 		factors = []
# # 		i_index = i + 1
# # 		for j in range(2, i_index):
# # 			if i % j == 0:
# # 				factors.append(j)
# # 		# print("Num: %d\tFactors:%s" % (i, factors))  # Debug
# # 		if len(factors) == 1:
# # 			primes.append(i)
# # 	return primes

# def generate_primes_in_range():
# 	primes = []
# 	potential_primes = []
# 	# Generate numbers in range
# 	for i in range(2, TOP_NUM_INDEX):
# 		# If it's a >2 digit number, examine the last digit
# 		if i > 10:
# 			str_i = str(i)
# 			last_digit = int(str_i[len(str_i) - 1])	
# 			if is_prime_candidate_per_last_digit(last_digit):
# 				potential_primes.append(i)
# 		# If it's a <2 digit number, do more granular check
# 		if i < 10:
# 			factors = []
# 			for j in range(2, 10):
# 				if i % j == 0:
# 					factors.append(j)
# 			if len(factors) == 1:
# 				primes.append(i)

# 	# Check the potential primes for actual prime numbers
# 	for potential_prime in potential_primes:
# 		found_factor = None

# 		for inner_potential_prime in potential_primes:
# 			factors = []
# 			if inner_potential_prime < potential_prime:
# 				if potential_prime % inner_potential_prime == 0:
# 					found_factor = True
			
# 		if not found_factor:
# 			primes.append(potential_prime)

# 	return primes

# def is_prime_candidate_per_last_digit(num):
# 	if num == 0 or num == 2 or num == 5:
# 		return False
# 	elif num % 2 == 0:
# 		return False
# 	else:
# 		return True

# # print(generate_primes_in_range())  # Debug

# # primes_in_range = generate_primes_in_range()
# # # prime_factors_of_top_num = []
# # largest_prime_factor_of_top_num = None

# # for prime in primes_in_range:
# # 	if TOP_NUM % prime == 0 and largest_prime_factor_of_top_num and prime > largest_prime_factor_of_top_num:
# # 		largest_prime_factor_of_top_num = prime
# # 	elif TOP_NUM % prime == 0 and largest_prime_factor_of_top_num is None:
# # 		largest_prime_factor_of_top_num = prime

# # largest_prime_factor = prime_factors_of_top_num[len(prime_factors_of_top_num) - 1]

# primes_in_range = generate_primes_in_range()
# primes_in_range.sort(reverse=True)
# largest_prime_factor_of_top_num = None

# for prime in primes_in_range:
# 	if TOP_NUM % prime == 0:
# 		largest_prime_factor_of_top_num = prime
# 		break  # We stop as soon as we find the largest prime number
# 	else:
# 		print("\tNot a prime factor... %d" % prime)

# print("Largest prime factor of %d is %d." % (TOP_NUM, largest_prime_factor_of_top_num))
import time
#dic={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

t0=time.time()
a="bba"
temp={}
for i in a:
    if i not in temp:
        temp[i]=1
    else:
        temp[i]+=1
for key,value in temp.items():
    if ord(key)-96!=value:
        print(False)
        break
else:
    print(True)
print(time.time()-t0)
"""# Python3 program for the above approach
import time
# Function to check whether the
# string is super ASCII or not
def checkSuperASCII(s):
	
	# Stores the frequency count
	# of characters 'a' to 'z'
	b = [0 for i in range(26)]

	# Traverse the string
	for i in range(len(s)):
		
		# AscASCIIii value of the
		# current character
		index = ord(s[i]) - 97 + 1;

		# Count frequency of each
		# character in the string
		b[index - 1] += 1

	# Traverse the string
	for i in range(len(s)):
		
		# ASCII value of the current
		# character
		index = ord(s[i]) - 97 + 1

		# Check if the frequency of
		# each character in string
		# is same as ASCII code or not
		if (b[index - 1] != index):
			print("No")
			return

	# Else print "Yes"
	print("Yes")

# Driver Code
if __name__ == '__main__':
	s = "bba"
	t0=time.time()
	checkSuperASCII(s)
	print(time.time()-t0)
"""
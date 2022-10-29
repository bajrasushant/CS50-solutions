# Python3 program to implement
# the above approach

# Function to count the maximum
# consecutive occurrence of the
# string str2 in the string str1
def maxRepeating(str1, str2):

	# Stores the count of consecutive
	# occurrences of str2 in str1
	cntOcc = str1.count(str2)

	# Concatenate str2 cntOcc times
	Contstr = str2 * cntOcc


	# Iterate over the string str1
	# while Contstr is not present in str1
	while(Contstr not in str1):

		# Update cntOcc
		cntOcc -= 1

	# Update Contstr
		Contstr = str2 * cntOcc

	return cntOcc

# Driver Code
if __name__ =="__main__":
str1 = "abababc"
str2 = "ba"
print(maxRepeating(str1, str2))


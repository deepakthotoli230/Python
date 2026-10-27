#  0,1 binary numbers

# 8,4,2,1 method
 
# 2^3  2^2  2^1  2^0
#  8    4    2    1
#  0    0    0    0 = 0
#  0    0    0    1 = 1
#  0    0    1    0 = 2
#  0    0    1    1 = 3

# Bitwise And operator(&)

# T T
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1

print(5&3)

# Bitwise OR (|)

# T T
# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 1
# 1 | 1 = 1

print (5|3)

# Bitwise NOT (~)

#  n = -(n+1)

print(~4)
print (~-4)
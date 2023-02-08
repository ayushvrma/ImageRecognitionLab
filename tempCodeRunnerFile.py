
# r2 = int(input())

# s1 = int(input())
# s2 = int(input())


# num_channels = (2**8)-1
# alpha = s1-0/(r1-0)
# beta = s2-s1/(r2-r1)
# gamma = num_channels-s2/(num_channels-r2)

# s = []

# for i in range(num_channels+1):
#     if i<r1:
#         s[i] = alpha*i
#     elif i<r2:
#         s[i] = beta*(i-r1) + s1
#     else:
#         s[i] = gamma * (i-r2) + s2


# s = np.round(s).astype(np.uint8)
pattern_size = int(input("Enter the size of the pattern: "))
i = 0
while i<pattern_size:
    for _ in range(pattern_size):
        print("*", end="")
    print("\n")
    i+=1    	



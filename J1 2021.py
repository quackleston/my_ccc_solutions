#1 = above sea level
#-1 = below

waterB = int(input())
formula = 5 * waterB - 400
print(formula)

if(formula < 100 and waterB < 100):
    print(1)
elif(formula > 100 and waterB > 100):
    print(-1)
else:
    print(0)

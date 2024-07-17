height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
avg = 0
v = 0
for i in range(0,len(height)):
    avg += height[i]
v = avg/len(height)
print(v)
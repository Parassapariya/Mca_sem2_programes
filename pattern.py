# 1
# 0 1
# 0 1 0
# 1 0 1 0
# 1 0 1 0 1

# odd even 0 and 1 loop print in pyramid python
rows = 5

for i in range(1, rows + 1):
    toggle = i % 2
    for j in range(1, i + 1):
        print(toggle, end=" ")
        toggle = 1 - toggle
    print()







"""                  
n=5

for i in range(1, n+1):
        row = ''
        for j in range(1,i+1):
            row += str(j % 2) + ' '
        print(row)

"""




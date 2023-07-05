line = float(input("Enter your number: "))
round(line, 2)
line = str(line)
line = line.split('.')
line[1] = line[1][:2]
line[0] = line[0][::-1]
n = len(line[0]) // 3
k = ''
for i in range(n):
    k += line[0][3 * i:3 * i + 3] + ","
if len(line[0]) % 3 == 0:
    k = k[:len(k) - 1]
else:
    k += line[0][n * 3:len(line[0])]
line[0] = k[::-1]
new_line = line[0] + "." + line[1]
print(new_line)

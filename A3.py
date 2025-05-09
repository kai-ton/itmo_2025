sm = cnt = 0

with open('CdSe_CdZnS Core_Shell.txt') as f:
    for s in f.readlines():
        sm += float(s.split()[1].replace(',', '.'))
        cnt += 1

print(sm/cnt)
# Ответ: 8.506962025316456

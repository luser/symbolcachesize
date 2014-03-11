import csv
import sys

lines = list(csv.reader(open(sys.argv[1], "rb")))
totalhits = float(sum(int(x[0]) for x in lines))
percent = int(sys.argv[2])
n = 0
cachesize = 0
for count, path, size in lines:
    n += int(count)
    cachesize += int(size)
    if 100 * n / totalhits >= percent:
        break

print "%d%% (%d) = %d bytes" % (percent, (percent/100.0 * totalhits), cachesize)

import sys
recall = float(sys.argv[1])/100
precision = float(sys.argv[2])/100

print 2.0/(1 / recall + 1 / precision)


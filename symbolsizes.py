import csv
import os
import sys

d = "/mnt/netapp/breakpad/"
dirs = []
for x in os.listdir(d):
  full = os.path.join(d, x)
  if os.path.isdir(full):
    dirs.append(full)

with open(sys.argv[2], "wb") as of:
    out = csv.writer(of)
    missing = csv.writer(open("/tmp/missing.csv", "wb"))
    for line in csv.reader(open(sys.argv[1], "rb")):
      debug_file, debug_id, count = line
      for dir in dirs:
        path = os.path.join(dir, debug_file, debug_id)
        if debug_file.endswith(".pdb"):
            path = os.path.join(path, debug_file.replace(".pdb",".sym"))
        else:
            path = os.path.join(path, debug_file + ".sym")
        if os.path.exists(path):
          out.writerow([count, path, os.stat(path).st_size])
          break
      else:
          missing.writerow([count, debug_file, debug_id])
          print "No file found for %s/%s" % (debug_file, debug_id)

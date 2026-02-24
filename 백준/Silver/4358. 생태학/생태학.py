import sys

trees = {}
total = 0

for line in sys.stdin:
    name = line.strip()
    if name == "":
        continue
    total += 1 
    trees[name] = trees.get(name,0)+1 

for name in sorted(trees.keys()) :
    percent = trees[name] / total * 100
    print(f"{name} {percent:.4f}")
    
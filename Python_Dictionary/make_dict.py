dict={}
with open("out_1.txt") as file1:
    for line in file1:
        line=line.strip().split("\t")
        if line[0] in dict:
            dict[line[0]].append(line[1])
        else:
            dict[line[0]] = [line[1]]        
for k,v in dict.items():
    print k, ", ".join(v)

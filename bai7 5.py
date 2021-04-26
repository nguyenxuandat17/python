def file read(fname):
    from itertools import islice
    with open(fname,"w") as myfile:
        myfile.write("python exercise\n")
        myfile.write("java exercise")
    txt = open(fname)
    print(txt.read())
file_read('abc.txt')
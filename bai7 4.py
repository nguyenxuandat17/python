def file_reead_from_head(fname, nlines):
    from itertools import islice
    witn open(fname) as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head('tesst.txt',2)
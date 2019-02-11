import os
fpath = r"C:\Users\ryman\Documents\3. Winter A 2019\4. TO 640"

for froots, fdirs, ffiles in os.walk(fpath):
    print(ffiles)

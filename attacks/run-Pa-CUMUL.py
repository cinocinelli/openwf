import subprocess
from loaders import *
r = sys.argv[1]  #run 20 or 1000
options = load_options("options"+r)
for i in range(10):
    options["CORE_NAME"] = str(i)
    options["FOLD_NUM"] = str(i)
    write_options("options"+r+"-" + str(i), options)
    cmd = "python Pa-CUMUL.py options"+r+"-" + str(i)
    subprocess.Popen(cmd, shell=True)

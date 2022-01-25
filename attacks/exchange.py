import os
#cell_add ='..\\cellss'
cell_add ='../cellss'
def replace(file, old_content, new_content):
    content = read_file(file)
    content = content.replace(old_content, new_content)
    rewrite_file(file, content)

def read_file(file):
    with open(file) as f:
        read_all = f.read()
        f.close()

    return read_all

def rewrite_file(file, data):
    with open(file, 'w') as f:
        f.write(data)
        f.close()


for f in os.listdir(cell_add):
    print(f)
    replace(os.path.join(cell_add,f), ' ', '\t')
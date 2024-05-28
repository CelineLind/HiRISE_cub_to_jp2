import os

# NOTE: do the below:
# conda environments which need to be created and stacked: https://hiproc.readthedocs.io/en/latest/installation.html
# conda activate isis
# conda activate --stack hiproc

# get all .IMG files in a folder and pair up [[], [], ..., []]
folder = "imgs" # NOTE: change to your folder name/location
file_names = []

for count, filename in enumerate(os.listdir(folder)):
    src =f"{folder}/{filename}"
    file_names.append(src)#[:-4])

file_names = sorted(file_names)
files = []
for i, item in enumerate(file_names):
    if '.IMG' in item and (i+1 != len(file_names)):
        if item[:-6] == file_names[i+1][:-6]:
            files.append([item[5:], file_names[i+1][5:]])

# run EDR_Stats on each pair
for pair in files:
    print(pair)
    os.system("EDR_Stats -v imgs/"+str(pair[0])+" -o outs/"+str(pair[0][:-4])+".cub")
    os.system("EDR_Stats -v imgs/"+str(pair[1])+" -o outs/"+str(pair[1][:-4])+".cub")

# Run HiCal on each pair
for pair in files:
    print(pair)
    print("HiCal -v outs/"+str(pair[0][:-4])+".cub outs/"+str(pair[0][:-4])+".HiCat.json")
    print("HiCal -v outs/"+str(pair[1][:-4])+".cub outs/"+str(pair[1][:-4])+".HiCat.json")


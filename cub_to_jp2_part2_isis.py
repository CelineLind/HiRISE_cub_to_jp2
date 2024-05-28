import os

# NOTE: do the below:
# conda deactivate

# get file names
folder = "outs" # NOTE: change to output folder for your images
file_names = []

for count, filename in enumerate(os.listdir(folder)):
    src =f"{folder}/{filename}"
    file_names.append(src)

file_names = sorted(file_names)
files = []
for i, item in enumerate(file_names):
    if '.cub' in item and (i+1 != len(file_names)):
        if item[:-6] == file_names[i+1][:-6]:
            files.append([item[5:], file_names[i+1][5:]])

# HiStitch from pairs
new_filenames = []
print("histitch")
for pair in files:
    print(pair)
    new_file_name = str(pair[0][:-4])+"_stitched.cub"
    new_filenames.append(new_file_name)
    os.system("histitch from1=outs/"+str(pair[0])+" from2=outs/"+str(pair[1])+" to=outs/"+str(new_file_name))

# Cubenorm
print("cubenorm")
final_filenames = []
for file in new_filenames:
    out_name = str(file[:-4])+"_norm.cub"
    final_filenames.append(out_name)
    os.system("cubenorm from=outs/"+str(file)+" to=outs/"+str(out_name)+" format=PVL")

# Save as JP2
print("jp2")
for file in final_filenames:#[:4]:
    # name = str(file[:-4])+".jp2"
    # os.system("isis2std from=outs/"+str(file)+" to=jp2s/"+str(name)+" format=jp2")
    name = str(file[:-4])+".jpg"
    os.system("isis2std from=outs/"+str(file)+" to=jp2s/"+str(name)+" format=jpeg")

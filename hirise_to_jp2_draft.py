# INSTRUCTIONS:
# conda environments which need to be created and stacked: https://hiproc.readthedocs.io/en/latest/installation.html

# conda activate isis
# conda activate --stack hiproc

import os

####

# run hi2isis
# os.system("hi2isis from=imgs/ESP_068294_1985_RED0_0.IMG to=outs/ESP_068294_1985_RED0_0.cub")
#os.system("hi2isis from=imgs/ESP_068294_1985_RED0_1.IMG to=outs/ESP_068294_1985_RED0_1.cub")

# run hiclean
# os.system("hical from=outs/ESP_068294_1985_RED0_0.cub to=outs/ESP_068294_1985_RED0_0_callib.cub")

##

# run histitch which uses hiproc 
# os.system("HiStitch -v outs/ESP_068294_1985_RED0_0.HiCal-230325143848.hical.cub outs/ESP_068294_1985_RED0_1.HiCal-230325143859.hical.cub") # --db outs/ESP_068294_1985_RED0_0.HiCat.json --db2 outs/ESP_068294_1985_RED0_1.HiCat.json
# os.system("HiStitch -v outs/ESP_068294_1985_RED0_0.HiCal-230325143848.cub outs/ESP_068294_1985_RED0_1.HiCal-230325143859.cub") # --db outs/ESP_068294_1985_RED0_0.HiCat.json --db2 outs/ESP_068294_1985_RED0_1.HiCat.json

#####

# run EDR_Stats which uses hiproc
# os.system("EDR_Stats -v imgs/ESP_068294_1985_RED0_0.IMG -o outs/ESP_068294_1985_RED0_0.cub")
# os.system("EDR_Stats -v imgs/ESP_068294_1985_RED0_1.IMG -o outs/ESP_068294_1985_RED0_1.cub")

# run hical which uses hiproc
# os.system("HiCal -v outs/ESP_068294_1985_RED0_0.cub 'imgs/ESP_068294_1985_RED0_0.HiCat.json'")
# os.system("HiCal -v outs/ESP_068294_1985_RED0_1.cub 'imgs/ESP_068294_1985_RED0_1.HiCat.json'")

# conda deactivate - back to just isis

# os.system("histitch from1=outs/ESP_068294_1985_RED0_0.HiCal-230325143848.cub from2=outs/ESP_068294_1985_RED0_1.HiCal-230325143859.cub to=histitchoutputcube.cub")
# os.system("histitch from1=outs/ESP_068294_1985_RED0_0.HiCal-230325143848.hical.cub from2=outs/ESP_068294_1985_RED0_1.HiCal-230325143859.hical.cub to=histitchoutputcube.hical.cub")

# maybe run cubenorm
# os.system("cubenorm from=histitchoutputcube.cub to=histitchoutputcubeNORM.cub format=PVL")

# run spaceinit
# os.system("spiceinit from=histitchoutputcubeNORM.cub web=true")
# os.system("spiceinit from=histitchoutputcube.cub web=true")

# run camp2map

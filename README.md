# HiRISE cub files -> JPEG2000 files

## How  
1. Locate an image on HiRISE (https://www.uahirise.org/hiwish/browse)  
    * For example: https://www.uahirise.org/PSP_003798_1985  
2. On the right-hand side, click EDR products
3. Download the relevant images (for example, all the RED images)
4. Place in a folder, perhaps with this repository
5. Open up *cub_to_jp2_part1_hiproc.py*

The process of converting these .IMG files into JPEG2000s (aka, mimicking the process that turns them into the JP2 outputs already on the HiRISE website) has been split between two files: part 1 and part 2.  
*Why?* It didn't want to work in one go and I was a tired honours student just wanting to get *something* working.

6. Setup your environments - you need to stack 2 virtual environments:
    1. Conda environments which need to be created and stacked: https://hiproc.readthedocs.io/en/latest/installation.html
    2. run `conda activate isis`
    3. run `conda activate --stack hiproc`
6. Change the value of *folder* in *cub_to_jp2_part1_hiproc.py* to where your images are saved  
7. Run Part 1: *cub_to_jp2_part1_hiproc.py*
8. run `conda deactivate`  
9. Open *cub_to_jp2_part2_hiproc.py* and change the output folder location for your image(s)
10. Run Part 2: *cub_to_jp2_part2_hiproc.py*

Congrats, you now repeated the process of turning the EDR products into JPEG2000 images.  
https://hiproc.readthedocs.io will be your best friend for any additional troubleshooting.  
Or, see the hirise_to_jp2_draft.py file where I attempted to do part 1 and part 2 in one file, but couldn't get it to work, so split it into two files instead. 

## What  
.IMG EDR files from HiRISE into a single, combined JPEG2000 image.

## Why  
Because you want to repeat the process that creates the JPEG2000 images that HiRISE already kindly provide on the UoA website. Or, because like me in 2023, you didn't realise that's what the output of this would be (an identical image instead of perhaps one composed of additional layers... *sigh*).

# When  
I wrote this in 2023 during my honours thesis. I tidied this code in 2024.

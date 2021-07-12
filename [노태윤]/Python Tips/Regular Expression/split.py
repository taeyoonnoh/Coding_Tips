import re

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

new_files = [re.split('([0-9]+)',file) for file in files]

# new_files 
'''
[['img', '12', '.png'],
 ['img', '10', '.png'],
 ['img', '02', '.png'],
 ['img', '1', '.png'],
 ['IMG', '01', '.GIF'],
 ['img', '2', '.JPG']]
'''

new_files = [re.split('[0-9]+',file) for file in files]
'''
[['img', '.png'],
 ['img', '.png'],
 ['img', '.png'],
 ['img', '.png'],
 ['IMG', '.GIF'],
 ['img', '.JPG']]
'''

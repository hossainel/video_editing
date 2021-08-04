
# Import everything needed to edit video clips
from moviepy.editor import VideoFileClip
print('Video rotator By: safayethossain775@gmail.com')
# loading video dsa gfg intro video
vv = input('Enter File Location: ')
if vv=='': exit()
clip = VideoFileClip(vv)
# rotating clip by 45 degree
cc = int(input('Enter rotation in degree ([-] to rotate counter clockwize): '))
if cc=='': cc=-90
clip = clip.rotate(cc)
oo = input('Enter output Filename: ')
if oo=='':oo='output'
else: oo=oo.replace('.mp4','')
clip.write_videofile('%s.mp4'%oo, threads=8)
print('All Done')

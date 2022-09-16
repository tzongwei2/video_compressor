import argparse
import os
import moviepy.editor as mp

parser = argparse.ArgumentParser()
parser.add_argument("-s",default ="1080", help ="size of downsized video")
parser.add_argument("-out",default ="output", help="name of output folder") 
args = parser.parse_args()

video_path ="raw_videos"

if not os.path.exists(args.out):
    os.makedirs(args.out)


for file in os.listdir(video_path):
    vid = mp.VideoFileClip((video_path + '/' + file))
    clip = vid.subclip(0,3)
    height =clip.h
    filename = os.path.splitext(file)[0] #remove the extension from the name

    if(height <= int(args.s)):
       vid.write_videofile(args.out + "/" + filename + args.s +"p.mp4")
    else:
        resized_vid = vid.resize(height= int(args.s))
        resized_vid.write_videofile(args.out + "/" + filename + args.s +"p.mp4")
    









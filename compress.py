import argparse
import os
import moviepy.editor as mp

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--size",default ="1080")
parser.add_argument("-out", "--output",default ="output")
args = parser.parse_args()

video_path ="raw_videos"

if not os.path.exists(args.output):
    os.makedirs(args.output)


for file in os.listdir(video_path):
    vid = mp.VideoFileClip((video_path + '/' + file))
    clip = vid.subclip(0,3)
    height =clip.h
    filename = os.path.splitext(file)[0] #remove the extension from the name

    if(height <= int(args.size)):
       vid.write_videofile(args.output + "/" + filename + args.size +"p.mp4")
    else:
        resized_vid = vid.resize(height= int(args.size))
        resized_vid.write_videofile(args.output + "/" + filename + args.size +"p.mp4")
    









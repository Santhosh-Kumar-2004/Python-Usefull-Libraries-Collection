"C:/Users/Santhosh kumar/Pictures/For gudiya"
"c:/Users/Santhosh kumar/Music/songs/Lovely English/y2mate.com - Tesher Jason Derulo  Jalebi Baby Lyrics.mp3"

from moviepy.editor import * # type: ignore
import os

# Define the path to your image folder and music file
image_folder = "C:/Users/Santhosh kumar/Pictures/For gudiya"  # Replace with your image folder path
music_file = "c:/Users/Santhosh kumar/Music/songs/Lovely English/y2mate.com - Tesher Jason Derulo  Jalebi Baby Lyrics.mp3"
  # Replace with your music file path

# Load images and create image clips
image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
image_clips = [ImageClip(img).set_duration(2).fadein(1).fadeout(1) for img in sorted(image_files)]

# Create a video from the image clips
video = concatenate_videoclips(image_clips, method="compose")

# Load background music
audio = AudioFileClip(music_file)

# Set the audio for the video (make sure the video is as long as the music)
final_audio = audio.subclip(0, video.duration)
video = video.set_audio(final_audio)

# Write the final video to a file
video.write_videofile("slideshow_sanjana.mp4", fps=24)

print("Slideshow video created successfully!")

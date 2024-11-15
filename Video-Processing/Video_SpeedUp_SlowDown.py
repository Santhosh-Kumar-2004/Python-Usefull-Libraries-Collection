from moviepy.editor import * # type: ignore

# Load a video clip
clip = VideoFileClip("c:/Users/Santhosh kumar/Videos/Status's Vids/y2mate.com - Who Let the Dogs Out  shorts wholetthedogsout 2000smusic_v720P (1) (1).mp4")

# Speed-up the video by 2x
speed_up_clip = clip.fx(vfx.speedx, 2) # type: ignore

# Slow down the video by 0.5x
slow_motion_clip = clip.fx(vfx.speedx, 0.5) # type: ignore

# Concatenate the clips
final_video = concatenate_videoclips([speed_up_clip, slow_motion_clip])

# Write the final video to a file
final_video.write_videofile("speed_and_slow_motion.mp4", fps=24)

print("Video speed and slow motion effect applied successfully!")

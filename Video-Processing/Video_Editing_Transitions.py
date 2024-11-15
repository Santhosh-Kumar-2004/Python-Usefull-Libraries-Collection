from moviepy.editor import * # type: ignore

# Load video clips
clip1 = VideoFileClip("c:/Users/Santhosh kumar/Videos/Status's Vids/y2mate.com - The Wolf of Wall Street 4K EDIT_1080pFHR.mp4")
clip2 = VideoFileClip("c:/Users/Santhosh kumar/Videos/Status's Vids/y2mate.com - Paul Walker  Vin Diesel  Fast  Furious_480p.mp4")

# Create a fade transition between the clips
clip1 = clip1.fadeout(1)  # type: ignore # 1 second fade-out
clip2 = clip2.fadein(1)  # type: ignore # 1 second fade-in

# Combine the clips with the transition
final_video = concatenate_videoclips([clip1, clip2])

# Write the final video to a file
final_video.write_videofile("final_movie.mp4", fps=24)

print("Video editing with transition completed!")

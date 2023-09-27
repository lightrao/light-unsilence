from unsilence import Unsilence

# Input and output video paths
my_input_video = "./original/first.mp4"
my_output_video = "./output/first.mp4"

# Create Unsilence object
u = Unsilence(my_input_video)

# Detect silence in the video
u.detect_silence()

# Render the output video
u.render_media(my_output_video, audible_speed=1, silent_speed=32)

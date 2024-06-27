# Toolbox
This repository contains a collection of general-purpose scripts used for various video processing tasks in my day-to-day work. It includes scripts for converting video frame rates, using FFmpeg commands to cut, crop, and loop videos, as well as converting videos to RTSP streams using Python.


## convert_video_to_12fps.py

### Description
pip install Python 3.x, OpenCV and tqdm to run the script. 
To convert the frame rate of a video to any specified FPS, run the following command:

```sh
python convert_video_to_12fps.py <input_video_path> <output_video_path> <new_fps>
```
#### Arguments

- `<input_video_path>`: Path to the input video file.
- `<output_video_path>`: Path to save the output video file.
- `<new_fps>`: The desired frame rate for the output video.

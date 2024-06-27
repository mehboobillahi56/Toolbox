# Filename: convert_video_to_12fps.py

import cv2
import argparse
from tqdm import tqdm

def convert_video_to_12fps(input_path, output_path, new_fps):
    # Open the input video file
    cap = cv2.VideoCapture(input_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get the original frame rate, size, and total frame count
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change the codec if needed
    out = cv2.VideoWriter(output_path, fourcc, new_fps, (frame_width, frame_height))

    # Frame counter
    frame_count = 0

    # Progress bar setup
    progress_bar = tqdm(total=total_frames, desc="Processing Video", unit="frame")

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Write every nth frame to achieve the desired frame rate
        if frame_count % int(original_fps / new_fps) == 0:
            out.write(frame)

        frame_count += 1
        progress_bar.update(1)

    # Release everything when done
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    progress_bar.close()
    print(f"Video saved to {output_path}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert video to a specified FPS")
    parser.add_argument('input_path', type=str, help="Path to the input video file")
    parser.add_argument('output_path', type=str, help="Path to save the output video file")
    parser.add_argument('fps', type=int, help="New frame rate (FPS)")
    args = parser.parse_args()

    # Call the function with parsed arguments
    convert_video_to_12fps(args.input_path, args.output_path, args.fps)

import subprocess
import os

def create_image_video():
    """
    Creates a video by evenly distributing images from the 'images' directory using Kdenlive's 'melt' tool,
    with smooth crossfade transitions. The output video is saved in the 'video' directory.
    """
    try:
        duration_seconds = int(input("Enter the desired video length in seconds: "))
        output_file = input("Enter the output filename (e.g., image_video.mp4): ")
        frame_rate = 30  # Standard frame rate

        images_dir = "../images"
        image_files = sorted([f for f in os.listdir(images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))])
        if not image_files:
            print("No images found in the 'images' directory.")
            return

        num_images = len(image_files)
        if num_images == 1:
            transition_frames = 0
        else:
            transition_frames = int(0.5 * frame_rate)  # 0.5 second crossfade

        # Calculate duration per image (including overlap for transitions)
        total_transition_time = (num_images - 1) * (transition_frames / frame_rate)
        duration_per_image = (duration_seconds + total_transition_time) / num_images
        image_frames = int(duration_per_image * frame_rate)

        # Ensure 'video' directory exists
        video_dir = ""
        os.makedirs(video_dir, exist_ok=True)
        output_path = os.path.join(video_dir, output_file)

        # Build melt command with transitions
        command = ["melt", "-silent"]
        for i, img in enumerate(image_files):
            img_path = os.path.join(images_dir, img)
            command.extend([img_path, f"length={image_frames}"])
            if i > 0:
                command.extend(["-transition", "luma", f"duration={transition_frames}"])

        command.extend(["-consumer", f"avformat:{output_path}"])
        print(f"\nExecuting command: {' '.join(command)}\n")

        process = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Image video with transitions created successfully!")
        print(f"Output file: {output_path}")
    except FileNotFoundError:
        print("Error: The 'melt' command was not found.")
        print("Please ensure that Kdenlive and the MLT framework are installed and in your system's PATH.")
    except subprocess.CalledProcessError as e:
        print("An error occurred while creating the video:")
        print(e.stderr)
    except ValueError:
        print("Invalid input. Please enter a whole number for the duration.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    create_image_video()


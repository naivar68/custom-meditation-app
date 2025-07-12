import subprocess
import shlex
import os

def create_image_video():
    """
    Creates a video by evenly distributing images from the 'images' directory using Kdenlive's 'melt' tool.
    """
    try:
        duration_seconds = int(input("Enter the desired video length in seconds: "))
        output_file = input("Enter the output filename (e.g., image_video.mp4): ")
        frame_rate = 30  # Standard frame rate

        # List image files
        images_dir = "images"
        image_files = [f for f in os.listdir(images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
        if not image_files:
            print("No images found in the 'images' directory.")
            return

        num_images = len(image_files)
        duration_per_image = duration_seconds / num_images

        # Build melt command
        inputs = []
        for img in image_files:
            img_path = os.path.join(images_dir, img)
            length_frames = int(duration_per_image * frame_rate)
            inputs.append(f"{img_path} length={length_frames}")

        command = f"melt -silent {' '.join(inputs)} -consumer avformat:{output_file}"
        print(f"\nExecuting command: {command}\n")

        process = subprocess.run(shlex.split(command), check=True, capture_output=True, text=True)
        print("Image video created successfully!")
        print(f"Output file: {output_file}")
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


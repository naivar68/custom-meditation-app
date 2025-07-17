import subprocess as sp
import os

def resample_wav(input_path: str, output_path: str, target_sample_rate: int = 48000):
    """
    Resamples a .wav file to the target sample rate using ffmpeg and saves it as a .wav.
    """
    command = [
        'ffmpeg',
        '-y',  # Overwrite output file if it exists
        '-i', input_path,
        '-ar', str(target_sample_rate),
        '-acodec', 'pcm_s16le',
        output_path
    ]
    try:
        sp.run(command, check=True, capture_output=True)
        print(f"File saved as '{output_path}' with sample rate {target_sample_rate} Hz.")
    except sp.CalledProcessError as e:
        print(f"FFmpeg Error: {e.stderr.decode()}")
    except FileNotFoundError:
        print("Error: ffmpeg is not installed or not in your system's PATH.")

if __name__ == "__main__":
    file_to_load = input("Enter the path to the .wav file to import: ").strip()
    if not file_to_load or not os.path.exists(file_to_load) or not file_to_load.lower().endswith('.wav'):
        print("No valid .wav file path provided.")
    else:
        # Ensure 'audio' directory exists
        output_dir = ''
        os.makedirs(output_dir, exist_ok=True)
        base_name = os.path.splitext(os.path.basename(file_to_load))[0]
        output_path = os.path.join(output_dir, f"{base_name}_48000.wav")

        # Probe the input file's sample rate
        probe_cmd = [
            'ffprobe', '-v', 'error', '-select_streams', 'a:0',
            '-show_entries', 'stream=sample_rate', '-of', 'default=noprint_wrappers=1:nokey=1',
            file_to_load
        ]
        try:
            result = sp.run(probe_cmd, capture_output=True, check=True, text=True)
            src_sample_rate = int(result.stdout.strip())
        except Exception:
            print("Could not determine source sample rate. Proceeding with resampling.")
            src_sample_rate = None

        if src_sample_rate == 48000:
            # Just copy the file to the audio directory
            import shutil
            shutil.copy2(file_to_load, os.path.join(output_dir, os.path.basename(file_to_load)))
            print(f"File copied to '{output_dir}' (already at 48000 Hz).")
        else:
            resample_wav(file_to_load, output_path, target_sample_rate=48000)
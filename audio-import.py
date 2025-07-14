import subprocess as SP
import numpy as np
import pandas as pd
import os
import glob

def load_audio_to_dataframe(file_path: str, sample_rate: int = 44100):
    """
    Loads a .wav audio file using ffmpeg and returns it as a pandas DataFrame.
    The audio is converted to 16-bit signed PCM, stereo, with the specified sample rate.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'")
        return None

    command = [
        'ffmpeg',
        '-i', file_path,
        '-f', 's16le',
        '-ac', '2',
        '-ar', str(sample_rate),
        '-loglevel', 'error',
        'pipe:1'
    ]

    try:
        result = SP.run(command, capture_output=True, check=True)
        raw_audio = result.stdout
        audio_array = np.frombuffer(raw_audio, dtype=np.int16).reshape(-1, 2)
        audio_df = pd.DataFrame(audio_array, columns=['Left', 'Right'])
        return audio_df

    except SP.CalledProcessError as e:
        print(f"FFmpeg Error: {e.stderr.decode()}")
        return None
    except FileNotFoundError:
        print("Error: ffmpeg is not installed or not in your system's PATH.")
        return None

if __name__ == "__main__":
    wav_files = glob.glob('*.wav')
    if not wav_files:
        print("No .wav files found in the current directory.")
    else:
        file_to_load = wav_files[0]
        print(f"Loading audio file: {file_to_load}")
        audio_df = load_audio_to_dataframe(file_to_load, sample_rate=44100)

        if audio_df is not None:
            print("\n✅ Audio loaded successfully into a pandas DataFrame!")
            print("\nDataFrame Info:")
            audio_df.info()
            print("\nFirst 5 samples:")
            print(audio_df.head())
            duration_seconds = len(audio_df) / 44100
            print(f"\nDuration: {duration_seconds:.2f} seconds")
            print(f"Number of samples: {len(audio_df)}")

            # Ensure 'audio' directory exists
            output_dir = 'audio'
            os.makedirs(output_dir, exist_ok=True)
            base_name = os.path.splitext(os.path.basename(file_to_load))[0]
            output_path = os.path.join(output_dir, f"{base_name}.csv")
            audio_df.to_csv(output_path, index=False)
            print(f"\nDataFrame saved to '{output_path}'")import subprocess as SP
            import numpy as np
            import pandas as pd
            import os
            import glob

            def load_audio_to_dataframe(file_path: str, sample_rate: int = 44100):
                """
                Loads a .wav audio file using ffmpeg and returns it as a pandas DataFrame.
                The audio is converted to 16-bit signed PCM, stereo, with the specified sample rate.
                """
                if not os.path.exists(file_path):
                    print(f"Error: File not found at '{file_path}'")
                    return None

                command = [
                    'ffmpeg',
                    '-i', file_path,
                    '-f', 's16le',
                    '-ac', '2',
                    '-ar', str(sample_rate),
                    '-loglevel', 'error',
                    'pipe:1'
                ]

                try:
                    result = SP.run(command, capture_output=True, check=True)
                    raw_audio = result.stdout
                    audio_array = np.frombuffer(raw_audio, dtype=np.int16).reshape(-1, 2)
                    audio_df = pd.DataFrame(audio_array, columns=['Left', 'Right'])
                    return audio_df

                except SP.CalledProcessError as e:
                    print(f"FFmpeg Error: {e.stderr.decode()}")
                    return None
                except FileNotFoundError:
                    print("Error: ffmpeg is not installed or not in your system's PATH.")
                    return None

            if __name__ == "__main__":
                wav_files = glob.glob('*.wav')
                if not wav_files:
                    print("No .wav files found in the current directory.")
                else:
                    file_to_load = wav_files[0]
                    print(f"Loading audio file: {file_to_load}")
                    audio_df = load_audio_to_dataframe(file_to_load, sample_rate=44100)

                    if audio_df is not None:
                        print("\n✅ Audio loaded successfully into a pandas DataFrame!")
                        print("\nDataFrame Info:")
                        audio_df.info()
                        print("\nFirst 5 samples:")
                        print(audio_df.head())
                        duration_seconds = len(audio_df) / 44100
                        print(f"\nDuration: {duration_seconds:.2f} seconds")
                        print(f"Number of samples: {len(audio_df)}")

                        # Ensure 'audio' directory exists
                        output_dir = 'audio'
                        os.makedirs(output_dir, exist_ok=True)
                        base_name = os.path.splitext(os.path.basename(file_to_load))[0]
                        output_path = os.path.join(output_dir, f"{base_name}.csv")
                        audio_df.to_csv(output_path, index=False)
                        print(f"\nDataFrame saved to '{output_path}'")
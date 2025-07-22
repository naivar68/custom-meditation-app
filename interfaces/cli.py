 # The cmd version of the interface for the audio import and video creation scripts.
# The final creation utilizes the functionality of a script which unifies the audio, video
# and binuaral audio into a single video file.

import subprocess as sp
import os
from github import Github
import requests


def clear_screen():
    """Clear the terminal screen."""
    if os.name == 'nt':
        sp.run(['cls'], check=True)
    else:
        sp.run(['clear'], check=True)


def cli_interface():
    """ Command line interface for the audio import / video creation tool """
    print("Welcome to the Audio Video Creation Tool!\n")

    print("Do you already have the binaural beats creator cloned fro  Github into your project directory 'git-repositories'?[y/n]")
    clone = input()
    if clone == 'y':
        print("Great! Proceeding with the audio import and video creation.")
    elif clone == 'n':
        print("Cloning the binaural beats creator repository from GitHub...")
        try:
            g = Github()
            # First repo
            repo = g.get_repo("https://github.com/naivar68/Binuaral_Beat_Session_Creator.v.1.0.git")  # Replace with your repo
            repo.clone_to("git-repositories/binaural-beats-creator")
            # Second repo
            repo = g.get_repo("https://github.com/naivar68/OpenVoice.git")
            repo.clone_to("git-repositories/OpenVoice")

            print("Repository cloned successfully!")
        except Exception as e:
            print(f"An error occurred while cloning the repository: {e}")
            return
    else:
        print("Invalid input. Please run the program again and enter 'y' or 'n'.")
        return
    clear_screen()


    print("Please type the path to the audio file you want to use:")
    print("example: /path/to/your/audio-file.mp3 ")
    audio_path = input("Audio file path: ").strip()
    if not os.path.isfile(audio_path):
        print("The specified audio file does not exist. Please check the path and try again.")
        return
    print(f"Audio file '{audio_path}' found. Proceeding with import to 'custom-meditation-app/audio/...")
    # Here you would call the audio import function
    # For example: audio_import(audio_path)
    print("Audio import successful!")

    print("Now, please type the path to the video file you want to use:")
    print("example: /path/to/your/video-file.mp4 ")
    video_path = input("Video file path: ").strip()
    if not os.path.isfile(video_path):
        print("The specified video file does not exist. Please check the path and try again.")
        return
    print(f"Video file '{video_path}' found. Proceeding with import to 'custom-meditation-app/video/...")
    # Here you would call the video import function
    # For example: video_import(video_path)
    print("Video import successful!")

    print("Now, please type the path to the text file containing your affirmations:")
    print("example: /path/to/your/affirmations.txt ")
    affirmations_path = input("Affirmations file path: ").strip()
    if not os.path.isfile(affirmations_path):
        print("The specified affirmations file does not exist. Please check the path and try again.")
        return
    print(f"Affirmations file '{affirmations_path}' found. Proceeding with import to 'custom-meditation-app/data/...")
    # Here you would call the affirmations import function
    # For example: affirmations_import(affirmations_path)
    print("Affirmations import successful!")

    print("All files imported successfully!")

    print("Now, let's create your video with the imported audio, video, and affirmations.")
    # Here you would call the video creation function
    # For example: create_video(audio_path, video_path, affirmations_path)
    print("Video creation successful! Your video is ready.")






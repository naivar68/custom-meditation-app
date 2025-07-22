from logo import logo
import subprocess as sp
import os



def main():
    # Clear the screen
    if os.name == 'nt':
        sp.run(['cls'], check=True)
    else:
        sp.run(['clear'], check=True)




    # Print the logo
    logo()

    # Print the welcome message
    print("Welcome to the Audio Video Creation Tool!")
    print("Please have the following to best work with this tool:\n")
    print("""
    1. A pre-recorded audio file of your own voice [5-10 seconds] if voice cloning is enabled.
    2. A series of 'royalty free' images or videos that you want to use in your video.
    3. A text file of the affirmations you want to use in the video, if you want to customize.
    \n
    Save the text file into the 'data' folder in the same directory as this script.
    \n""")
    print("Press Enter to continue...")
    input()

    # Graphical or command line interface
    print("This tool is currently in development. Please use the command line interface for now.")

    input()

    sp.run(['clear','cls'][os.name == 'nt'], check=True)
    print("Which interface would you like to use?")
    print("1. Command Line Interface (CLI)")
    print("2. Graphical User Interface (GUI) [Coming Soon]")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        print("You have chosen the Command Line Interface (CLI).")
        # Here you would call the CLI function or module
        # For example: cli.run()
    elif choice == '2':
        print("The Graphical User Interface (GUI) is coming soon!")
    else:
        print("Invalid choice. Please run the program again.")

    print("Thank you for using the Audio Video Creation Tool!")
    print("Goodbye!")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()


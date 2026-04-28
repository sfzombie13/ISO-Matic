import subprocess
import os
import sys
import shutil

def get_valid_path(prompt, is_directory=True, must_exist=True):
    """
    Prompts the user for a path and validates it.
    """
    while True:
        path = input(prompt).strip()
        if not path:
            print("Path cannot be empty. Please try again.")
            continue

        if is_directory:
            if must_exist and not os.path.isdir(path):
                print(f"Error: Directory '{path}' does not exist. Please enter a valid directory path.")
            elif not must_exist and os.path.exists(path) and not os.path.isdir(path):
                print(f"Error: A file with the same name as the target directory already exists at '{path}'.")
            else:
                return path
        else: # It's a file or a directory that doesn't necessarily exist yet
            parent_dir = os.path.dirname(path)
            if parent_dir and not os.path.isdir(parent_dir):
                try:
                    os.makedirs(parent_dir, exist_ok=True)
                    return path
                except OSError as e:
                    print(f"Error creating output directory '{parent_dir}': {e}. Please check permissions or path.")
            elif not parent_dir and not is_directory: # Case where path is just a filename in current dir
                 return path
            else: # Parent dir exists or it's a valid directory for output
                return path


def find_oscdimg_path():
    """
    Attempts to locate oscdimg.exe in common ADK paths.
    """
    common_adk_paths = [
        r"C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment Kit\Deployment Tools\amd64\Oscdimg\oscdimg.exe",
        r"C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment Kit\Deployment Tools\x86\Oscdimg\oscdimg.exe",
        r"C:\Program Files\Windows Kits\10\Assessment and Deployment Kit\Deployment Tools\amd64\Oscdimg\oscdimg.exe",
        r"C:\Program Files\Windows Kits\10\Assessment and Deployment Kit\Deployment Tools\x86\Oscdimg\oscdimg.exe"
    ]

    for path in common_adk_paths:
        if os.path.exists(path):
            print(f"Found oscdimg.exe at: {path}")
            return path
    
    # Try finding it in PATH
    if shutil.which("oscdimg.exe"):
        print(f"Found oscdimg.exe in system PATH: {shutil.which('oscdimg.exe')}")
        return shutil.which("oscdimg.exe")

    return None


def create_iso_with_progress():
    """
    Guides the user through creating an ISO file with real-time progress.
    """
    print("--- ISO - Matic ---")
    print("This script will help you create an ISO file using oscdimg.exe.")
    print("Please ensure you have oscdimg.exe installed (part of Windows ADK - Deployment Tools).\n")

    # 1. Get Source Directory
    source_dir = get_valid_path("Enter the SOURCE directory (files to include in ISO): ", is_directory=True, must_exist=True)

    # 2. Get Output Directory and Filename
    output_base_dir = get_valid_path("Enter the OUTPUT DIRECTORY for the ISO: ", is_directory=True, must_exist=False)
    
    iso_filename = ""
    while not iso_filename:
        iso_filename = input("Enter the DESIRED FILENAME for the ISO: ").strip()
        if not iso_filename:
            print("Filename cannot be empty. Please try again.")
        elif any(char in iso_filename for char in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']):
            print("Filename contains invalid characters. Please avoid \\ / : * ? \" < > |")
            iso_filename = "" # Reset to ask again
    
    # Construct the final output ISO path
    output_iso_path = os.path.join(output_base_dir, iso_filename + ".iso")

    # 3. Get Oscdimg.exe Path
    auto_oscdimg_path = find_oscdimg_path()
    if auto_oscdimg_path:
        use_auto = input(f"Use detected oscdimg.exe path '{auto_oscdimg_path}'? (y/n): ").lower()
        if use_auto == 'y':
            oscd_img_path = auto_oscdimg_path
        else:
            oscd_img_path = get_valid_path("Enter the FULL PATH to oscdimg.exe: ", is_directory=False, must_exist=True)
    else:
        print("oscdimg.exe not found automatically.")
        oscd_img_path = get_valid_path("Enter the FULL PATH to oscdimg.exe: ", is_directory=False, must_exist=True)

    print("\n--- Configuration Summary ---")
    print(f"Source Directory: {source_dir}")
    print(f"Output ISO File:  {output_iso_path}")
    print(f"Oscdimg.exe Path: {oscd_img_path}")
    print("-" * 30)

    confirm = input("Proceed with ISO creation? (yes/no): ").lower()
    if confirm != 'yes':
        print("ISO creation cancelled.")
        return

    # Construct the command for oscdimg.exe
    # -n: Allows long filenames (Joliet)
    # -m: No size limit
    # -o: Optimized storage (removes duplicate files)
    command = [
        oscd_img_path,
        "-n",
        "-m",
        "-o",
        source_dir,
        output_iso_path
    ]

    print("\nStarting ISO creation...")
    print(f"Command: {' '.join(command)}\n")

    try:
        # Use subprocess.Popen for real-time output
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, # Merge stderr into stdout for easier progress capture
            text=True, # Decode output as text
            bufsize=1, # Line-buffered output
            universal_newlines=True # Ensure consistent line endings
        )

        # Read and print output line by line for progress
        for line in iter(process.stdout.readline, ''):
            sys.stdout.write(line)
            sys.stdout.flush() # Ensure the output is immediately visible

        process.wait() # Wait for the process to complete

        if process.returncode == 0:
            print(f"\nSUCCESS: ISO file created at '{output_iso_path}'")
        else:
            print(f"\nERROR: oscdimg.exe exited with code {process.returncode}")
            print("Please check the messages above for details.")

    except FileNotFoundError:
        print(f"\nERROR: oscdimg.exe not found at '{oscd_img_path}'.")
        print("Please ensure the path is correct or OSCDIMG is installed with the Windows ADK.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    create_iso_with_progress()
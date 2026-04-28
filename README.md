ISO-matic 💿

ISO-matic is a user-friendly Python script designed to simplify the creation of ISO disk images from your files and folders on Windows. Leveraging the robust oscdimg.exe utility (part of the Windows ADK), ISO-matic provides an interactive command-line interface to effortlessly package your data into a standard ISO file.

Say goodbye to complex command-line arguments and manual path handling! ISO-matic streamlines the process, making ISO creation quick and intuitive.
✨ Features

    Interactive Prompts: Guides you through source directory, output location, and ISO filename.

    oscdimg.exe Integration: Utilizes the powerful and reliable oscdimg.exe from the Windows ADK for high-quality ISO generation.

    Real-time Progress: Displays the output from oscdimg.exe directly in your terminal, so you always know what's happening.

    Path Validation: Basic checks for valid input paths to prevent common errors.

    Automatic oscdimg.exe Discovery: Attempts to locate your oscdimg.exe installation automatically.

    Automatic Directory Creation: Creates the output directory for your ISO if it doesn't already exist.

🚀 Getting Started

Follow these steps to get ISO-matic up and running on your Windows machine.
Prerequisites

Before you can use ISO-matic, you'll need the following:

    Python 3.x:

        Download and install Python from python.org.

        Crucially, during installation, ensure you check the box that says "Add Python to PATH".

    Windows Assessment and Deployment Kit (ADK) - Deployment Tools:

        oscdimg.exe is a vital component. It comes with the Windows ADK.

        Download the Windows ADK from Microsoft Learn.

        During the ADK installation, you only need to select "Deployment Tools". You can deselect other components.

        After installation, oscdimg.exe is typically found in a path similar to:
        C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment Kit\Deployment Tools\amd64\Oscdimg\oscdimg.exe
        (The exact path may vary based on your Windows version and architecture.)

Installation

    Clone the Repository:
    code Bash

    git clone https://github.com/YOUR_GITHUB_USERNAME/ISO-matic.git
    cd ISO-matic

    (Replace YOUR_GITHUB_USERNAME with your actual GitHub username.)

    Download Manually:

        Alternatively, you can download the iso_matic.py script directly from this repository and place it in a folder of your choice.

🏃 How to Run

    Open Command Prompt or PowerShell: Navigate to the directory where you saved iso_matic.py.
    code Bash

    cd C:\path\to\your\ISO-matic-folder

    Execute the script:
    code Bash

    python iso_matic.py

    Follow the Interactive Prompts:

        The script will first ask for the source directory containing the files/folders you want to put into the ISO.

        Next, it will ask for the output directory where you want the ISO file to be saved.

        Then, you'll provide the desired filename for your ISO (e.g., MyInstaller – the .iso extension will be added automatically).

        Finally, it will attempt to auto-detect your oscdimg.exe path. If found, you can confirm; otherwise, you'll be prompted to enter the full path manually.

    The script will display the progress of the ISO creation and notify you upon completion or if any errors occur.

⚠️ Troubleshooting

    "Error 5: Access is denied" or "Could not delete existing file...":

        This usually means the specified output ISO path refers to an existing directory instead of a filename, or that the file/directory is locked by another program.

        Ensure your output is a proper filename (e.g., C:\Output\MyDisc.iso), not just a directory name.

        Close any File Explorer windows or applications that might be accessing the output location.

        Try running your Command Prompt/PowerShell as Administrator.

    "oscdimg.exe not found...":

        Double-check that the Windows ADK "Deployment Tools" component is installed correctly.

        Verify the path to oscdimg.exe is accurate if you entered it manually.

        Ensure the oscdimg.exe directory is in your system's PATH environment variable (though the script tries to find it, this can help).

    "Python is not recognized as an internal or external command":

        This means Python is not correctly added to your system's PATH. Re-run the Python installer and ensure "Add Python to PATH" is checked, or manually add it.

🤝 Contributing

ISO-matic is a simple tool, but contributions are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to:

    Fork the repository.

    Create a new branch (git checkout -b feature/your-feature-name).

    Make your changes.

    Commit your changes (git commit -m 'Add new feature').

    Push to the branch (git push origin feature/your-feature-name).

    Open a Pull Request.

📜 License

This project is licensed under the Unlicense License - see the LICENSE file for details.
🌟 Acknowledgements

    oscdimg.exe for being the powerful backbone of Windows ISO creation.

    The Python subprocess module for making external command execution a breeze.

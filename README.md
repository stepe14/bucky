# BUCKY_V1

## Setup

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.12 or higher
- System Package Installer
- Virtual Environment (venv)

### Installations

1. <b>Clone the Repository</b>
    git clone https://github.com/<yourusername>/bucky_v1.git
    cd bucky_v1

2. <b>Create and Activate a Virtual Environment</b>
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. <b>Install Required Python Packages</b> 
    pip install -r requirements.txt

4. <b>Install System Dependencies</b>
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    choco install flac  

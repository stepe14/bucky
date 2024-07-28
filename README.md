# BUCKY_V1

B.U.C.K.Y is an AI Assistant project using integrations of ChatGPT, Alexa, etc.

## Introduction

BUCKY_V1 is designed to provide a versatile AI assistant that can be easily set up and run on various devices. The project leverages Flask for web functionalities and requests for handling HTTP requests.

## Features

- Flask-based web server
- HTTP request handling with `requests`
- Audio processing with `flac`

## Installation

Follow these steps to set up the project on your local machine.

### Prerequisites

- Python 3.12 or higher
- Git
- Virtual Environment (venv)

### Setup

1. **Clone the repository:**

   
   git clone https://github.com/yourusername/bucky_v1.git
   cd bucky_v1

Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Required Python Packages 
   pip install -r requirements.txt

Install System Dependencies
   choco install flac  #install flac using chocolatey













B.U.C.K.Y
# Setup
-python, git, and vscode are prereqs to have before isntalling app code
-for windows, need chocolatey for system wide packages and pip for ones inside the venv
*  ``` @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin" ```
-all poython packages are managed inside venv, and tracked via adding pip freeze to requirements.txt
-should make startup script that installs system wide packages and pip install -r requirements.txt
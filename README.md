# MCSAST-Py Minecraft Server Auto Setup Tool (Python Version)

## Overview
MCSAST-Py is a Python-based tool designed to automate the setup of various types of Minecraft servers. It supports multiple server types, including Paper, Purpur, Pufferfish, Velocity, BungeeCord, Waterfall, Fabric, Forge, and custom server setups. This tool simplifies the installation process, ensuring that your Minecraft server is up and running with minimal effort.


## Features
- Automated download and setup for various Minecraft server types.
- Customizable server flags for optimal performance.
- Supports Windows and Linux operating systems.
- Checks Java installation and version compatibility.
## Requirements
- Python 3.x
- Java Development Kit (JDK) installed and added to the system PATH
- Internet connection for downloading server files

## Installation
1. **Clone the Repository:**
    ```sh
    git clone https://github.com/RyanisyydsTT/MCSAST-Py.git
    cd MCSAST-Py
    ```

2. **Install Dependencies:**
    Ensure you have Python and Java installed on your system.

3. **Run the Setup:**
    ```sh
    python main.py
    ```

## Usage
1. **Check Java Installation:**
    The script will automatically check if Java is installed and if the version is supported (17-21). If Java is not found or not supported, the script will exit with an error message.

2. **Choose a Server Type:**
    The setup supports various server types. You will be prompted to choose one from the list:
    - Paper
    - Purpur
    - Pufferfish
    - Velocity
    - BungeeCord
    - Waterfall
    - Fabric
    - Forge
    - Custom

3. **Enter Server Version and Build Number:**
    For most server types, you will need to enter the server version and build number.

4. **Download and Setup Server:**
    The script will download the server jar file, set it up, and create a script (`runserver.bat` for Windows or `runserver.sh` for Linux) to start the server with recommended flags for optimal performance.

5. **Run Your Server:**
    Once the setup is complete, run your server by executing the generated script:
    - On Windows: Double-click `runserver.bat`
    - On Linux: Run `./runserver.sh`

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or support, please contact [willy0925owo@gmail.com](mailto:willy0925owo@gmail.com).

## Disclaimer
This tool is provided "as is" without any warranties. Use it at your own risk. The author is not responsible for any damages or data loss resulting from the use of this tool.

Enjoy your Minecraft server with MCSAST-Py!

## TODO List
- Pterodactyl Support(Gave up cause I cannot find a way to install java in a python file.)
- Download without build number

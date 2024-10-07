1. **Install Python**
- Windows:
	- Python can be installed using the Microsoft Store.
- MacOS:
	-	`brew install python3`
	-	Check the installation: `python3 --version`
-	Linux:
	-	`sudo apt update && sudo apt install python3 python3-pip #for Debian/Ubuntu`
	-	Check the installation: `python3 --version`


2.  **Clone the repository**:

```bash
git clone https://github.com/yourrepo/sharing_synergy.git

cd sharing_synergy
```

3. **Install Sharing Synergy**

Windows:
`pip install --editable .`

MacOS and Linux:
`pip3 install --editable .`

4. **Environment variables**

You might need to place the Sharing Syngery Script in your PATH environment variable, then **restart** your computer.

To find where the script is located, use this command:
```python3 -m site --user-base```

Depending on your operating system this will return different paths that look like these:
1. `/Users/yourname/Library/Python/3.x/bin` (MacOS)
2. `/home/yourname/.local/bin` Linux
3. `C:\Users\your_username\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts` Windows

### For Windows:
- Type System into the windows search bar, and select System
- Navigate to Advanced System Settings
- Select Environment Variables at the bottom, under Startup and Recovery
- Under System Variables, select Path and click Edit...
- Select New, and add the script path from above
- Press OK on all the dialogue boxes to finish
- **You may need to restart your computer for it to take effect**

### For MacOS
- Open your .bash_profile (or .zshrc if you're using Zsh):
```bash
nano ~/.bash_profile # For Bash
nano ~/.zshrc # For Zsh
```
- Add this line to the end of the file: `export PATH="$PATH:/Users/yourname/Library/Python/3.x/bin"` (Use whatever path was given to you by the ```python3 -m site --user-base``` command)
- Save the file and run the following command to reload the shell: ```source ~/.bash_profile # or source ~/.zshrc```

### For Linux
- Open `.bashrc` or `.zshrc`:
- ```nano ~/.bashrc # For Bash```
- Add the line:
- ```export PATH="$PATH:/home/yourname/.local/bin"```  (Use whatever path was given to you by the ```python3 -m site --user-base``` command)
- Reload the shell: `source ~/.bashrc`

5. **Test the CLI**
Try running the following command:
```bash
syn help
```

A list of commands to use for Sharing Synergy should pop up.
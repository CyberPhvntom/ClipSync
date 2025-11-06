# **ClipSync**

Seamlessly send clipboard content to any application with zero clicks.
ClipSync is a lightweight Python utility that monitors your system clipboard and automatically submits copied content to your target application. Perfect for rapid research, learning workflows, and productivity enhancement.


## Use Cases

Study & Practice: Work through textbook problems and practice questions to verify your understanding
Research Assistant: Quickly query concepts from papers, articles, or documentation
Code Learning: Get instant explanations of code snippets while learning to program
Language Learning: Rapid translation and grammar checking
Content Summarization: Summarize articles and documents efficiently
Accessibility: Quick information lookup for users who benefit from streamlined workflows
General Automation: Automate text input to any application—text editors, documents, chat interfaces, and more

## Responsible Use
ClipSync is designed as a learning and productivity tool. Please use it responsibly:

✅ Practice problems and self-study

✅ Research and exploration

✅ Learning new concepts

❌ Graded exams or assessments

❌ Assignments where independent work is required

❌ Academic dishonesty of any kind

**Remember: AI is a tool to enhance learning, not replace it. Use ClipSync to supplement your understanding, not substitute for it.**


## Features

>Automatic clipboard monitoring
>Auto-focus any target window
>Instant paste and submit
>Configurable polling interval
>Cross-platform (Windows, macOS, Linux)
>Easy stop with Ctrl+C
>Minimal dependencies


## Prerequisites

Python 3.7 or higher
Any target application (AI chat, text editor, etc.)

### Check your Python version:
bashpython --version
or
bashpython3 --version

## Installation
### Windows

Clone the repository

cmd   git clone https://github.com/CyberPhvntom/clipsync.git
   cd clipsync

Install dependencies

cmd   pip install -r requirements.txt
If pip doesn't work, try:
cmd   python -m pip install -r requirements.txt


### macOS / Linux

Clone the repository

bash   git clone https://github.com/CyberPhvntom/clipsync.git
   cd clipsync

#### Install dependencies

bash   pip3 install -r requirements.txt
If pip3 doesn't work, try:
bash   python3 -m pip install -r requirements.txt

#### Alternative: Using Virtual Environment (Recommended)
##### Windows:
cmdpython -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

##### macOS/Linux:
bashpython3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

## Configuration
Open _clipsync.py_ and customize these settings:

** Target Window ** 
python TARGET_WINDOW_TITLE = "Claude"  # > _Change this to your target window_
By default, ClipSync looks for a window titled "Claude", but you can use any application:
Examples:

AI Chat:  "_ChatGPT_", "_Claude_", "_Gemini_" ***
Text Editors: "_Notepad_", "_Visual Studio Code_", "_Sublime Text_"
Documents: "_Document1 - Microsoft Word_", "_Untitled - Google Docs_"
Terminals: "_Command Prompt_", "_Terminal_"

Simply change the TARGET_WINDOW_TITLE to match your desired window's exact title.
** Pro Tip: Window titles are case-sensitive and must match exactly, including spaces! **

** Polling Interval **
pythontime.sleep(1.5)  # > _How often to check clipboard (in seconds)_

Default: 1.5 seconds - Good balance of speed and resource usage
Faster (0.5-1.0): More responsive, uses more CPU
Slower (2.0-3.0): Less responsive, lighter on resources

Choose based on your workflow speed and system performance.

## Usage
Starting ClipSync

### Windows:
cmdpython clipsync.py

### macOS/Linux:
bashpython3 clipsync.py

You should see:
_Monitoring clipboard... Press Ctrl+C to stop._
Workflow 

Open your target application (Claude, Notepad, ChatGPT, etc.)
Run ClipSync using the command above
Copy any text (Ctrl+C or Cmd+C)
ClipSync automatically pastes and submits to your target window
Stop monitoring by pressing Ctrl+C in the terminal

## Usage Tips

Keep your target window open and visible before starting ClipSync
Ensure the text input field is active and ready to receive input
Wait for AI responses before copying new content
Keep the terminal window open while ClipSync is running


## Finding Window Titles
Not sure what your window is called? Run this helper script:

Windows:
cmdpython -c "import pygetwindow as gw; [print(f'  - {title}') for title in gw.getAllTitles() if title.strip()]"

macOS/Linux:
bashpython3 -c "import pygetwindow as gw; [print(f'  - {title}') for title in gw.getAllTitles() if title.strip()]"

Or create a file find_windows.py:
pythonimport pygetwindow as gw

print("All open window titles:")
for title in gw.getAllTitles():
    if title.strip():
        print(f"  - {title}")
Then run it:
bashpython find_windows.py    # Windows
python3 find_windows.py   # macOS/Linux
Copy the exact title and paste it into TARGET_WINDOW_TITLE.

## Troubleshooting
** "Window not found" error **
Problem: ClipSync can't locate your target window.
Solutions:

Verify the window is open and visible
Check that TARGET_WINDOW_TITLE exactly matches (case-sensitive!)
Use the "Finding Window Titles" script above to get the exact title
Include all spaces and special characters in the title
**NOTE:** Window Titles can change. If the script suddenly stops working, double
 check Target Title still matches. Particularly, a fresh ChatGPT window will usually
 have a title of simply "ChatGPT". After the first prompt, the window title will
 most likely change to what ChatGPT decides to name your new conversation/chat.
 

**Nothing happens when copying**
Problem: Script runs but doesn't paste content.
Solutions:

-Confirm you see "New clipboard content: ..." in the terminal
-Verify ClipSync is still running (terminal window should be open)
-Restart the script: Ctrl+C, then run again
-Ensure you're copying text (not images or files)
-Try copying from a different application

**Paste not working properly**
Problem: Content pastes but doesn't submit, or pastes in wrong location.
Solutions:

-Click in the text input field before copying
-Increase the focus delay in clipsync.py:

python  time.sleep(0.5)  # Change to 1.0 or higher

-Some applications block automated input as a security feature
-Manually click the input field after window focuses

**pip or pip3 not recognized**
Problem: Command not found when installing dependencies.
Solutions:

Windows: Try python -m pip install -r requirements.txt
macOS/Linux: Try python3 -m pip install -r requirements.txt

Ensure Python is in your PATH
Restart your terminal after installing Python
Use a virtual environment (see Installation section)

**Module not found errors**
Problem: ModuleNotFoundError: No module named 'pyperclip' (or similar).
Solutions:

Install dependencies: pip install -r requirements.txt
If using virtual environment, ensure it's activated
Check you're using the same Python version that installed packages:

bash  which python    # macOS/Linux

  where python    # Windows

**Script stops unexpectedly**
Problem: ClipSync exits without pressing Ctrl+C.
Solutions:

-Check terminal for error messages
-Verify all dependencies installed: pip list
-Confirm Python 3.7+: python --version
-Run with verbose output:

bash  python clipsync.py 2>&1 | tee output.log

**High CPU usage**

Problem: ClipSync uses too many resources.
Solutions:

-Increase polling interval: time.sleep(3.0)
-Close other clipboard monitoring apps
-Restart your system if clipboard access is sluggish

**Linux-specific: Permission denied** 
Problem: Cannot access clipboard or window management.
Solutions:

-Install X11 dependencies:

bash  sudo apt-get install python3-tk python3-dev  # Ubuntu/Debian
  sudo dnf install python3-tkinter              # Fedora

Ensure you're running in a graphical environment (not SSH without X forwarding)


### **Pro Tips** ###

**Testing:** Use Notepad/TextEdit as your target to test without using AI credits
**Shortcuts:** Create a system shortcut to start/stop ClipSync quickly
**Multiple instances:** Run multiple ClipSync instances for different windows (advanced)
**Workflow:** Keep ClipSync in a dedicated terminal during work sessions
**Focus:** Close unnecessary windows to avoid title conflicts
**Setup:** First prompt should guide the rest of the conversation. 
           Example, you're using it to answer many multiple choice
           questions. Your first prompt could read:
           
           "For the remainder of this conversation, provide solely 
           the answer. No explanation is needed."

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

### Ideas for Contributions

Improve cross-platform compatibility
Add GUI interface
Add configuration file support
Improve documentation
Fix bugs
Add new features


📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

# **Disclaimer**
This tool is provided as-is for educational and productivity purposes. Users are responsible for ensuring their use complies with their institution's academic integrity policies and any applicable terms of service. The authors and contributors are not responsible for misuse of this tool.

## Acknowledgments
Built to enhance learning workflows and research productivity. Use wisely, learn actively.
Special thanks to the open-source community and the developers of:

pyperclip - Cross-platform clipboard access
pyautogui - GUI automation
pygetwindow - Window management


Made with ☕ for learners and researchers
Report Issues | Request Features

# UiCompiler
This is a python script to compile a ui file into a py file. This script uses pyuic5.

## How it works ?
To run correctly this script you must be in the folder where your ui files are stored.
Once the script launched, it will compile all the ui file in the folder into a py file.  
The new py file will have the same name as the ui file but with a "Ui_" at the beginning. For example, "window.ui" will be "Ui_window.py".
Here is the command to run the script :
>`python C:/Users/username/folderPath/UiCompiler/main.py`

## VSCode shortcut
To be more productive, we will set a shortcut into VSCode to run automatically the script.

### Install the extension
First install the extension : "*multi-command*"  
This extension will allow us to run multiple commands with one shortcut.

### Create the shortcut
To create a shortcut, add a .json file called "*settings*" in your "*.vscode*" folder.
In this file, add the following code :
```
{
    "multiCommand.commands" :[
        {
            "command": "multiCommand.uiCompiler",
            "sequence": [
                "workbench.action.terminal.sendSequence",
                {
                    "args": {
                        "text": "python C:/Users/username/folderPath/UiCompiler/main.py"
                    }
                },
                "workbench.action.terminal.runSelectedText",
                "editor.action.deleteLines"
            ]
        }
    ]
}
```
Here is the multi-command extension [documentation's](https://marketplace.visualstudio.com/items?itemName=ryuta46.multi-command).  
Then you need to modify the *keybindings.json* file. This file contains your personal shortcut or the one you modified.  
The simplest way to access this file is to go to :
* File
* Preference
* Keyboard shortcuts
* Then click on the button "*Open keyboard shortcuts (JSON)*" in the upper right corner of the window.

Add the following code into this file :
```
[
    {
        "key": "ctrl+alt+c",
        "command": "extension.multiCommand.execute",
        "args": {
            "command": "multiCommand.uiCompiler"
        },
        "when": "editorFocus && !editorReadOnly"
    }
]
```
For sure you can modify the pressed keys to run the shortcut. Here is the VSCode keybinding [documentation](https://code.visualstudio.com/docs/getstarted/keybindings).
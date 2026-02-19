# Mbook
This is a python script I made that reads a .txt file and automaticly seperates the text into the Minecraft page format.
I made this script as I wanted to add stories or wiki pages into my minecraft world via the book and quill.
However, since Minecraft does not allow you to paste text larger than a page (and the page size is very small), doing this was very slow.

# Useage
Before running, create a file called MineRaw.txt in the same cwd as the script and fill it with the text you want to be converted.
Please note that you can use a command in the text file @NEW to tell the script when you want to manually move to the next page.
Make sure when using the command that you do not leave any spaces or newlines between text e.g. "Page 1 Text@NEWPage 2 Text"
When running the script it'll create a new file called MineProc.txt with the converted text.
If you choose option 2, the script will begin pasting each page into your clipboard waiting 3 seconds before pasting the next page (signified by a terminal beep)
This is helpfull for pasting each page into the book without having to tab out of your game.

# FerretCLI
A simple discord.py client for use with 2 terminals, one for receiving messages, and another for sending them. This is primarily to be able to communicate when stuck in a CLI environment, as there is no official alternative.

# Usage
To use this, open 2 terminals using the method of your choice (I generally use tmux) and execute the chat.py on the first one to display messages, then run the input.py on the second terminal to type in your messages. I don't know the reason for the errors in the input.py, but I believe it's due to the fact that it is sharing a token with the other file or may have issues consistently grabbing and sending messages. I generally just shrink down the input terminal to one line and put it directly under the chat terminal, to emulate a little text area. If you have an idea on how to fix the error messages, or get this thing to run in just one terminal with multithreading, please feel free to let me know through the issues tab.

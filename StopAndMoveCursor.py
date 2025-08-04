"""

This file plays the recorded segment - starting on the cursors location - when audacity is opened on a Windows PC. It ends when pressed again and moves the cursor to the stopping location.
Coded by blackdiagon. 

"""


TONAME = '\\\\.\\pipe\\ToSrvPipe'
FROMNAME = '\\\\.\\pipe\\FromSrvPipe'
EOL = '\r\n\0'
TOFILE = open(TONAME, 'w')
FROMFILE = open(FROMNAME, 'rt')

def send_command(command):

    TOFILE.write(command + EOL)
    TOFILE.flush()

if __name__ == "__main__":
    send_command('PlayStopSelect:')
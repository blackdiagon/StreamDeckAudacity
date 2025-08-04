# StreamDeckAudacity
In this repository you will find different python files you can run from your stream deck to control Audacity.


Important:

* This code only runs on Windows x64 Systems.
* This code requires at least one instance of Audacity to be opened.
* You need to activate mod-script-pipe in Audacity. Please make sure your Audacity-file lies locally on your client and not on a server.
* In Audacity 3.7.4 you'll find it by pressing CRTL + P on your keyboard, go to "Modules" and scroll down until you find "mod-script-pipe". Per default, it won't have a specified value

How to use it on Stream Deck:

* Open your Stream Deck
* Under "System" select "Open"
* Select the Python file you want to asign to the button
* Optional: Choose a Name and an image

Tips:
* Create a folder on your PC, where you can permanently store the files. Otherwise, if you accidentally move or delete them, you'll have to set it all up from scratch.
* Bonus: Store the data on a HDD. A SSD is limited in its writing / reading - cycles. It's better for your SSD's health, to not store them on a HDD, especially if you use the buttons often.

Customization:

You can customize the code. Just copy and paste one of the datas entirely. You only need to change the scripting commands. You'll find an overview here:
https://manual.audacityteam.org/man/scripting_reference.html

Troubleshooting:

If you have any kind of problems, make sure to follow all the steps mentioned above. If you'll still have problems, try reading this article about Audacity Scripting:
https://manual.audacityteam.org/man/scripting.html

The testfile mentioned in the article isn't linked properly, as the Audacity-devs have restructured their Github-Repository. You'll find it here:
https://github.com/audacity/audacity/blob/master/au3/scripts/piped-work/pipe_test.py





Thx for reading. Have fun.

In the end, I hope, this module helps you.

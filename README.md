I should have written this a long time ago. 

This is a simple script that you can fork into the background on osx (If you want windows shit, you're asking the wrong person) that will effectively query your system processes and light up a blink(1) LED if you are in the middle of a zoom call. I use this to let people know around me to leave me alone. 

For this project, you will need a blink(1) LED that can be found here: https://blink1.thingm.com/

Once you have one of those, plug it in, run a pip install on this repo, and run the script forking it into the background. 

It's pretty simple. It's not perfect but I'm too lazy to write all of the exceptions/handling and it fulfills all of my requirements. 

If you want to improve this, feel free to fork it and make your own changes. If you have a suggestion, open a pull request and I will probably never get to it. 
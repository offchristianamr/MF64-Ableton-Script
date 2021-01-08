# MF64 - Ableton Control Surface Script (Live 11 Beta)
DJ Techtool's Midi Fighter 64 control surface script, created by padi04 with help from Jademalo, updated for use in Live 11 Beta by offchristianamr.

The aim of this version of the script is to adhere as closely as possible to the original, created for Ableton Live 9.7.
The most drastic change is removing the Colors.py and SkinDefault.py files entirely and instead calling the original versions from their respective directories.
The __init__.py file was updated to keep it more in line with other control scripts, but other than that, everything is kept as untouched as I could.

This version of the script fixes colors that were previously inaccurate and allows the script to load in Live 11 Beta.
Comments are left throughout the midi_fighter_64 script by myself which document all changes that I made, along with some information about the script.

-----
SETUP
-----

1. Copy the downloaded folder "Midi_Fighter_64" into your Ableton Live's MIDI Remote Scripts folder. 
Located in "C:\Program Files (x86)\Ableton\Live x.x\Resources\MIDI Remote Scripts\" under Windows or
"\Live x.x\Live.app\Contents\App-Resources\MIDI Remote Scripts\" for Mac OS X.

2. Launch Ableton Live and your device will be automatically detected.

Note: If your device isn't detected open the Preferences window. Under MIDI Sync tab select "Midi Fighter 64" in the Control Surface drop down list and set the correct input and output MIDI ports

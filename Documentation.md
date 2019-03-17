The Midi Fighter 64 remote script automatically maps the controller to Ableton Live's session view.
This allows you to quickly launch clips and perform other functions without MIDI mapping or manually adjusting the button colors.
It features four "modes" that have different functions, described in this document. Modes 1 and 4 are toggled while modes 2 and 3 must be held.

**To use this script, follow the README.md file for placing the folder in the correct directory. Addtionally, you must use the Midi Fighter Utility
and set the "Corner Button Bank Change" option to "Held." This switches between MIDI channel 3 and 2 when using the Midi Fighter 64 (if you set a MIDI
channel different to the default, bank 1 will be channel n and bank 2 will be channel n+1). 
When entering Live, hold the top right corner button to enter bank 2, which is now used for launching clips now that the script installed.
When you would like to return to the default functionality of the Midi Fighter 64, hold the top left button.**

Notes: for the sake of clarity, buttons will be labelled starting in the top left and moving left to right, 
NOT according to what MIDI notes they send. Follow them as you would reading a book. The colors mentioned in
this file are subject to change as I continue to work on the script. Changing modes will result in a message
saying "_mode# is active"

-----------------------------------------------------------------------------------------------------

GENERAL:

The first four dark green buttons correspond to the first four tracks.
The buttons underneath these correspond to any clips within these tracks in Live's session view.
The colors of these buttons roughly match the colors of the clips present.
Pressing these buttons launches the corresponding session clip.
Clips are orange as they are being quantized and dark red as they are playing 

-----------------------------------------------------------------------------------------------------

MODE 1:

Default mode. Button 5 is light blue when in this mode.
The first two buttons in the upper left switch between scenes 1-7 and 8-14.
Possible bug: If there are more than 14 scenes it will skip 8-14 and move to the bottom seven scenes instead.

-----------------------------------------------------------------------------------------------------

MODE 2:

Momentary mode.
Holding button 8 will cause all of column 8 to turn dark red.
Each row (buttons 16, 24, 32, 40, 48. 56, and 64) will play the corresponding master scene. 

-----------------------------------------------------------------------------------------------------

MODE 3:

Momentary mode.
Holding button 7 will cause the button to turn from light blue to dark red and rows 4-8 become colored.
**Clips cannot be launched while in mode three.**

ROW 4 - Blue - Switches between different tracks. The button corresponding to the currently selected track
is light green.

ROW 5 - Light Blue - Toggles tracks on and off. Off = dark blue.

ROW 6 - Pale Blue - Solos tracks. The button corresponding to the currently soloed track is light green.

ROW 7 - Dark Green - Record arms tracks. The button corresponding to the currently armed track is yellow.
Possible bug: Pressing multiple row 7 buttons quickly can arm multiple tracks. Pressing another button unarms them all.

ROW 8 - Pink - Stops tracks.

-----------------------------------------------------------------------------------------------------

MODE 4:

Press button 5 toggles between modes 1 and 4.
Button 5 is lime green when in this mode.
When mode 4 is active, pressing button 1 turns will cause it to turn yellow
and session record will toggle on. This is presumably for quickly recording DJ sets without touching the mouse.
This appears to be the only difference between modes 1 and 4.

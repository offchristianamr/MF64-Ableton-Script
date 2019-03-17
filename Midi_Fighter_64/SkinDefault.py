#Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/midi-remote-scripts/_APC/SkinDefault.py
from _Framework.Skin import Skin
from _Framework.ButtonElement import Color
from Colors import Rgb, Pulse, Blink
GREEN = Color(21)
RED = Color(5)
GREEN_BLINK_SLOW = Color(2)
RED_BLINK_SLOW = Color(4)
AMBER = Color(9)

class Defaults:

    class DefaultButton:
        On = Color(127)
        Off = Color(0)
        Disabled = Color(0)


class BiLedColors:

    class Session:
        ClipStopped = AMBER
        ClipStarted = GREEN
        ClipRecording = RED
        ClipTriggeredPlay = GREEN_BLINK_SLOW
        ClipTriggeredRecord = RED_BLINK_SLOW
        ClipEmpty = Color(0)
        Scene = Color(0)
        SceneTriggered = GREEN_BLINK_SLOW
        NoScene = Color(0)
        StopClip = Color(0)
        StopClipTriggered = GREEN_BLINK_SLOW
        RecordButton = Color(0)

    class Zooming:
        Selected = AMBER
        Stopped = RED
        Playing = GREEN
        Empty = Color(0)


class RgbColors:

    class Session:
        Scene = Rgb.GREEN
        SceneTriggered = Blink(Rgb.GREEN, Rgb.BLACK, 24)
        NoScene = Rgb.BLACK
        ClipStopped = Rgb.AMBER
        ClipStarted = Pulse(Rgb.GREEN, Rgb.BLACK, 48)
        ClipRecording = Pulse(Rgb.BLACK, Rgb.RED, 48)
        ClipTriggeredPlay = Blink(Rgb.GREEN, Rgb.BLACK, 24)
        ClipTriggeredRecord = Blink(Rgb.RED, Rgb.BLACK, 24)
        ClipEmpty = Rgb.BLACK
        RecordButton = Rgb.BLACK

    class Zooming:
        Selected = Rgb.AMBER
        Stopped = Rgb.RED
        Playing = Rgb.GREEN
        Empty = Rgb.BLACK


def make_default_skin():
    return Skin(Defaults)


def make_biled_skin():
    return Skin(BiLedColors)


def make_rgb_skin():
    return Skin(RgbColors)

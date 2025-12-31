import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# Macros
macros = Macros()
keyboard.modules.append(macros)

# Encoder
encoder = EncoderHandler()
keyboard.modules.append(encoder)

# -------- MACROS --------

COPY = KC.MACRO(
    [
        Press(KC.LEFT_CTRL),
        Tap(KC.C),
        Release(KC.LEFT_CTRL),
    ]
)

PASTE = KC.MACRO(
    [
        Press(KC.LEFT_CTRL),
        Tap(KC.V),
        Release(KC.LEFT_CTRL),
    ]
)

SCREENSHOT = KC.MACRO(
    [
        Press(KC.LEFT_CMD),
        Press(KC.LEFT_SHIFT),
        Tap(KC.N4),
        Release(KC.LEFT_SHIFT),
        Release(KC.LEFT_CMD),
    ]
)

UNDO = KC.MACRO(
    [
        Press(KC.LEFT_CMD),
        Tap(KC.Z),
        Release(KC.LEFT_CMD),
    ]
)

REDO = KC.MACRO(
    [
        Press(KC.LEFT_CMD),
        Tap(KC.Y),
        Release(KC.LEFT_CMD),
    ]
)

NEWTAB = KC.MACRO(
    [
        Press(KC.LEFT_CMD),
        Tap(KC.T),
        Release(KC.LEFT_CMD),
    ]
)

# -------- PINS --------

PINS = [
    board.D0,
    board.D1,
    board.D2,
    board.D3,
    board.D4,
    board.D5,
    board.D6,   # encoder push button
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Encoder rotation pins + button
encoder.pins = (
    (board.D7, board.D8, board.D6, False),
)

# -------- KEYMAP --------)

keyboard.keymap = [
    [
        COPY,        # D0
        PASTE,       # D1
        SCREENSHOT,  # D2
        UNDO,        # D3
        REDO,        # D4
        NEWTAB,      # D5
        KC.MUTE,       # D6 
    ]
]

# -------- ENCODER MAP --------
encoder.map = [
    ((KC.VOLD, KC.VOLU),)
]

if __name__ == '__main__':
    keyboard.go()

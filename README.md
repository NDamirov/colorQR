# colorQR
Attempt to make QR code with 4 colors. \
Field with size 23x23: 4 squares 8x8 for detection, 255 squares for 64 byte-blocks, at least 10 of them are Reed-Solomon additional code (9% error, 54 UTF-8 characters), 3 squares for mode (max 1 error), 4 groups of 3 squares for length of message (max 1 error in each group).
## Instruction
To decode use `python decode.py` (decodes 'temp.png') \
To encode use `python encode.py`, type value doesn't matter for now.
## Examples
![Black and white version](https://github.com/NDamirov/colorQR/blob/master/black_white.png?raw=true)
![Colorful version](https://github.com/NDamirov/colorQR/blob/master/colors.png?raw=true)

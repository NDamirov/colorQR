# colorQR
Attempt to make QR code with 4 colors. \
Field with size 23x23: 4 squares 8x8 for detection, 255 squares for 64 byte-blocks, 10 of them Reed-Solomon additional code (9% error, 54 UTF-8 characters), 3 squares for mode (xor operation for check). 
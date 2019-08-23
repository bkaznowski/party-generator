# Party emoji generator
This tool makes slack party emojis. It can convert all files ending with jpg, jpeg, png. It resizes the image to 100x100 so it fits slacks size restrictions.

### Before:
![](/input_data/Portrait_Placeholder.jpg)  
![](/input_data/download.jpeg)

### After:

![](/output_data/Portrait_Placeholder.jpg.gif)  
![](/output_data/download.jpeg.gif)


## Requirements
- Must have docker installed

## How to use
1. Place files in input_data (must end with .jpg)
2. Execute `./run.sh`. Sudo may be required for docker.
3. Retrieve gifs from output_data

## Issues
* It doesn't handle transparency properly. Currently, it replaces solid black, solid white and transparent pixels with white (no color variation).

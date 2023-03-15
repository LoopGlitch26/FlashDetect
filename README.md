# Project Title: Photosensitive Detection Algorithm Using Adaptive Thresholding and Contrast Analysis

Photosensitive epilepsy is a neurological disorder that affects a small percentage of the population. People with this disorder experience seizures triggered by visual stimuli such as flashing lights or contrasting light and dark patterns. To prevent triggering seizures, videos with photosensitive content should be identified and flagged. However, manually reviewing videos is time-consuming and costly. Therefore, an automated algorithm for detecting videos with photosensitive content is necessary.

The algorithm described is a photosensitive detection algorithm that analyzes a video for flashing lights or contrasting light and dark patterns. The algorithm uses OpenCV, NumPy, Matplotlib, and the YouTube API to read frames from a YouTube video, convert them to grayscale, and apply adaptive thresholding to the frames.

# Result:
[Example](https://youtu.be/pOnwPiL42Qw) 

![Screenshot 2023-03-14 at 6 33 16 PM](https://user-images.githubusercontent.com/53336715/225009417-476d9dbc-c3b6-444d-aedc-4f51b89a7515.png)

# FlashDetect Package

FlashDetect is a Python package for detecting the presence of a flash in a video. It is built on top of OpenCV and PyTube.

## Installation

`pip install git+https://github.com/LoopGlitch26/FlashDetect.git`

## Usage

```
import flashdetect
url = ''  # Insert Video Link
result = flashdetect.analyze_video(url)
print(result)
```

## Contributing

If you find a bug or have a suggestion for a new feature, please submit an issue on GitHub. Pull requests are also welcome!

## License

FlashDetect is licensed under the MIT License. See the LICENSE file for more information.




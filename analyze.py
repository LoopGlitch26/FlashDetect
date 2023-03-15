import os
import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
from pytube import YouTube

def analyze_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()

    cap = cv2.VideoCapture(stream.url)

    contrasts = []
    frame_nums = []

    frame_num = 0

    block_size = 33
    std_threshold = 30

    num_flashing_frames = 0
    num_contrasting_frames = 0

    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, std_threshold)
        
        num_white_pixels = np.sum(adaptive_thresh == 255)
        
        if num_white_pixels >= 0.2 * gray.size:
            num_flashing_frames += 1
        if num_white_pixels <= 0.8 * gray.size:
            num_contrasting_frames += 1

        contrast = np.std(gray) / np.mean(gray)

        contrasts.append(contrast)
        frame_nums.append(frame_num)

        frame_num += 1

    end_time = time.time()

    execution_time = end_time - start_time

    num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    flashing_lights = num_flashing_frames >= 0.2 * num_frames
    contrasting_patterns = num_contrasting_frames >= 0.2 * num_frames

    cap.release()

    return {
        'execution_time': execution_time,
        'flashing_lights': flashing_lights,
        'contrasting_patterns': contrasting_patterns,
        'frame_nums': frame_nums,
        'contrasts': contrasts,
    }

def plot_contrasts(frame_nums, contrasts):
    plt.plot(frame_nums, contrasts)
    plt.xlabel("Frame Number")
    plt.ylabel("Contrast")
    plt.show()

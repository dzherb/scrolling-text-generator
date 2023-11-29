import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def create_scrolling_text(text, font_path, font_size,
                          file_path='scrolling_text.mp4',
                          image_width=100, image_height=100, fps=30,
                          direction='left', duration=3):
    """
    Makes a video with scrolling text.
    Saves mp4 file to the file_path.
    """
    text_color = (255, 255, 255)
    bg_color = (0, 50, 50)

    font = ImageFont.truetype(font_path, font_size)

    # Get text size in pixels
    _, _, text_width, text_height = font.getbbox(text)

    # Amount of frames
    num_frames = duration * fps
    # Text speed
    speed = (text_width + 2*image_width) / num_frames

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(file_path, fourcc, fps, (image_width, image_height))

    # Make each frame and then unite all of them as a video
    for i in range(num_frames):
        img = Image.new("RGB", (image_width, image_height), bg_color)
        draw = ImageDraw.Draw(img)

        if direction == 'left':
            x = image_width - int(i * speed)
        elif direction == 'right':
            x = -(image_width - int(i * speed))
        else:
            raise ValueError("Invalid direction. Choose either 'left' or 'right'.")

        y = (image_height - text_height) // 2
        draw.text((x, y), text, font=font, fill=text_color)

        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        video_writer.write(frame)

    video_writer.release()

if __name__ == '__main__':
    text = "Scrolling text"
    font_path = "arial.ttf"
    font_size = 55
    duration = 3  # Продолжительность видео в секундах

    create_scrolling_text(text, font_path, font_size, duration=duration)

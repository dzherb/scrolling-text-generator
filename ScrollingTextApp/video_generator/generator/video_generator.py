import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def create_scrolling_text(text='No input :(', font_path='video_generator/generator/fonts/arial.ttf', font_size=55,
                          file_path='test.mp4', frame_size=(100, 100),
                          bg_color=(200, 60, 50), text_color=(255, 255, 255),
                          duration=3, direction='left', fps=30):
    """
    Makes a video with scrolling text.
    Saves mp4 file to the file_path.
    """
    image_width, image_height = frame_size
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
            x = 0 - text_width + int(i * speed)
        else:
            raise ValueError("Invalid direction. Choose either 'left' or 'right'.")

        y = (image_height - text_height) // 2
        draw.text((x, y), text, font=font, fill=text_color)

        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        video_writer.write(frame)

    video_writer.release()

if __name__ == '__main__':
    text = "Scrolling text"

    create_scrolling_text(text, direction='right')

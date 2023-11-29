import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def create_scrolling_text_video(text, font_path, font_size,
                                output_file='video/scrolling_text.mp4',
                                width=100, height=100, fps=30,
                                direction='left', duration=3):
    """
    Makes a video with scrolling text.
    Returns mp4 file.
    """
    image_width = width
    image_height = height
    text_color = (255, 255, 255)  # Цвет текста
    bg_color = (0, 50, 50)  # Цвет фона

    font = ImageFont.truetype(font_path, font_size)

    # Размеры текста в пикселях
    _, _, text_width, text_height = font.getbbox(text)

    # Количество кадров
    num_frames = duration * fps
    # Скорость смещения текста - (длина строки + двойная ширина кадра) / кол-во кадров
    speed = (text_width + 2*image_width) / num_frames

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, (image_width, image_height))

    # Создаем кадры
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

        # Запись кадра в итоговое видео
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        video_writer.write(frame)

    video_writer.release()

if __name__ == '__main__':
    text = "Пример движущегося текста..."
    font_path = "arial.ttf"
    font_size = 55
    duration = 3  # Продолжительность видео в секундах

    create_scrolling_text_video(text, font_path, font_size, duration=duration)

from PIL import Image
import os

class ImageProcessor:
    @staticmethod
    def resize(source_path, target_path, width, height):
        with Image.open(source_path) as img:
            img = img.resize((width, height), Image.LANCZOS)
            img.save(target_path)
        return target_path

    @staticmethod
    def thumbnail(source_path, target_path, size=(128, 128)):
        with Image.open(source_path) as img:
            img.thumbnail(size)
            img.save(target_path)
        return target_path

    @staticmethod
    def compress(source_path, target_path, quality=85):
        with Image.open(source_path) as img:
            img.save(target_path, optimize=True, quality=quality)
        return target_path

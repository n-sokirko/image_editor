import os

# ...

def save_image(self, pixmap, index):
    if not os.path.exists("output"):
        os.makedirs("output")
    file_path = f"output/image_{index}.png"
    pixmap.save(file_path, "PNG")
    print(f"Image saved: {file_path}")

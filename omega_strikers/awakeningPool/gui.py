import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# TODO: Tie object detection to gui display

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.image_labels = []

        self.open_button = tk.Button(root, text="Open Images", command=self.open_images)
        self.open_button.grid()

    def open_images(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if file_paths:
            for image_path in file_paths:
                self.show_image(image_path)

    def show_image(self, image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self.root, image=photo)
        label.photo = photo  # To prevent image from being garbage collected
        label.grid(row=len(self.image_labels) // 8, column=len(self.image_labels) % 8)
        self.image_labels.append(label)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()

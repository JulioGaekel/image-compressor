import os
from tkinter import Tk, Label, Button, filedialog, messagebox
from PIL import Image

# Create output folder if it does not exist
OUTPUT_DIR = "compressed_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def compress_image(input_path, quality=60, max_size=(1024, 1024)):
    try:
        img = Image.open(input_path)

        # Resize image if larger than max_size
        img.thumbnail(max_size)

        # Extract filename and creat output path
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = os.path.join(OUTPUT_DIR, f"{name}_compressed{ext}")

        # Save compressed image
        img.save(output_path, optimize=True, quality=quality)
        messagebox.showinfo("Success", f"Image saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_image():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.webp")]
    )
    if file_path:
        compress_image(file_path)

# GUI
root = Tk()
root.title("Simple Image Compressor")
root.geometry("300x150")

label = Label(root, text="Click to select an image to compress:")
label.pack(pady=10)

select_button = Button(root, text="Select Image", command=select_image)
select_button.pack(pady=10)

root.mainloop()

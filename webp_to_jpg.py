import os
from tkinter import Tk, Button, Label, filedialog, messagebox
from PIL import Image

class WebPToJPGConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("WebP to JPG Converter")
        self.root.geometry("420x220")
        self.root.resizable(False, False)

        self.input_dir = ""
        self.output_dir = ""

        Label(root, text="WebP → JPG Batch Converter", font=("Arial", 14, "bold")).pack(pady=10)

        Button(root, text="Select Input Folder", width=25, command=self.select_input).pack(pady=5)
        Button(root, text="Select Output Folder", width=25, command=self.select_output).pack(pady=5)

        Button(root, text="Convert Images", width=25, bg="#4CAF50", fg="white",
               command=self.convert_images).pack(pady=15)

    def select_input(self):
        self.input_dir = filedialog.askdirectory(title="Select WebP Folder")
        if self.input_dir:
            messagebox.showinfo("Selected", f"Input Folder:\n{self.input_dir}")

    def select_output(self):
        self.output_dir = filedialog.askdirectory(title="Select Output Folder")
        if self.output_dir:
            messagebox.showinfo("Selected", f"Output Folder:\n{self.output_dir}")

    def convert_images(self):
        if not self.input_dir or not self.output_dir:
            messagebox.showerror("Error", "Please select both folders.")
            return

        converted = 0

        for file in os.listdir(self.input_dir):
            if file.lower().endswith(".webp"):
                webp_path = os.path.join(self.input_dir, file)
                jpg_path = os.path.join(
                    self.output_dir,
                    os.path.splitext(file)[0] + ".jpg"
                )

                try:
                    img = Image.open(webp_path)

                    # Handle transparency
                    if img.mode == "RGBA":
                        background = Image.new("RGB", img.size, (255, 255, 255))
                        background.paste(img, mask=img.split()[3])
                        background.save(jpg_path, "JPEG", quality=95)
                    else:
                        img.convert("RGB").save(jpg_path, "JPEG", quality=95)

                    converted += 1

                except Exception as e:
                    messagebox.showerror("Error", f"Failed to convert {file}\n{e}")
                    return

        messagebox.showinfo("Done", f"✅ Converted {converted} images successfully!")


if __name__ == "__main__":
    root = Tk()
    app = WebPToJPGConverter(root)
    root.mainloop()

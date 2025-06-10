import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from PIL import Image, ImageTk
import pytesseract
import os

# Set the path to the Tesseract executable
# If you haven't installed Tesseract, you'll need to do that first.
# For Windows, it's typically 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# For macOS/Linux, it's usually in your PATH.
# You might need to adjust this path based on your installation.
try:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
except Exception:
    # Fallback for other OS or if not found in default path
    # You might need to add a try-except block or user input for the path
    pass


class TesseractOCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tesseract OCR Image to Text")
        self.root.geometry("800x700")

        # --- Top Frame for Image Display and Browse Button ---
        self.top_frame = tk.Frame(root, bd=2, relief="groove")
        self.top_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.image_label = tk.Label(self.top_frame, text="No image loaded", bg="lightgray")
        self.image_label.pack(pady=10, fill="both", expand=True)

        self.browse_button = tk.Button(self.top_frame, text="Browse Image", command=self.browse_image)
        self.browse_button.pack(pady=5)

        # --- Bottom Frame for Text Output ---
        self.bottom_frame = tk.Frame(root, bd=2, relief="groove")
        self.bottom_frame.pack(pady=10, padx=10, fill="both", expand=False) # Don't expand vertically for this frame

        self.text_label = tk.Label(self.bottom_frame, text="Extracted Text:")
        self.text_label.pack(pady=5)

        self.text_output = scrolledtext.ScrolledText(self.bottom_frame, wrap=tk.WORD, width=90, height=20)
        self.text_output.pack(pady=5)

        self.current_image_path = None

    def browse_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an image file",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff")]
        )
        if file_path:
            self.current_image_path = file_path
            self.display_image(file_path)
            self.extract_text(file_path)

    def display_image(self, file_path):
        try:
            img = Image.open(file_path)
            # Resize image to fit in the label while maintaining aspect ratio
            img.thumbnail((400, 300)) # Max width 400, max height 300
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk  # Keep a reference!
            self.image_label.config(text="") # Clear "No image loaded" text
        except Exception as e:
            messagebox.showerror("Image Error", f"Could not load image: {e}")
            self.image_label.config(text="Error loading image")

    def extract_text(self, image_path):
        self.text_output.delete(1.0, tk.END) # Clear previous text
        try:
            text = pytesseract.image_to_string(Image.open(image_path))
            self.text_output.insert(tk.END, text)
        except pytesseract.TesseractNotFoundError:
            messagebox.showerror(
                "Tesseract Error",
                "Tesseract is not installed or not in your PATH. "
                "Please install Tesseract OCR and ensure its executable path is correctly set."
            )
            self.text_output.insert(tk.END, "Error: Tesseract OCR not found. Please install it.")
        except Exception as e:
            messagebox.showerror("OCR Error", f"An error occurred during OCR: {e}")
            self.text_output.insert(tk.END, f"Error during OCR: {e}")

# --- Main execution ---
if __name__ == "__main__":
    # Check if pytesseract is installed
    try:
        import pytesseract
    except ImportError:
        messagebox.showerror("Missing Module", "The 'pytesseract' module is not installed.\n"
                                               "Please install it using: pip install pytesseract pillow")
        exit()

    # Check if PIL (Pillow) is installed
    try:
        from PIL import Image, ImageTk
    except ImportError:
        messagebox.showerror("Missing Module", "The 'Pillow' module is not installed.\n"
                                               "Please install it using: pip install pillow")
        exit()

    root = tk.Tk()
    app = TesseractOCRApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def encrypt_image():
    image_path = filedialog.askopenfilename()
    if image_path:
        # Open the image
        img = Image.open(image_path)
        width, height = img.size

        # Create a new blank image with the same size
        encrypted_img = Image.new("RGB", (width, height))

        # Loop through each pixel
        for x in range(width):
            for y in range(height):
                # Get the RGB values of the pixel
                r, g, b = img.getpixel((x, y))
                # Swap the red and blue channels
                encrypted_img.putpixel((x, y), (b, g, r))

        # Save the encrypted image
        encrypted_img_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if encrypted_img_path:
            encrypted_img.save(encrypted_img_path)
            messagebox.showinfo("Success", "Image encrypted successfully!")
    else:
        messagebox.showwarning("Warning", "Please select an image file.")

def decrypt_image():
    image_path = filedialog.askopenfilename()
    if image_path:
        # Open the encrypted image
        encrypted_img = Image.open(image_path)
        width, height = encrypted_img.size

        # Create a new blank image with the same size
        decrypted_img = Image.new("RGB", (width, height))

        # Loop through each pixel
        for x in range(width):
            for y in range(height):
                # Get the RGB values of the pixel
                r, g, b = encrypted_img.getpixel((x, y))
                # Swap the red and blue channels back
                decrypted_img.putpixel((x, y), (b, g, r))

        # Save the decrypted image
        decrypted_img_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if decrypted_img_path:
            decrypted_img.save(decrypted_img_path)
            messagebox.showinfo("Success", "Image decrypted successfully!")
    else:
        messagebox.showwarning("Warning", "Please select an image file.")

# Create main window
root = tk.Tk()
root.title("Image Encryption Tool")

# Create buttons for encryption and decryption
button_encrypt = tk.Button(root, text="Encrypt Image", command=encrypt_image)
button_encrypt.pack(pady=10)
button_decrypt = tk.Button(root, text="Decrypt Image", command=decrypt_image)
button_decrypt.pack(pady=10)

root.mainloop()

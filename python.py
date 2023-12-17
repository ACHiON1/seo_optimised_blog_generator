
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import openai
from PIL import Image, ImageDraw, ImageFont
import os
import tkinter as tk
from tkinter import filedialog

# Set your OpenAI API key
openai.api_key = "your_openai_api_key_here"  # Replace with your actual OpenAI API key

class EmailGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Email Generator App")

        self.prompt_label = tk.Label(master, text="Enter Email Prompt:")
        self.prompt_label.pack()

        self.prompt_entry = tk.Entry(master, width=50)
        self.prompt_entry.pack()

        self.image_button = tk.Button(master, text="Select Image", command=self.load_image)
        self.image_button.pack()

        self.generate_button = tk.Button(master, text="Generate and Send Email", command=self.generate_and_send_email)
        self.generate_button.pack()

        self.image_path = ""

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    def generate_and_send_email(self):
        prompt = self.prompt_entry.get()

        if not prompt:
            tk.messagebox.showwarning("Warning", "Please enter an email prompt.")
            return

        if not self.image_path:
            tk.messagebox.showwarning("Warning", "Please select an image.")
            return

        # ... (rest of the code remains unchanged)

def main():
    root = tk.Tk()
    app = EmailGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# Set your OpenAI API key
openai.api_key = "your_openai_api_key_here"  # Replace with your actual OpenAI API key

# Set your email credentials and server details
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "your_email@example.com"
smtp_password = "your_email_password"

def generate_email_content(prompt):
    # Use the OpenAI API to generate email content based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response["choices"][0]["text"]

def arrange_image_in_template(image_path, prompt):
    # Load image
    image = Image.open(image_path)

    # Create a new image with a white background
    width, height = 800, 600
    template = Image.new("RGB", (width, height), "white")

    # Paste the original image onto the template
    template.paste(image, (50, 50))

    # Draw the prompt text on the template
    draw = ImageDraw.Draw(template)
    font = ImageFont.load_default()  # You can use a specific font if needed
    draw.text((50, height - 50), prompt, font=font, fill="black")

    return template

def send_email(subject, body, to_email, smtp_server, smtp_port, smtp_username, smtp_password, attachment_path=None):
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            img = MIMEImage(attachment.read(), name=os.path.basename(attachment_path))
            msg.attach(img)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())

def main():
    # Sample email dataset
    email_dataset = [
        {"email": "recipient1@example.com", "name": "Recipient 1"},
        {"email": "recipient2@example.com", "name": "Recipient 2"},
        # Add more recipients as needed
    ]

    # Image and prompt details
    image_path = "your_image.jpg"  # Replace with your image path
    prompt = "Write your prompt here for generating email content using OpenAI."

    for recipient in email_dataset:
        # Generate email content using OpenAI API
        email_content = generate_email_content(prompt)

        # Arrange image in the template
        arranged_image = arrange_image_in_template(image_path, email_content)

        # Save the arranged image with a unique name
        arranged_image_path = f"arranged_image_{recipient['name']}.png"
        arranged_image.save(arranged_image_path)

        # Send email
        send_email(
            subject="Generated Email Subject",
            body=f"Dear {recipient['name']},\n\n{email_content}\n\nBest regards,\nYour Name",
            to_email=recipient["email"],
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            smtp_username=smtp_username,
            smtp_password=smtp_password,
            attachment_path=arranged_image_path
        )

        # Remove the temporary arranged image file
        os.remove(arranged_image_path)

if __name__ == "__main__":
    main()

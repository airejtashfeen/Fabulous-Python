from PIL import Image, ImageDraw, ImageFont

# Create a blank white image
width, height = 800, 600
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Load fonts
# Update these paths to the location of your downloaded fonts
montserrat_font_path = "/Users/airejtashfeen/Desktop/Fabulous Python/fonts/Montserrat-Bold.ttf"  # Path to Montserrat Bold font
open_sans_font_path = "/Users/airejtashfeen/Desktop/Fabulous Python/fonts/OpenSans-Regular.ttf"  # Path to Open Sans Regular font

montserrat_font = ImageFont.truetype(montserrat_font_path, 40)
montserrat_subheader_font = ImageFont.truetype(montserrat_font_path, 30)
open_sans_font = ImageFont.truetype(open_sans_font_path, 20)
button_font = ImageFont.truetype(montserrat_font_path, 25)

# Define colors
primary_blue = "#007BFF"
secondary_green = "#28A745"
dark_grey = "#333333"
white = "#FFFFFF"

# Add header text
header_text = "Introducing Smart Village"
draw.text((50, 50), header_text, font=montserrat_font, fill=primary_blue)

# Add subheader text
subheader_text = "A Sustainable Future"
draw.text((50, 120), subheader_text, font=montserrat_subheader_font, fill=secondary_green)

# Add body text
body_text = (
    "Smart Village leverages modern technologies to improve rural life\n"
    "and promote sustainability. It includes smart agriculture, renewable\n"
    "energy, e-governance, and more, creating a connected and efficient\n"
    "community."
)
draw.multiline_text((50, 180), body_text, font=open_sans_font, fill=dark_grey)

# Add call-to-action button
button_text = "Learn More"
button_x, button_y, button_w, button_h = 50, 400, 200, 50
draw.rectangle([button_x, button_y, button_x + button_w, button_y + button_h], fill=primary_blue)
text_bbox = draw.textbbox((0, 0), button_text, font=button_font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
text_x = button_x + (button_w - text_width) // 2
text_y = button_y + (button_h - text_height) // 2
draw.text((text_x, text_y), button_text, font=button_font, fill=white)

# Save the image to a file
image_path = "smart_village_post.png"
image.save(image_path)

print(f"Image saved as {image_path}")

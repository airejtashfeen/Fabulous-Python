from rembg import remove
from PIL import Image

# Can be any image's path ofc
input_path = '/Users/airejtashfeen/Desktop/Fabulous Python/images/lion.jpeg'

#The output path that you want
output_path = '/Users/airejtashfeen/Desktop/Fabulous Python/images/lionwithoutbackground.jpeg'

input_image = Image.open(input_path)

output_image = remove(input_image)

output_image = output_image.convert("RGB")

output_image.save(output_path)

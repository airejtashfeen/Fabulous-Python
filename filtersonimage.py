from PIL import Image, ImageFilter

# Open an image
image = Image.open('images/lion.jpeg')

# Filters being applied
blurred_image = image.filter(ImageFilter.BLUR)
detail_image = image.filter(ImageFilter.DETAIL)
edge_enhance_image = image.filter(ImageFilter.EDGE_ENHANCE)

# Saving the filtered images
blurred_image.save('images/blurred_lion.jpeg')
detail_image.save('images/detailed_lion.jpeg')
edge_enhance_image.save('images/enhanced_lion.jpeg')

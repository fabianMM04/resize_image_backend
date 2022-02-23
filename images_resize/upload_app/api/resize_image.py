from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files import File

def resize_image(file):
    image_name = file.name
    img = Image.open(file)  # Catch original
    if img.width > img.height:
        image_orientation = "Horizontal"
    else:
        image_orientation = "Vertical"
    while(True):
        
        if img.width > 796 or img.height > 1123:
            img = img.resize((img.width//2, img.height//2))
        else:
            break
        
        
            
    output = BytesIO()
    img.save(output, format='JPEG')
    output.seek(0)
    content_file = ContentFile(output.read())  # Read output and create ContentFile in memory
    file = File(content_file)
    return file, image_name, image_orientation
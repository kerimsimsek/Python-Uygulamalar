from rembg import remove
from PIL import Image
image_input = Image.open("C:/Users/gfbke/Desktop/Proje/background-remove/a.jpg")
output = remove(image_input)
output.save("C:/Users/gfbke/Desktop/Proje/background-remove/a.png")
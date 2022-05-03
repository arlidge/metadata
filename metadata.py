from PIL import Image, PngImagePlugin

from colorama import colorama_text, Fore, Back, Style
import pyfiglet
import base64

result = pyfiglet.figlet_format("Meta", font = "poison"  )
print(Fore.YELLOW+result)

print(Fore.RED+'This will add metadata to a specified image file.'+Fore.RESET)

info = PngImagePlugin.PngInfo()

message = input('String to encode into image ')
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

#user = input('Text to add to image ')
info.add_text("text", base64_message)
info.add_text("ZIP", "VALUE", zip=True)
name = input('name file ')
current = input('current image name ')
im = Image.open(current)
im.save(name, "PNG",optimize=False, pnginfo=info, compress_level=0)

print(Fore.RED+base64_message+Fore.RESET)

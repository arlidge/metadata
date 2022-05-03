from PIL import Image, PngImagePlugin
import base64
from colorama import colorama_text, Fore, Back, Style
import pyfiglet
import subprocess

result = pyfiglet.figlet_format("Read", font = "poison"  )
print(Fore.YELLOW+result)

print(Fore.RED+'This will read metadata from a specified image file.'+Fore.RESET)

user = input('image name ')
im3 = Image.open(user)
print(Fore.RED+im3.info["text"]+Fore.RESET)
print(Fore.BLUE+'The string has been copied to your clipboard'+Fore.RESET)
subprocess.run("pbcopy", universal_newlines=True, input=im3.info["text"])

base64_message = input('String to decode ')
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(Fore.GREEN+message+Fore.RESET)

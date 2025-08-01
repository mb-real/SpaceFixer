import unicodedata
import pyperclip
import re

# === Aim ===
# متن کپی شده از کلیپ برد را دریافت کنید
# Get the copied text from the clipboard
# نتیجه را در کلیپ برد قرار دهید
# Paste the result back in the clipboard
# تغغیرات را اعمال کنید
# Apply changes

class processText:
    def __init__(self):
        self.text = pyperclip.paste()
        
    def removeSpaces(self):
        self.text = re.sub(r"[\r\n]", " ", self.text)
        self.text = re.sub(r"\s+", " ", self.text)
        pyperclip.copy(self.text)

    def toVerticalText(self, form="NFKC"):
        vtext = ""
        if unicodedata.is_normalized(form, self.text):
            print("Text is already normal.")
            return
        else:
            for i in self.text:
                vtext += unicodedata.normalize(form, i)
            print("Text normalized.")
            pyperclip.copy(vtext)
            return vtext

    def ask(self):
        while True:
            ask = input("Do you want to display the result? (y)es/(n)o: ")
            ask = ask.lower()
            if ask.startswith('y'):
                print(self.text)
                break
            elif ask.startswith('n'):
                break
            else:
                print("Invalid option.")
                continue

p = processText()
p.removeSpaces()
p.toVerticalText()
p.ask()
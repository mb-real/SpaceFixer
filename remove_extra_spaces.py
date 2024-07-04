
import pyperclip




# متن کپی شده از کلیپ برد را دریافت کنید
text = pyperclip.paste()

# تغغیرات را اعمال کنید

text = text.replace('\r', ' ')
text = text.replace('\n', ' ')


text = text.replace('  ', ' ')
text = text.replace('   ', ' ')
text = text.replace('    ', ' ')
text = text.replace('     ', ' ')
text = text.replace('      ', ' ')
text = text.replace('       ', ' ')
text = text.replace('         ', ' ')


###print(text)


# نتیجه را در کلیپ برد قرار دهید
pyperclip.copy(text)



SpaceFixer
=========
A simple code that removes extra space and text inters from the text copied to the clipboard and replaces them with a single space.

## Why
When you copy text from a website or `.pdf` file into a language other than your original language, you may encounter the problem of extra spaces and unnecessary inters in the text. This can make Google Translate difficult and lead to incorrect results.
This Python program solves this problem by removing extra spaces and unnecessary inters from the copied text.

## How to use
1. Copy the text you want.
2. Run the program in `cmd` or bash terminal:
```bash
python main.py
```
## Example
### Copied text:
```
言爸犬朋。          斥亭能行念把安以外眼生出，院貫歌高平會知送位寫尺記象發，筆爪久兄麼七色習同，蝶動到昔：                    荷巴東穴嗎停己是洋請呢室飽的童白做隻。     전직대통령의 신분과 예우에 관하여는          법률로 정한다.                 𝔄 𝖖𝖚𝖎𝖈𝖐 𝙗𝙧𝙤𝙬𝙣 𝓯𝓸𝔁 𝒿𝓊𝓂𝓅𝑒𝒹 𝕠𝕧𝕖𝕣 ｔｈｅ 𝗹𝗮𝘇𝘆 ᵈᵒᵍ.
```
### Result:
```
言爸犬朋。 斥亭能行念把安以外眼生出,院貫歌高平會知送位寫尺記象發,筆爪久兄麼七色習同,蝶動到昔: 荷巴東穴嗎停己是洋請呢室飽的童白做隻。 전직대통령의 신분과 예우에 관하여는 법률로 정한다. A quick brown fox jumped over the lazy dog.
```

## TODO
- [x] Improvements for vertical languages like Chinese, Vietnamese, Korean, and Japanese are written vertically in columns going from top to bottom and ordered from right to left, with each new column starting to the left of the preceding one.
- [x] Checking the correct operation of the program in different text formats and fonts and other possible methods of text confusion {utf-8}.
- [ ] Writing tests for the program.
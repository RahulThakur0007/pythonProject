import qrcode as qr 

img = qr.make("https://chat.openai.com/")
img.save("chatgpt.png")
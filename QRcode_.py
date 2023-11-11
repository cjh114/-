import tkinter as tk
import qrcode
from PIL import ImageTk

def generate_qr_code():
    link = link_entry.get()
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img = qr_img.resize((200, 200))
    qr_img_tk = ImageTk.PhotoImage(qr_img)
    
    qr_label.config(image=qr_img_tk)
    qr_label.image = qr_img_tk

# GUI 생성
root = tk.Tk()
root.title("QR Code Generator")

# 링크 입력 위젯과 버튼 생성
link_entry = tk.Entry(root, width=40)
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)

# QR 코드 이미지를 표시할 라벨 생성
qr_label = tk.Label(root)

# 위젯 배치
link_entry.pack(pady=10)
generate_button.pack(pady=5)
qr_label.pack()

root.mainloop()

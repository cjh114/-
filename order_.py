import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

class ChineseRestaurantVendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("중국집 자판기")
        self.root.geometry("800x600")  # 화면 크기 설정

        self.menu = {
            "짜장면": {"price": 6000, "quantity": 5, "image": "jjm.png"},
            "짬뽕": {"price": 7000, "quantity": 5, "image": "jjp.png"},
            "탕수육": {"price": 12000, "quantity": 5, "image": "ts.png"},
            "볶음밥": {"price": 8000, "quantity": 5, "image": "bb.png"}
        }

        self.balance = 1000000  # 초기 잔액 설정
        self.cart = {}

        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack()

        for item in self.menu.keys():
            image = Image.open(self.menu[item]['image'])
            image = image.resize((50, 50), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            label = tk.Label(self.menu_frame, text=item, image=photo, compound="top")
            label.photo = photo
            label.grid(row=list(self.menu.keys()).index(item), column=0, padx=20)

            info_label = tk.Label(self.menu_frame, text=f"{self.menu[item]['price']}원 - {self.menu[item]['quantity']}개 남음")
            info_label.grid(row=list(self.menu.keys()).index(item), column=1, padx=20)

            button = tk.Button(self.menu_frame, text="장바구니에 담기", command=lambda i=item: self.add_to_cart(i))
            button.grid(row=list(self.menu.keys()).index(item), column=2, padx=20)

        self.balance_label = tk.Label(root, text=f"잔액: {self.balance} 원")
        self.balance_label.pack()

        self.buy_button = tk.Button(root, text="구매하기", command=self.purchase_items)
        self.buy_button.pack()

        self.clear_cart_button = tk.Button(root, text="장바구니 초기화", command=self.clear_cart)
        self.clear_cart_button.pack()

        self.cart_frame = tk.Frame(root)
        self.cart_frame.pack()

        self.cart_label = tk.Label(root, text="장바구니:")
        self.cart_label.pack()

        self.cart_listbox = tk.Listbox(root)
        self.cart_listbox.pack()

        self.total_price_label = tk.Label(root, text="총 가격: 0 원")
        self.total_price_label.pack()

        self.update_cart_label()

    def add_to_cart(self, menu_item):
        if self.menu[menu_item]['quantity'] > 0:
            if menu_item in self.cart:
                self.cart[menu_item] += 1
            else:
                self.cart[menu_item] = 1
            self.menu[menu_item]['quantity'] -= 1
            self.update_cart_label()
            self.update_menu_labels()
            self.update_total_price_label()
        else:
            messagebox.showinfo("품절", f"{menu_item}은(는) 품절되었습니다.")

    def purchase_items(self):
        total_price = sum(self.menu[item]['price'] * self.cart[item] for item in self.cart)
        if total_price <= self.balance:
            self.balance -= total_price
            self.cart.clear()  # 장바구니 초기화
            self.update_cart_label()
            self.balance_label.config(text=f"잔액: {self.balance} 원")
            self.update_menu_labels()
            self.update_total_price_label()
        else:
            messagebox.showinfo("경고", "잔액이 부족합니다.")

    def clear_cart(self):
        for item in self.cart:
            self.menu[item]['quantity'] += self.cart[item]
        self.cart.clear()
        self.update_cart_label()
        self.update_menu_labels()
        self.update_total_price_label()

    def update_cart_label(self):
        self.cart_listbox.delete(0, tk.END)
        for item, quantity in self.cart.items():
            self.cart_listbox.insert(tk.END, f"{item} - {quantity}개")

    def update_menu_labels(self):
        for item in self.menu.keys():
            info_label = tk.Label(self.menu_frame, text=f"{self.menu[item]['price']}원 - {self.menu[item]['quantity']}개 남음")
            info_label.grid(row=list(self.menu.keys()).index(item), column=1, padx=20)

    def update_total_price_label(self):
        total_price = sum(self.menu[item]['price'] * self.cart[item] for item in self.cart)
        self.total_price_label.config(text=f"총 가격: {total_price} 원")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChineseRestaurantVendingMachine(root)
    root.mainloop()

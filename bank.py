# NBP BANK - PYTHON TKINTER GUI - ENGLISH VERSION
# Run: python bank.py
# No pip install needed!

import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime

GREEN = "#006341"
LIGHT = "#eef2f7"

acc = {}

root = tk.Tk()
root.title("NBP - National Bank of Pakistan | Hafizabad")
root.geometry("520x700")
root.configure(bg=LIGHT)
root.resizable(False, False)

def clear():
    for w in root.winfo_children():
        w.destroy()

def header(text):
    top = tk.Frame(root, bg=GREEN, height=70)
    top.pack(fill="x")
    tk.Label(top, text="NATIONAL BANK OF PAKISTAN", bg=GREEN, fg="white", font=("Arial", 14, "bold")).pack(pady=(8,0))
    tk.Label(top, text="Hafizabad Branch | Code 1234", bg=GREEN, fg="white", font=("Arial", 10)).pack()
    tk.Label(root, text=text, bg=LIGHT, fg="#1a237e", font=("Arial", 18, "bold"), pady=12).pack()

def entry(parent, label, show=None):
    tk.Label(parent, text=label, bg="white", font=("Arial", 10, "bold"), anchor="w").pack(fill="x", padx=20, pady=(8,0))
    e = tk.Entry(parent, font=("Arial", 12), show=show, relief="solid", bd=1)
    e.pack(fill="x", padx=20, pady=4, ipady=6)
    return e

def btn(parent, text, cmd, bg=GREEN):
    b = tk.Button(parent, text=text, command=cmd, bg=bg, fg="white" if bg==GREEN else "black", font=("Arial", 12, "bold"), relief="flat", cursor="hand2")
    b.pack(fill="x", padx=20, pady=8, ipady=8)
    return b

# ========== HOME ==========
def home():
    clear()
    header("Welcome to NBP Banking")
    f = tk.Frame(root, bg="white", bd=1, relief="solid")
    f.pack(padx=20, pady=5, fill="both", expand=True)
    tk.Label(f, text="Open Your Account From Home\nJust Like Real Bank - Authentic Way", bg="white", font=("Arial", 12), pady=20, justify="center").pack()
    btn(f, "Create New Account", create_screen)
    btn(f, "Login", login_screen, bg="#ff9800")
    tk.Label(f, text="Secure | Encrypted | NBP Hafizabad\n© 2025 National Bank of Pakistan", bg="white", fg="gray", font=("Arial", 9), pady=15).pack()

# ========== CREATE ACCOUNT ==========
def create_screen():
    clear()
    header("Account Opening Form")
    f = tk.Frame(root, bg="white")
    f.pack(padx=15, pady=5, fill="both", expand=True)
    tk.Label(f, text="Hafizabad Branch | Please Fill The Form Completely", bg="white", fg="gray", font=("Arial", 10)).pack()

    e_name = entry(f, "Full Name (As per CNIC)")
    e_father = entry(f, "Father Name")
    e_cnic = entry(f, "CNIC (13 digits)")
    e_phone = entry(f, "Mobile Number")
    e_addr = entry(f, "Address")
    e_dep = entry(f, "Initial Deposit (Min Rs. 500)")
    e_pass = entry(f, "Create Login Password", show="•")
    e_pin = entry(f, "Create 4 Digit ATM PIN", show="•")

    tk.Label(f, text="Account Type", bg="white", font=("Arial", 10, "bold")).pack(fill="x", padx=20)
    var_type = tk.StringVar(value="Saving Account")
    tk.OptionMenu(f, var_type, "Saving Account", "Current Account", "Asaan Account").pack(fill="x", padx=20, pady=4)

    def do_create():
        name = e_name.get().strip().title()
        father = e_father.get().strip().title()
        cnic = e_cnic.get().strip()
        phone = e_phone.get().strip()
        addr = e_addr.get().strip()
        pwd = e_pass.get().strip()
        pin = e_pin.get().strip()
        try:
            dep = float(e_dep.get())
        except:
            messagebox.showerror("Error", "Please enter only numbers in Deposit!")
            return
        if not name or not father or not cnic or not phone or not pwd or not pin:
            messagebox.showerror("Error", "Please fill all fields!")
            return
        if len(cnic) != 13 or not cnic.isdigit():
            messagebox.showerror("Error", "CNIC must be 13 digits!")
            return
        if dep < 500:
            messagebox.showerror("Error", "Minimum Deposit is Rs. 500!")
            return
        if len(pin) != 4 or not pin.isdigit():
            messagebox.showerror("Error", "PIN must be 4 digits!")
            return

        acc_no = "1234" + str(random.randint(1000000000, 9999999999))
        iban = "PK45NBPA" + acc_no
        atm = "5200 " + " ".join([str(random.randint(1000,9999)) for _ in range(3)])
        acc.clear()
        acc.update({"name":name,"father":father,"cnic":cnic,"phone":phone,"address":addr,"type":var_type.get(),"password":pwd,"pin":pin,"balance":dep,"acc_no":acc_no,"iban":iban,"atm":atm,"txns":[(datetime.now().strftime("%d-%m-%Y %I:%M %p"), "Account Opening", dep, dep)]})
        show_slip()

    btn(f, "Create Account", do_create)
    btn(f, "Back to Home", home, bg="#eeeeee")

def show_slip():
    clear()
    header("Account Successfully Created!")
    f = tk.Frame(root, bg="white", bd=1, relief="solid")
    f.pack(padx=20, pady=10, fill="both", expand=True)
    txt = f"""Bank: NATIONAL BANK OF PAKISTAN
Branch: NBP Hafizabad - Code 1234

Account Holder: {acc['name']}
Father Name: {acc['father']}
CNIC: {acc['cnic']}
Phone: {acc['phone']}
Address: {acc['address']}
Account Type: {acc['type']}

Account No: {acc['acc_no']}
IBAN: {acc['iban']}
ATM Card: {acc['atm']}
Balance: Rs. {acc['balance']:,.0f}"""
    tk.Label(f, text=txt, bg="white", font=("Arial", 11), justify="left", pady=15, padx=10).pack()
    tk.Label(f, text=f"Please Remember Your Account No: {acc['acc_no']}", bg="#e8f5e9", fg="green", font=("Arial", 11, "bold"), pady=8).pack(fill="x", padx=10)
    btn(f, "Login Now", login_screen)

# ========== LOGIN ==========
def login_screen():
    clear()
    header("Login")
    f = tk.Frame(root, bg="white")
    f.pack(padx=20, pady=10, fill="both", expand=True)
    e_acc = entry(f, "Account Number")
    e_name = entry(f, "Your Full Name")
    e_pass = entry(f, "Password", show="•")
    def do_login():
        if not acc:
            messagebox.showerror("Error", "Please create an account first!")
            return
        if e_acc.get().strip() != acc['acc_no'] or e_name.get().strip().title() != acc['name'] or e_pass.get() != acc['password']:
            messagebox.showerror("Error", "Wrong Account No / Name / Password!")
            return
        dashboard()
    btn(f, "Login", do_login)
    btn(f, "Back to Home", home, bg="#eeeeee")

# ========== DASHBOARD ==========
def dashboard():
    clear()
    header(f"Welcome, {acc['name']}")
    f = tk.Frame(root, bg="white")
    f.pack(padx=20, pady=10, fill="both", expand=True)
    bal_frame = tk.Frame(f, bg=GREEN)
    bal_frame.pack(fill="x", padx=10, pady=10)
    tk.Label(bal_frame, text="Current Balance", bg=GREEN, fg="white", font=("Arial", 11)).pack(pady=(10,0))
    tk.Label(bal_frame, text=f"Rs. {acc['balance']:,.0f}", bg=GREEN, fg="white", font=("Arial", 22, "bold")).pack()
    tk.Label(bal_frame, text=f"{acc['type']} | {acc['acc_no']}", bg=GREEN, fg="white", font=("Arial", 10)).pack(pady=(0,10))

    btn(f, "Deposit", deposit_screen)
    btn(f, "Withdraw", withdraw_screen)
    btn(f, "Bank Statement", statement_screen)
    btn(f, "Credit Score & Loan", loan_screen)
    btn(f, "My Account Details", details_screen)
    btn(f, "Logout", home, bg="#eeeeee")

def deposit_screen():
    clear()
    header("Deposit")
    f = tk.Frame(root, bg="white")
    f.pack(padx=20, pady=10, fill="both", expand=True)
    tk.Label(f, text=f"Balance: Rs. {acc['balance']:,.0f}", bg="white", font=("Arial", 13, "bold")).pack(pady=10)
    e = entry(f, "How Much Amount To Deposit? Rs.")
    def do():
        try: amt = float(e.get())
        except: messagebox.showerror("Error", "Please enter only numbers!"); return
        if amt <= 0: messagebox.showerror("Error", "Amount must be greater than 0!"); return
        acc['balance'] += amt
        acc['txns'].append((datetime.now().strftime("%d-%m-%Y %I:%M %p"), "Deposit", amt, acc['balance']))
        messagebox.showinfo("Success", f"Rs. {amt:,.0f} Deposited Successfully!\nNew Balance: Rs. {acc['balance']:,.0f}")
        dashboard()
    btn(f, "Deposit Now", do)
    btn(f, "Back to Dashboard", dashboard, bg="#eeeeee")

def withdraw_screen():
    clear()
    header("Withdraw")
    f = tk.Frame(root, bg="white")
    f.pack(padx=20, pady=10, fill="both", expand=True)
    tk.Label(f, text=f"Balance: Rs. {acc['balance']:,.0f}", bg="white", font=("Arial", 13, "bold")).pack(pady=10)
    e_amt = entry(f, "How Much Amount To Withdraw? Rs.")
    e_pin = entry(f, "ATM PIN", show="•")
    def do():
        try: amt = float(e_amt.get())
        except: messagebox.showerror("Error", "Please enter only numbers!"); return
        if e_pin.get() != acc['pin']:
            messagebox.showerror("Error", "Wrong PIN!"); return
        if amt > acc['balance']:
            messagebox.showerror("Error", f"Insufficient Balance! You have only Rs. {acc['balance']:,.0f}"); return
        acc['balance'] -= amt
        acc['txns'].append((datetime.now().strftime("%d-%m-%Y %I:%M %p"), "Withdraw", -amt, acc['balance']))
        messagebox.showinfo("Success", f"Rs. {amt:,.0f} Withdrawn Successfully!\nRemaining: Rs. {acc['balance']:,.0f}")
        dashboard()
    btn(f, "Withdraw Now", do)
    btn(f, "Back to Dashboard", dashboard, bg="#eeeeee")

def statement_screen():
    clear()
    header("Bank Statement")
    f = tk.Frame(root, bg="white")
    f.pack(padx=15, pady=10, fill="both", expand=True)
    tk.Label(f, text=f"{acc['name']} | {acc['acc_no']} | CNIC: {acc['cnic']}", bg="white", font=("Arial", 10, "bold")).pack(pady=5)
    txt = tk.Text(f, height=18, font=("Arial", 10))
    txt.pack(fill="both", padx=10)
    for d, typ, amt, bal in acc['txns']:
        txt.insert("end", f"{d} | {typ} | Rs. {amt:,.0f} | Bal: Rs. {bal:,.0f}\n")
    txt.config(state="disabled")
    tk.Label(f, text=f"Final Balance: Rs. {acc['balance']:,.0f}", bg="white", font=("Arial", 12, "bold")).pack(pady=8)
    btn(f, "Back to Dashboard", dashboard, bg="#eeeeee")

def details_screen():
    clear()
    header("My Account Details")
    f = tk.Frame(root, bg="white")
    f.pack(padx=20, pady=10, fill="both", expand=True)
    txt = f"Name: {acc['name']}\nFather: {acc['father']}\nCNIC: {acc['cnic']}\nPhone: {acc['phone']}\nAddress: {acc['address']}\nType: {acc['type']}\nAcc No: {acc['acc_no']}\nIBAN: {acc['iban']}\nATM: {acc['atm']}\nBalance: Rs. {acc['balance']:,.0f}"
    tk.Label(f, text=txt, bg="white", font=("Arial", 11), justify="left", pady=15).pack()
    btn(f, "Back to Dashboard", dashboard, bg="#eeeeee")

def loan_screen():
    clear()
    header("Credit Score & Loan")
    f = tk.Frame(root, bg="white")
    f.pack(padx=20, pady=10, fill="both", expand=True)
    s = 600
    bal = acc['balance']
    if bal >= 100000: s += 120
    elif bal >= 50000: s += 80
    elif bal >= 10000: s += 40
    elif bal >= 1000: s += 20
    if len(acc['txns']) >= 5: s += 15
    s = min(850, s)
    tk.Label(f, text=f"Credit Score\n{s} / 850", bg=GREEN, fg="white", font=("Arial", 16, "bold"), pady=15).pack(fill="x", padx=10, pady=10)
    if s >= 750: loan = f"Rs. {bal*5+200000:,.0f} at 10%"
    elif s >= 650: loan = f"Rs. {bal*3+100000:,.0f} at 13%"
    elif s >= 550: loan = f"Rs. {bal*2+50000:,.0f} at 16%"
    else: loan = "Loan Not Available - Low Score"
    tk.Label(f, text=f"Loan Eligibility:\n{loan}\n\nBalance: Rs. {bal:,.0f}", bg="white", font=("Arial", 12)).pack(pady=15)
    btn(f, "Back to Dashboard", dashboard, bg="#eeeeee")

home()
root.mainloop()
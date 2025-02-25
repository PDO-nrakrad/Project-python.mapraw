import tkinter as tk
from tkinter import messagebox

def show_custom_message(title, message):
    custom_dialog = tk.Toplevel()
    custom_dialog.title(title)
    custom_dialog.configure(bg="#AED6F1")  # พื้นหลังโทนเย็น
    
    label = tk.Label(custom_dialog, text=message, font=("Arial", 14), bg="#AED6F1", fg="#154360", wraplength=400)
    label.pack(padx=20, pady=20)
    
    close_button = tk.Button(custom_dialog, text="ตกลง", font=("Arial", 12), bg="#5DADE2", fg="white", command=custom_dialog.destroy)
    close_button.pack(pady=10)

def calculate_fine(vehicle_type, distance, time, has_license):
    speed_limits = {
        "จักรยานยนต์": 80,
        "รถบรรทุก": 90,
        "รถยนต์ 4 ล้อ": 110
    }
    fines = {
        "จักรยานยนต์": 4000,
        "รถบรรทุก": 4000,
        "รถยนต์ 4 ล้อ": 4000
    }
    license_fine = 500
    
    if vehicle_type not in speed_limits:
        return "ประเภทพาหนะไม่ถูกต้อง", 0
    
    speed = distance / time
    speed_limit = speed_limits[vehicle_type]
    fine = fines[vehicle_type]
    total_fine = 0
    reason = ""
    
    if speed > speed_limit:
        total_fine = fine
        reason = f"🚗 ขับรถเร็วเกินกำหนด (เกิน {speed_limit} km/h)"
        if has_license:
            total_fine += license_fine
            reason += " และมีค่าปรับใบขับขี่เพิ่ม 🪪"
        return f"เหตุผลที่โดนปรับ: {reason}\nคุณขับเร็วเกินกำหนด ({speed_limit} km/h) ความเร็วของคุณคือ {speed:.2f} km/h ค่าปรับ {total_fine} บาท", total_fine
    else:
        return f"✅ คุณขับอยู่ในความเร็วที่กฎหมายกำหนด ({speed:.2f} km/h) ไม่มีค่าปรับ", total_fine

def calculate_and_display():
    vehicle_type = vehicle_var.get()
    try:
        distance = float(distance_entry.get())
        time = float(time_entry.get())
        has_license = license_var.get()
        
        result, total_fine = calculate_fine(vehicle_type, distance, time, has_license)
        show_custom_message("ผลการคำนวณ", f"{result}\n💰 สรุปยอดค่าปรับทั้งหมด: {total_fine} บาท")
    except ValueError:
        show_custom_message("ข้อผิดพลาด", "⚠️ กรุณากรอกตัวเลขที่ถูกต้องในช่องระยะทางและเวลา")

# สร้าง GUI
root = tk.Tk()
root.title("โปรแกรมคำนวณค่าปรับความเร็วเกินกฎหมาย")
root.configure(bg="#D6EAF8")  # พื้นหลังโทนเย็น (สีฟ้าอ่อน)

# ตัวเลือกประเภทพาหนะ
vehicle_var = tk.StringVar(value="จักรยานยนต์")
tk.Label(root, text="🚘 เลือกประเภทพาหนะ:", font=("Arial", 12), bg="#D6EAF8").pack()
tk.OptionMenu(root, vehicle_var, "จักรยานยนต์", "รถบรรทุก", "รถยนต์ 4 ล้อ").pack()

# ช่องกรอกระยะทาง
tk.Label(root, text="📏 ระยะทางที่ขับขี่ (กิโลเมตร):", font=("Arial", 12), bg="#D6EAF8").pack()
distance_entry = tk.Entry(root, font=("Arial", 12))
distance_entry.pack()

# ช่องกรอกเวลา
tk.Label(root, text="⏳ ระยะเวลาที่ใช้ (ชั่วโมง):", font=("Arial", 12), bg="#D6EAF8").pack()
time_entry = tk.Entry(root, font=("Arial", 12))
time_entry.pack()

# ตัวเลือกมีใบขับขี่หรือไม่
license_var = tk.BooleanVar()
tk.Checkbutton(root, text="🪪 มีใบขับขี่", variable=license_var, font=("Arial", 12), bg="#D6EAF8").pack()

# ปุ่มคำนวณ
calculate_button = tk.Button(root, text="🚦 คำนวณค่าปรับ", font=("Arial", 12), bg="#5DADE2", fg="white", command=calculate_and_display)
calculate_button.pack(pady=10)

# เริ่ม GUI
root.mainloop()

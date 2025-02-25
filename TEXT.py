def calculate_fine(vehicle_type, distance, time, has_license):
    # กำหนดความเร็วสูงสุดและค่าปรับตามประเภทของพาหนะ
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
    license_fine = 500  # ค่าปรับหากไม่มีใบขับขี่

    # ตรวจสอบว่าประเภทพาหนะถูกต้องหรือไม่
    if vehicle_type not in speed_limits:
        return "ประเภทพาหนะไม่ถูกต้อง", 0

    speed = distance / time  # คำนวณความเร็ว (km/h)
    speed_limit = speed_limits[vehicle_type]
    fine = fines[vehicle_type]
    total_fine = 0
    reason = ""

    if speed > speed_limit:
        total_fine = fine
        reason = f"ขับรถเร็วเกินกำหนด (เกิน {speed_limit} km/h)"
        
        if not has_license:  # ถ้าไม่มีใบขับขี่ ให้เพิ่มค่าปรับ
            total_fine += license_fine
            reason += " และไม่มีใบขับขี่"

        return (
            f"เหตุผลที่โดนปรับ: {reason}\n"
            f"คุณขับเร็วเกินกว่ากฎหมายกำหนด ({speed_limit} km/h) "
            f"ความเร็วของคุณคือ {speed:.2f} km/h ค่าปรับ {total_fine} บาท"
            + (f" (รวมค่าปรับไม่มีใบขับขี่ {license_fine} บาท)" if not has_license else ""),
            total_fine
        )
    else:
        return f"คุณขับอยู่ในความเร็วที่กฎหมายกำหนด ({speed:.2f} km/h) ไม่มีค่าปรับ", total_fine


# รับข้อมูลจากผู้ใช้
vehicle_type = input("กรุณาใส่ประเภทพาหนะ (จักรยานยนต์, รถบรรทุก, รถยนต์ 4 ล้อ): ")
distance = float(input("กรุณาใส่ระยะทางที่ขับขี่ (กิโลเมตร): "))
time = float(input("กรุณาใส่ระยะเวลาที่ใช้ (ชั่วโมง): "))
has_license = input("คุณมีใบขับขี่หรือไม่? (yes/no): ").strip().lower() == "yes"

# คำนวณค่าปรับ
result, total_fine = calculate_fine(vehicle_type, distance, time, has_license)
print(result)
print(f"สรุปยอดค่าปรับทั้งหมด: {total_fine} บาท")

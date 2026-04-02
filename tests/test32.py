import customtkinter as ctk

# 기본 설정
ctk.set_appearance_mode("dark")  # "light" 도 가능
ctk.set_default_color_theme("blue")

# 창 생성
app = ctk.CTk()
app.title("내 첫 GUI")
app.geometry("400x300")

# 라벨 (텍스트)
label = ctk.CTkLabel(app, text="안녕하세요!", font=("Arial", 20))
label.pack(pady=20)

# 버튼 클릭 함수
def button_click():
    label.configure(text="버튼이 눌렸어요!")

# 버튼
button = ctk.CTkButton(app, text="클릭", command=button_click)
button.pack(pady=10)

# 입력창
entry = ctk.CTkEntry(app, placeholder_text="이름 입력")
entry.pack(pady=10)

# 입력값 출력 함수
def show_name():
    name = entry.get()
    label.configure(text=f"안녕, {name}!")

# 입력 버튼
button2 = ctk.CTkButton(app, text="입력 확인", command=show_name)
button2.pack(pady=10)

# 실행
app.mainloop()
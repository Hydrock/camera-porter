import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Функция для копирования файлов с логами
def copy_files(source_path, destination_root, log_enabled):
    # Папки назначения
    jpeg_destination = os.path.join(destination_root, "JPEG")
    raw_destination = os.path.join(destination_root, "RAW")
    video_destination = os.path.join(destination_root, "Video")

    # Создаем папки назначения, если они еще не существуют
    os.makedirs(jpeg_destination, exist_ok=True)
    os.makedirs(raw_destination, exist_ok=True)
    os.makedirs(video_destination, exist_ok=True)

    # Проход по всем подкаталогам и файлам флешки
    for root, dirs, files in os.walk(source_path):
        for file in files:
            # Определяем тип файла по расширению и копируем в соответствующую папку
            file_path = os.path.join(root, file)
            if file.lower().endswith((".jpeg", ".jpg")):
                shutil.copy2(file_path, jpeg_destination)
                log_event(f"Скопирован JPEG файл: {file_path}", log_enabled)
            elif file.lower().endswith(".arw"):  # RAW файлы Sony
                shutil.copy2(file_path, raw_destination)
                log_event(f"Скопирован RAW файл: {file_path}", log_enabled)
            elif file.lower().endswith((".mp4", ".mov", ".xml")):  # Видео и XML
                shutil.copy2(file_path, video_destination)
                log_event(f"Скопировано видео или XML файл: {file_path}", log_enabled)
    
    messagebox.showinfo("Завершено", "Копирование завершено!")

# Функция для добавления логов в текстовое поле
def log_event(message, log_enabled):
    if log_enabled.get():
        log_text.insert(tk.END, message + "\n")
        log_text.see(tk.END)

# Функции для выбора директорий
def select_source_directory():
    path = filedialog.askdirectory(title="Выберите директорию на флешке")
    source_entry.delete(0, tk.END)
    source_entry.insert(0, path)

def select_destination_directory():
    path = filedialog.askdirectory(title="Выберите директорию на жестком диске")
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, path)

# Функция для запуска копирования с UI
def start_copy():
    source_path = source_entry.get()
    destination_root = destination_entry.get()

    if not os.path.isdir(source_path):
        messagebox.showerror("Ошибка", "Выберите корректную директорию на флешке!")
        return
    if not os.path.isdir(destination_root):
        messagebox.showerror("Ошибка", "Выберите корректную директорию на жестком диске!")
        return

    # Очищаем текстовое поле логов перед началом копирования
    log_text.delete(1.0, tk.END)
    copy_files(source_path, destination_root, log_enabled)

# Создание окна UI
root = tk.Tk()
root.title("Копирование файлов с флешки Sony")
root.geometry("600x600")

# Поля для ввода директорий
tk.Label(root, text="Директория на флешке:").pack(pady=5)
source_entry = tk.Entry(root, width=60)
source_entry.pack(pady=5)
tk.Button(root, text="Выбрать...", command=select_source_directory).pack(pady=5)

tk.Label(root, text="Директория на жестком диске:").pack(pady=5)
destination_entry = tk.Entry(root, width=60)
destination_entry.pack(pady=5)
tk.Button(root, text="Выбрать...", command=select_destination_directory).pack(pady=5)

# Чекбокс для управления логами
log_enabled = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Отображать логи копирования", variable=log_enabled).pack(pady=10)

# Поле для отображения логов
log_text = scrolledtext.ScrolledText(root, width=70, height=10, state="normal")
log_text.pack(pady=10)

# Кнопка запуска копирования
tk.Button(root, text="Начать копирование", command=start_copy).pack(pady=10)

# Запуск UI
root.mainloop()

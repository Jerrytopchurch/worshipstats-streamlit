
# gui_app.py
# 圖形化介面啟動程式（修正版）


from tkinter import messagebox
import pandas as pd
import os
import sys

# 加入 modules 模組路徑
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

from form_reader import read_forms_from_folder
from stat_calculator import calculate_statistics
from report_generator import export_reports

INPUT_FOLDER = "input_forms"
OUTPUT_FOLDER = "output_reports"

def run_statistics():
    try:
        df_all = read_forms_from_folder(INPUT_FOLDER)
        if df_all.empty:
            messagebox.showwarning("提醒", "input_forms 資料夾中找不到任何表單！")
            return

        stats_df, potential_df, heavy_df = calculate_statistics(df_all)
        export_reports(stats_df, potential_df, heavy_df, OUTPUT_FOLDER)

        messagebox.showinfo("完成！", f"報表已產出於 {OUTPUT_FOLDER} 資料夾！")
    except Exception as e:
        messagebox.showerror("錯誤", str(e))

def launch_gui():
    window = tk.Tk()
    window.title("敬拜服事報表工具")
    window.geometry("360x200")

    label = tk.Label(window, text="📥 點擊下方按鈕產出統計報表\n(請先將表單放進 input_forms 資料夾)", font=("Arial", 12))
    label.pack(pady=20)

    run_button = tk.Button(window, text="執行統計報表產生", font=("Arial", 14), bg="#4CAF50", fg="white", command=run_statistics)
    run_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    launch_gui()

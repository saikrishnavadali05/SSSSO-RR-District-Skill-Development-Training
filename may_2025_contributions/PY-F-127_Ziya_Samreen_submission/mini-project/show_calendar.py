import calendar
import datetime as dt
import sys

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN_BG = "\033[42m"
YELLOW_BG = "\033[43m"
RED = "\033[31m"
BLUE = "\033[34m"

# Holidays (year, month, day): "Holiday Name"
HOLIDAYS = {
    (2025, 1, 1): "New Year's Day",
    (2025, 7, 15): "My Birthday",
    (2025, 12, 25): "Christmas"
}

def highlight_today(cal_str, year, month):
    today = dt.date.today()
    if today.year != year or today.month != month:
        return cal_str

    lines = cal_str.splitlines()
    new_lines = []

    for line in lines:
        for day in range(1, 32):
            day_str = f"{day:2}"
            if today.day == day:
                colored = f"{GREEN_BG}{BOLD}{day_str}{RESET}"
                line = line.replace(day_str, colored, 1)
        new_lines.append(line)

    return "\n".join(new_lines)

def highlight_holidays(cal_str, year, month):
    lines = cal_str.splitlines()
    new_lines = []

    for line in lines:
        for day in range(1, 32):
            day_str = f"{day:2}"
            if (year, month, day) in HOLIDAYS:
                colored = f"{YELLOW_BG}{BOLD}{day_str}{RESET}"
                line = line.replace(day_str, colored, 1)
        new_lines.append(line)

    return "\n".join(new_lines)

def highlight_weekends(cal_str, year, month):
    lines = cal_str.splitlines()
    new_lines = []
    header_found = False

    for line in lines:
        if not header_found and any(day in line for day in ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']):
            header_found = True
            new_lines.append(line)
            continue

        if header_found:
            parts = line.split()
            new_line = ""
            for day_str in parts:
                try:
                    day = int(day_str)
                    day_of_week = calendar.weekday(year, month, day)
                    if day_of_week == 5:
                        day_str = f"{BLUE}{day_str:>2}{RESET}"
                    elif day_of_week == 6:
                        day_str = f"{RED}{day_str:>2}{RESET}"
                    else:
                        day_str = f"{day_str:>2}"
                except:
                    pass
                new_line += day_str + " "
            new_lines.append(new_line.rstrip())
        else:
            new_lines.append(line)

    return "\n".join(new_lines)

def show_month(year, month):
    cal_str = calendar.month(year, month)
    cal_str = highlight_today(cal_str, year, month)
    cal_str = highlight_weekends(cal_str, year, month)
    cal_str = highlight_holidays(cal_str, year, month)
    print(cal_str)

    with open(f"calendar_{year}_{month}.txt", "w") as f:
        f.write(calendar.month(year, month))
    print(f"\n📁 Calendar saved to calendar_{year}_{month}.txt")

def show_year(year):
    cal_str = calendar.calendar(year)
    print(cal_str)
    with open(f"calendar_{year}.txt", "w") as f:
        f.write(cal_str)
    print(f"\n📁 Full year calendar saved to calendar_{year}.txt")

def interactive_mode():
    print("No command-line arguments. Switching to interactive mode.")
    year = int(input("Enter year: "))
    month_input = input("Enter month (leave blank for full year): ")
    if month_input.strip():
        month = int(month_input)
        show_month(year, month)
    else:
        show_year(year)

# ─── GUI version with colours ────────────────────────────────────────────
def show_gui():
    import tkinter as tk
    from tkinter import ttk

    TODAY = dt.date.today()

    def render_calendar():
        try:
            y = int(year_var.get())
            m_raw = month_var.get().strip()

            # Clear previous content
            text_area.configure(state="normal")
            text_area.delete("1.0", tk.END)

            if m_raw == "" or m_raw.lower() == "all":
                # Whole year
                cal_str = calendar.TextCalendar().formatyear(y)
                text_area.insert(tk.END, cal_str)
                root.geometry("540x600")
                paint_year(y)
            else:
                m = int(m_raw)
                cal_str = calendar.month(y, m)
                text_area.insert(tk.END, cal_str)
                root.geometry("250x220")
                paint_month(y, m)

            text_area.configure(state="disabled")
        except Exception as e:
            text_area.insert(tk.END, f"Error: {e}")

    # ── tagging helpers ────────────────────────────────────────────────
    def paint_month(year, month):
        # loop through days 1‑31 and search for them in widget text
        for day in range(1, 32):
            tag = f"d{day}"
            idx = "1.0"
            while True:
                idx = text_area.search(f"{day:2}", idx, tk.END)
                if not idx:
                    break
                end = f"{idx}+2c"
                text_area.tag_add(tag, idx, end)
                idx = end
            # decide colour
            try:
                dt.date(year, month, day)
            except:
                continue              # invalid date
            dow = calendar.weekday(year, month, day)
            if (year, month, day) in HOLIDAYS:
                text_area.tag_config(tag, background="yellow", font=("Courier New", 10, "bold"))
            elif dt.date(year, month, day) == TODAY:
                text_area.tag_config(tag, background="lightgreen", font=("Courier New", 10, "bold"))
            elif dow == 5:            # Saturday
                text_area.tag_config(tag, foreground="blue")
            elif dow == 6:            # Sunday
                text_area.tag_config(tag, foreground="red")

    def paint_year(year):
        # walk every month
        for month in range(1, 13):
            paint_month(year, month)

    # ── UI layout ───────────────────────────────────────────────────────
    root = tk.Tk()
    root.title("Calendar")

    frm = ttk.Frame(root, padding=6)
    frm.pack(fill="x")

    ttk.Label(frm, text="Year").grid(row=0, column=0, sticky="e")
    year_var = tk.StringVar(value=str(TODAY.year))
    ttk.Entry(frm, textvariable=year_var, width=6).grid(row=0, column=1, sticky="w")

    ttk.Label(frm, text="Month").grid(row=1, column=0, sticky="e")
    month_var = tk.StringVar(value=str(TODAY.month))
    ttk.Entry(frm, textvariable=month_var, width=6).grid(row=1, column=1, sticky="w")
    ttk.Label(frm, text='(1‑12 or "all")').grid(row=1, column=2, sticky="w")

    ttk.Button(frm, text="Show Calendar", command=render_calendar).grid(
        row=2, column=0, columnspan=3, pady=4
    )

    text_area = tk.Text(root, width=48, height=20, font=("Courier New", 10))
    text_area.pack(expand=True, fill="both")

        # ── draw calendar the first time, then start Tk loop ──
    render_calendar()
    root.mainloop()


# =========================================================
#  MAIN DISPATCHER
# =========================================================
def main():
    # --gui  →  open the Tkinter window
    if "--gui" in sys.argv:
        show_gui()

    # two arguments (year month)  →  terminal month view
    elif len(sys.argv) == 3:
        year  = int(sys.argv[1])
        month = int(sys.argv[2])
        show_month(year, month)

    # one argument (year)  →  terminal year view
    elif len(sys.argv) == 2:
        year = int(sys.argv[1])
        show_year(year)

    # no arguments  →  interactive prompt
    else:
        interactive_mode()


# =========================================================
#  START THE PROGRAM
# =========================================================
if __name__ == "__main__":
    main()


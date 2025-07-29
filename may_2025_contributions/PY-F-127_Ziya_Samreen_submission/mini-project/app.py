from flask import Flask, render_template, request
import datetime as dt
import calendar

app = Flask(__name__)

# ── Holiday list (add your own) ───────────────────────────────────────
HOLIDAYS = {
    (2025, 1, 1):  "New Year",
    (2025, 8, 1):  "My Birthday",
    (2025, 12, 25): "Christmas",
}

# ── Helper: build one month as coloured HTML ──────────────────────────
def month_to_html(year: int, month: int) -> str:
    cal = calendar.monthcalendar(year, month)
    today = dt.date.today()

    parts = [
        f"<strong>{calendar.month_name[month]} {year}</strong><br>",
        "Mo Tu We Th Fr Sa Su<br>",
    ]

    for week in cal:
        line_cells = []
        for day in week:
            if day == 0:                               # blank cell
                line_cells.append("&nbsp;&nbsp;")
                continue

            classes = []
            if dt.date(year, month, day) == today:
                classes.append("today")
            if (year, month, day) in HOLIDAYS:
                classes.append("holiday")
            dow = calendar.weekday(year, month, day)
            if dow == 5:
                classes.append("saturday")
            elif dow == 6:
                classes.append("sunday")

            cls = " ".join(classes)
            line_cells.append(f"<span class='{cls}'>{day:2}</span>")
        parts.append(" ".join(line_cells) + "<br>")

    # wrap the whole month block
    return "<div class='month'>" + "".join(parts) + "</div>"

# ── Main route ────────────────────────────────────────────────────────
@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        year_txt  = request.form.get("year", "").strip()
        month_txt = request.form.get("month", "").strip().lower()

        try:
            year = int(year_txt)
        except ValueError:
            output = "<b style='color:red;'>Please enter a valid year.</b>"
            return render_template("index.html", output=output)

        # build calendar
        if month_txt in ("", "all"):
            for m in range(1, 13):
                output += month_to_html(year, m)
        else:
            try:
                month = int(month_txt)
                output = month_to_html(year, month)
            except ValueError:
                output = "<b style='color:red;'>Invalid month.</b>"

    return render_template("index.html", output=output)

# ── Run server ────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)

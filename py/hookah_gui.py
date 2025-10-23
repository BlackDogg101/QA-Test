import tkinter as tk

def hookah_counter(hookah_list):
    try:
        hookahs = list(map(int, hookah_list.strip().split()))
        summ = 0
        steps = []
        for h in hookahs:
            if h < 4999:
                deduction = 1000
            else:
                deduction = 1500
            result = h - deduction
            summ += result
            steps.append(f"{h} - {deduction} = {result}")
        steps.append(f"\nИтого: {summ}")
        return "\n".join(steps)
    except:
        return "Ошибка: введите только числа через пробел"

def solve():
    input_data = entry.get()
    result = hookah_counter(input_data)
    output.config(text=result)

# GUI
root = tk.Tk()
root.title("Кальяносчитатель")
root.geometry("400x300")

entry = tk.Entry(root)
entry.pack(fill='x', expand=True, padx=10, pady=10)

def show_context_menu(event):
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label="Вставить", command=lambda: entry.event_generate('<<Paste>>'))
    menu.tk_popup(event.x_root, event.y_root)

entry.bind("<Button-3>", show_context_menu)

entry.pack(pady=10)

btn = tk.Button(root, text="Посчитать", command=solve)
btn.pack(pady=5)

output = tk.Label(root, text="", fg="blue", justify="left", anchor="w", wraplength=380)
output.pack(pady=10)

root.mainloop()

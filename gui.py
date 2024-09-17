import tkinter as tk
from tkinter import ttk
import gpt2

def on_submit():
    query = query_text.get("1.0", tk.END).strip()
    if query:
        main_text.insert(tk.END, f"You: {query}\n")
        main_text.insert(tk.END, "myGPT:" + gpt2.main(prompt=query, n_tokens_to_generate=8) + "\n")


# Creating window.
root = tk.Tk()
root.title("myGPT")

# Creating frame for the main text field.
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Creating textfield with the vertical scrollbar.
main_text = tk.Text(main_frame, wrap="word", height=20, width=60)
main_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_scroll = ttk.Scrollbar(main_frame, orient="vertical", command=main_text.yview)
main_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
main_text['yscrollcommand'] = main_scroll.set

# Creating frame for query field and button.
query_frame = ttk.Frame(root, padding="10")
query_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

# Creating query field.
query_text = tk.Text(query_frame, wrap="word", height=5, width=50)
query_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
query_scroll = ttk.Scrollbar(query_frame, orient="vertical", command=query_text.yview)
query_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
query_text['yscrollcommand'] = query_scroll.set

# Creating "Enter" button.
submit_button = ttk.Button(query_frame, text="Enter", command=on_submit)
submit_button.grid(row=0, column=2, padx=5)

root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, scrolledtext
import time
import webbrowser
import tiktoken

# Constants for CO2 calculation
CO2_PER_TOKEN = 0.000004  # grams per token
GRAMS_TO_NANOGRAMS = 1_000_000  # Convert grams to nanograms

# Create the main window
root = tk.Tk()
root.title("Eco Prompt - Prompt for Sustainable AI")
root.geometry("850x900")  # Increased size for better display
root.configure(bg="#f0f0f0")

# Apply a modern theme
style = ttk.Style()
style.theme_use("clam")

# Customize styles
style.configure("TLabel", font=("Arial", 12), background="#f0f0f0", foreground="#333333")
style.configure("TButton", font=("Arial", 12), background="#4CAF50", foreground="#ffffff")
style.configure("TEntry", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 12))
style.configure("TNotebook", background="#f0f0f0")
style.configure("TNotebook.Tab", font=("Arial", 11), padding=[10, 5])

# Responsive grid configuration
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(13, weight=1)

# Add title text
ttk.Label(root, text="Prompt framework to reduce Carbon footprint in GenAI", 
          font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=(20, 10), sticky="n")

# Predefined lists for dropdowns (same as before)
roles = ["Sustainability Consultant", "Expert Accountant", "Skilled Software Developer", "Seasoned Teacher", 
         "Experienced Architect", "Creative Graphic Designer", "SEO Professional Writer", 
         "Blockchain Developer", "User Experience (UX) Researcher", "Cybersecurity Analyst"]
tasks = ["Summarize existing data", "Recommend sustainable solutions", "Analyze environmental impact", 
         "Predict energy efficiency", "Identify key trends", "Generate actionable strategies", 
         "Validate pre-trained models", "Streamline processes", "Plan localized solutions"]
formats = ["Markdown", "Plain text", "PDF", "JSON", "HTML", "CSV", "Excel", "PowerPoint", "XML"]
donots = ["Avoid generating new data if existing data suffices", "Do not include non-essential computations", 
          "Avoid using unnecessary resources", "Limit the scope to reduce computational overhead"]

# Function to add custom entry to a dropdown
def add_custom_entry(entry_list, dropdown, entry_type):
    new_entry = simpledialog.askstring(f"Add Custom {entry_type}", f"Enter a new {entry_type}:")
    if new_entry and new_entry not in entry_list:
        entry_list.append(new_entry)
        dropdown['values'] = entry_list
        dropdown.set(new_entry)

# Function to count tokens using tiktoken
def count_tokens(text):
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

# Function to calculate CO2 reduction
def calculate_co2_reduction(token_reduction):
    co2_grams = token_reduction * CO2_PER_TOKEN
    return int(co2_grams * GRAMS_TO_NANOGRAMS)

# Animation functions
def show_co2_reduction_effect(co2_reduction):
    for i in range(0, co2_reduction + 1, max(1, int(co2_reduction / 50))):
        co2_label.config(text=f"CO2 Reduction: {i:,} ng")
        root.update_idletasks()
        time.sleep(0.02)

def show_token_reduction_effect(original_tokens, optimized_tokens):
    reduction = original_tokens - optimized_tokens
    for i in range(0, reduction + 1, max(1, int(reduction / 50))):
        token_label.config(text=f"Token Reduction: {i:,} tokens (Original: {original_tokens:,} → Optimized: {optimized_tokens:,})")
        root.update_idletasks()
        time.sleep(0.02)

# Function to generate and display both prompts
def generate_prompt():
    role = role_var.get()
    needs = needs_entry.get()
    task = task_var.get()
    details = details_entry.get()
    format_ = format_var.get()
    donot = donot_var.get()

    # Generate both versions
    original_prompt = (
        f"Act like a {role}, I need a {needs}, you will {task}, in the process, "
        f"you should {details}, please {donot}, input the final result in a {format_}."
    )
    
    optimized_prompt = (
        f"As {role}, provide {needs} by {task}. {details}. {donot}. Output: {format_}."
    )

    # Count tokens
    original_tokens = count_tokens(original_prompt)
    optimized_tokens = count_tokens(optimized_prompt)
    token_reduction = original_tokens - optimized_tokens
    
    # Calculate CO2 reduction
    co2_reduction = calculate_co2_reduction(token_reduction)
    
    # Display both prompts in tabs
    original_text.delete(1.0, tk.END)
    original_text.insert(tk.END, original_prompt)
    optimized_text.delete(1.0, tk.END)
    optimized_text.insert(tk.END, optimized_prompt)
    
    # Show effects
    show_token_reduction_effect(original_tokens, optimized_tokens)
    show_co2_reduction_effect(co2_reduction)

# Function to open AI services
def open_url(url):
    webbrowser.open(url, new=1)

def show_service_popup():
    popup = tk.Toplevel(root)
    popup.title("Choose a Service")
    popup.geometry("350x200")
    popup.configure(bg="#f0f0f0")
    
    ttk.Label(popup, text="Where would you like to use the prompt?", 
              font=("Arial", 12, "bold")).pack(pady=10)

    services = [
        ("ChatGPT", "https://chat.openai.com"),
        ("Gemini", "https://gemini.google.com"),
        ("Perplexity", "https://www.perplexity.ai"),
        ("Mistral AI", "https://chat.mistral.ai/chat"),
        ("DeepSeek", "https://chat.deepseek.com/")
    ]
    
    for name, url in services:
        ttk.Button(popup, text=name, command=lambda u=url: open_url(u)).pack(pady=3, fill='x', padx=20)

def copy_to_clipboard():
    notebook.select(1)  # Select optimized prompt tab
    root.clipboard_clear()
    root.clipboard_append(optimized_text.get(1.0, tk.END).strip())
    show_service_popup()

# UI Elements
# Input fields (same as before)
ttk.Label(root, text="Role:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
role_var = tk.StringVar()
role_dropdown = ttk.Combobox(root, textvariable=role_var, values=roles, width=40)
role_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
ttk.Button(root, text="Add Custom", command=lambda: add_custom_entry(roles, role_dropdown, "Role")).grid(row=1, column=2, padx=5, pady=10)

ttk.Label(root, text="Needs:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
needs_entry = ttk.Entry(root, width=43)
needs_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

ttk.Label(root, text="Task:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
task_var = tk.StringVar()
task_dropdown = ttk.Combobox(root, textvariable=task_var, values=tasks, width=40)
task_dropdown.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
ttk.Button(root, text="Add Custom", command=lambda: add_custom_entry(tasks, task_dropdown, "Task")).grid(row=3, column=2, padx=5, pady=10)

ttk.Label(root, text="Details:").grid(row=4, column=0, padx=10, pady=10, sticky="e")
details_entry = ttk.Entry(root, width=43)
details_entry.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

ttk.Label(root, text="Format:").grid(row=5, column=0, padx=10, pady=10, sticky="e")
format_var = tk.StringVar()
format_dropdown = ttk.Combobox(root, textvariable=format_var, values=formats, width=40)
format_dropdown.grid(row=5, column=1, padx=10, pady=10, sticky="ew")
ttk.Button(root, text="Add Custom", command=lambda: add_custom_entry(formats, format_dropdown, "Format")).grid(row=5, column=2, padx=5, pady=10)

ttk.Label(root, text="Do Not:").grid(row=6, column=0, padx=10, pady=10, sticky="e")
donot_var = tk.StringVar()
donot_dropdown = ttk.Combobox(root, textvariable=donot_var, values=donots, width=40)
donot_dropdown.grid(row=6, column=1, padx=10, pady=10, sticky="ew")
ttk.Button(root, text="Add Custom", command=lambda: add_custom_entry(donots, donot_dropdown, "Do Not")).grid(row=6, column=2, padx=5, pady=10)

# Buttons
generate_button = ttk.Button(root, text="Generate Prompt", command=generate_prompt)
generate_button.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

copy_button = ttk.Button(root, text="Copy Optimized Prompt", command=copy_to_clipboard)
copy_button.grid(row=8, column=1, padx=10, pady=10, sticky="ew")

# Metrics display
co2_label = tk.Label(root, text="CO2 Reduction: 0 ng", font=("Arial", 14), bg="#d4edda", fg="#155724")
co2_label.grid(row=9, column=0, columnspan=3, padx=10, pady=10, sticky="n")

token_label = tk.Label(root, text="Token Reduction: 0 tokens", font=("Arial", 14), bg="#d1ecf1", fg="#0c5460")
token_label.grid(row=10, column=0, columnspan=3, padx=10, pady=10, sticky="n")

# Notebook for prompt display
notebook = ttk.Notebook(root)
notebook.grid(row=11, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Original prompt tab
original_frame = ttk.Frame(notebook)
notebook.add(original_frame, text="Original Prompt")
original_text = scrolledtext.ScrolledText(original_frame, height=10, width=80, font=("Arial", 12), wrap="word")
original_text.pack(fill="both", expand=True, padx=5, pady=5)

# Optimized prompt tab
optimized_frame = ttk.Frame(notebook)
notebook.add(optimized_frame, text="Optimized Prompt")
optimized_text = scrolledtext.ScrolledText(optimized_frame, height=10, width=80, font=("Arial", 12), wrap="word")
optimized_text.pack(fill="both", expand=True, padx=5, pady=5)

# Configure grid weights
root.grid_rowconfigure(11, weight=1)
root.grid_columnconfigure(1, weight=1)

# Run the application
root.mainloop()
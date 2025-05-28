# EcoPrompt: Sustainable Prompt Optimization Tool  
**Empowering Greener AI Interactions**

----------------------------------------------------------

## Overview

**EcoPrompt** is a Python-based desktop application developed to support sustainable AI usage by minimizing the carbon footprint of prompt generation. It streamlines verbose prompts into optimized versions, reducing token count and estimating the resulting CO₂ savings. Featuring an intuitive interface and built-in carbon analytics, EcoPrompt promotes environmentally conscious interactions with generative AI. This software was developed as part of my Master’s program at the University of Kelaniya.

Developed by **Kathiramalairajah Kapilaraj**, Sri Lanka.

---

## Key Features

- **Prompt Optimization:** Converts verbose prompts into compact, efficient versions.
- **Token & CO₂ Estimation:** Calculates token reduction and estimates carbon savings in nanograms.
- **Custom Input Fields:** Add roles, tasks, formats, and exclusions to personalize prompts.
- **Clipboard Integration:** Copy optimized prompts for immediate use.
- **Service Integration:** One-click access to ChatGPT, Gemini, Perplexity, Mistral, and DeepSeek.
- **Interactive GUI:** Smooth animations and modern UI using `tkinter`.

---

## Technology Stack

- **Language:** Python 3.x
- **Libraries:** `tkinter`, `ttk`, `tiktoken`, `webbrowser`, `time`
- **Token Estimation:** Uses OpenAI’s `tiktoken` encoder (cl100k_base)
- **Carbon Model:** 0.000004 grams of CO₂ per token → converted to nanograms

---

## Installation

1. **Install Python 3.x**  
2. *(Optional)* Clone repo:  
   ```bash
   git clone [https://github.com/yourusername/EcoPrompt.git](https://github.com/naankapil/EcoPromt_a_Sustainable_Prompt_-Optimization_Tool)
   cd EcoPrompt
   ```
3. **Run Application**  
   ```bash
   python Eco_Prompt_V3.py
   ```

---

## Project Structure (Highlights)

- `Eco_Prompt_V3.py` – Main GUI application and CO₂-aware prompt logic

---

## License

This project is under the [MIT License](LICENSE.md).


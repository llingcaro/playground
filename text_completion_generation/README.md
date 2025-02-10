# Email Autocompletion using GPT-Neo

## Overview
This project is a simple **email autocompletion tool** built using **Flask** (Python) as the backend and a basic **HTML + JavaScript frontend**. It uses the **GPT-Neo 1.3B model** from Hugging Face to generate intelligent email completions based on user input.

## Features
- 📝 **Smart text completion**: Automatically completes email drafts based on the input.
- 🔄 **Multiple suggestions**: Generates **three different suggestions** for each input.
- ✂ **Sentence-bound completion**: Ensures the generated text **stops at a natural sentence boundary**.
- 🚀 **Fast and simple setup**: Runs locally with Flask and a lightweight frontend.

## Technologies Used
- **Backend**: Flask, Hugging Face `transformers`
- **Frontend**: HTML, JavaScript, Fetch API
- **Model**: `EleutherAI/gpt-neo-1.3B`

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/email-autocomplete.git
cd email-autocomplete
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r playground/requirements.txt
```

### 4️⃣ Run the Flask Server
```bash
cd playground/text_completion_generation
python app.py
```
The server will start at **http://127.0.0.1:5000/**.

### 5️⃣ Open the Web App
- Open `index.html` in your browser.
- Start typing in the text box and click **"Complete"** to get suggestions.

## Project Structure
```
playground/
│-- requirements.txt       # Python dependencies
│-- text_completion_generation/
    │-- app.py            # Flask backend
    │-- index.html        # Frontend UI
    │-- README.md         # Project documentation
```

## API Endpoint
### `/complete` (POST)
**Description**: Takes user input and returns three different text completions.

**Request:**
```json
{
  "text": "Hi John, I wanted to follow up on our meeting regarding"
}
```

**Response:**
```json
{
  "suggestions": [
    "the project timeline. Let me know your thoughts!",
    "the updates we discussed. Looking forward to your feedback.",
    "the next steps we need to take. Let me know what works for you."
  ]
}
```

## Future Improvements
- 🔹 Deploy the project on **Flask + Gunicorn** for production use.
- 🔹 Allow **customization of tone** (formal/informal).
- 🔹 Add **more models** (GPT-3.5, LLaMA) for comparison.

## License
This project is licensed under the **MIT License**.

---
🔥 **Enjoy building with AI!** 🚀


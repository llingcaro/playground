from flask import Flask, request, jsonify
from flask_cors import CORS
from sympy.physics.units import temperature
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Load the Hugging Face text generation model
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/complete", methods=["POST"])
def complete_text():
    data = request.json
    user_input = data.get("text", "")

    # Generate text completion
    response = generator(user_input,
                         max_new_tokens=20,
                         do_sample=True,
                         temperature=0.7,
                         eos_token_id=13)

    full_text = response[0]["generated_text"]

    # Remove the prompt
    completion = full_text[len(user_input):].strip()

    # Stop at the first period/exclamation/question mark
    for char in [".","!","?"]:
        if char in full_text:
            completion = completion.split(char)[0] + char
            break # Stop after finding the first full sentence

    return jsonify({"completion":completion})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
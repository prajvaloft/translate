from flask import Flask, request, render_template_string

app = Flask(__name__)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

HTML = """
<h2>Caesar Cipher</h2>
<form method="post">
    <textarea name="message" rows="4" cols="50"></textarea><br><br>
    <input type="number" name="key" value="3"><br><br>

    <select name="mode">
        <option value="encrypt">Encrypt</option>
        <option value="decrypt">Decrypt</option>
    </select><br><br>

    <button type="submit">Submit</button>
</form>

{% if result %}
<h3>Result:</h3>
<p>{{ result }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        message = request.form["message"]
        key = int(request.form["key"])
        mode = request.form["mode"]

        for symbol in message:
            if symbol in SYMBOLS:
                idx = SYMBOLS.find(symbol)
                if mode == "encrypt":
                    idx += key
                else:
                    idx -= key
                result += SYMBOLS[idx % len(SYMBOLS)]
            else:
                result += symbol

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run()

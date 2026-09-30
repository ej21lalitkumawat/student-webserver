from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        name = request.form["name"]
        roll = request.form["roll"]

        maths = int(request.form["maths"])
        science = int(request.form["science"])
        english = int(request.form["english"])

        total = maths + science + english
        percentage = total / 3

        if percentage >= 40:
            status = "PASS"
        else:
            status = "FAIL"

        result = f"""
        <h2>Student Result</h2>
        <p>Name: {name}</p>
        <p>Roll No: {roll}</p>
        <p>Total: {total}</p>
        <p>Percentage: {percentage:.2f}%</p>
        <p>Result: {status}</p>
        """

    return f"""
    <html>
    <head>
        <title>Student Result System</title>
    </head>

    <body>
        <h1>Student Result System</h1>

        <form method="POST">

            Name:
            <input type="text" name="name" required>
            <br><br>

            Roll No:
            <input type="text" name="roll" required>
            <br><br>

            Maths:
            <input type="number" name="maths" required>
            <br><br>

            Science:
            <input type="number" name="science" required>
            <br><br>

            English:
            <input type="number" name="english" required>
            <br><br>

            <button type="submit">Calculate Result</button>

        </form>

        <hr>

        {result}

    </body>
    </html>
    """

app.run(debug=True)

from flask import Flask, render_template, request
from calculator import calculate_carbon
from recommendations import get_recommendations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    recommendations = []

    if request.method == "POST":

        car_km = float(request.form["car_km"])
        electricity = float(request.form["electricity"])
        flights = int(request.form["flights"])
        diet = request.form["diet"]

        result = calculate_carbon(
            car_km,
            electricity,
            flights,
            diet
        )

        recommendations = get_recommendations(result)

    return render_template(
        "index.html",
        result=result,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)
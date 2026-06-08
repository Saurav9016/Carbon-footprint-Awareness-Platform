def get_recommendations(score):

    recommendations = []

    if score > 300:
        recommendations.append(
            "Reduce private vehicle usage and use public transport."
        )

    if score > 200:
        recommendations.append(
            "Switch to energy-efficient appliances."
        )

    if score > 150:
        recommendations.append(
            "Reduce short-haul flights where possible."
        )

    if not recommendations:
        recommendations.append(
            "Great job! Keep maintaining sustainable habits."
        )

    return recommendations
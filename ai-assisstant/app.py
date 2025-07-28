from flask import Flask, render_template, request
from ai_helper import answer_question, summarize_text, generate_creative_content, save_feedback

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    responses = []
    user_input = ""
    function_choice = ""
    feedback_message = ""

    if request.method == "POST":
        if "feedback" in request.form:  # Feedback form
            response_text = request.form.get("response_text")
            feedback_value = request.form.get("feedback")
            save_feedback(response_text, feedback_value)
            feedback_message = "Thank you for your feedback!"
        else:
            user_input = request.form["user_input"]
            function_choice = request.form["function"]

            if function_choice == "question":
                responses = answer_question(user_input)
            elif function_choice == "summary":
                responses = summarize_text(user_input)
            elif function_choice == "creative":
                responses = generate_creative_content(user_input)

    return render_template("index.html", responses=responses, user_input=user_input, feedback_message=feedback_message)

if __name__ == "__main__":
    app.run(debug=True)

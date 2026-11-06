from flask import Flask,render_template,request
from google import genai
import os
from dotenv import load_dotenv,find_dotenv

app=Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/amitava")
def chatbot():
    question=request.args.get("question")
    load_dotenv(find_dotenv(),override=True)
    key=os.getenv("GOOGLE_API_KEY")
    client=genai.Client(api_key=key)
    response=client.models.generate_content(
        model='gemini-3.5-flash',
        contents=question
    )
    return f"AI: {response.text}"


if __name__=='__main__':
    app.run(debug=True)



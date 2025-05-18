import os
import json
import openai

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": "Method Not Allowed"
        }
    
    # Parse form data from the request.
    form = request.form
    project = form.get("project")
    if not project:
        return {
            "statusCode": 400,
            "body": "Please provide a valid project name."
        }
    
    # Build a prompt for security analysis.
    prompt = (
        f"Perform a thorough security analysis of the project named '{project}'. "
        "Identify any potential bugs, vulnerabilities, and security issues within the project. "
        "Provide recommendations for mitigating these issues and improving the design if necessary."
    )
    
    try:
        # Directly include the provided API key (not recommended for production)
        openai.api_key = "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"
        openai.api_base = "https://openrouter.ai/api"  # Adjust as needed

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or use another supported model
            messages=[
                {"role": "system", "content": "You are a skilled security analyst and code auditor."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response["choices"][0]["message"]["content"]
    except Exception as e:
        reply = f"An error occurred: {e}"
    
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"reply": reply})
    }

# LLM-GenAI-project
1️⃣ Bias Detection in AI Output

2️⃣ Code Explainer Bot (Error-Focused) 

🤖 Python Code Error Explanation Bot

Transform confusing error messages into learning opportunities! This bot helps Python learners understand their code errors without giving away complete solutions, fostering true comprehension.

🌟 Key Features

Error Analysis Engine: Breaks down Python errors into understandable explanations

Learning-Focused Guidance: Provides conceptual repair suggestions instead of complete solutions

Batch Processing: Analyze multiple error files at once

Professional Reports: Generates detailed Markdown reports with explanations

Sample Errors Included: Comes with common Python error examples for practice

🚀 Quick Start

Prerequisites
Python 3.7+

OpenAI API key (get one here)

Installation
bash

# Clone the repository
git clone https://github.com/yourusername/code-error-explainer.git

# Navigate to project directory
cd code-error-explainer

# Install dependencies
pip install -r requirements.txt
Configuration
Create a .env file in the project root:

env
OPENAI_API_KEY=your_api_key_here
Run the bot:

bash
python error_explainer.py
🧠 How It Works
Single Error Analysis Mode
Select mode 1 when prompted

Paste your problematic Python code

Type END when finished

Optionally provide the error message

Get instant explanation!

text
🤖 Code Error Explanation Bot
==================================================
✅ API key loaded from environment variables
Sample error code files created in data/error_codes/ directory

✅ Code Error Explanation Bot started!
==================================================
Select mode:
1. Single error analysis
2. Batch analysis of folder
Please enter 1 or 2: 1

Please enter the error code to analyze (enter 'END' to finish):
def calculate_area():
    area = length * width
    return area

result = calculate_area()
print(result)
END

Error message (optional, press Enter to skip): NameError: name 'length' is not defined

🔍 Analyzing...
Batch Analysis Mode
Select mode 2 when prompted

The bot will analyze all .py files in data/error_codes/

Get a comprehensive report in data/error_analysis_report.md

text
🤖 Code Error Explanation Bot
==================================================
Select mode:
1. Single error analysis
2. Batch analysis of folder
Please enter 1 or 2: 2

📁 Analyzing code in data/error_codes folder...
Analyzing syntax_error.py...
Analyzing variable_error.py...
Analyzing type_error.py...
Analyzing index_error.py...
Analyzing logic_error.py...
Analysis complete! Result saved to data/error_analysis_report.md
📝 Sample Report Output
markdown
# Python Code Error Explanation Report

---

## Case 1: variable_error.py

### Original Code
```python
# Variable error example
def calculate_area():
    # Using undefined variables
    area = length * width  # length and width are not defined
    return area

result = calculate_area()
print(result)            
AI Assistant Explanation
Error Analysis
The error is a NameError, indicating that Python encountered a variable name that hasn't been defined...

Cause
This error occurs because the variables 'length' and 'width' are used in the calculate_area() function...

Repair Suggestions
Define the variables 'length' and 'width' before using them...

Consider passing these values as parameters to the function...

Learning Points
Variable scope in Python functions

Parameter passing in functions

Importance of initializing variables before use

text

## 🔧 Customization Options

1. **Modify Prompt Style**: Edit the `system_prompt` in `CodeExplainerBot.__init__()`
```python
self.system_prompt = """You are a Python programming teaching assistant..."""
Change Model: Switch to a different OpenAI model

python
response = self.client.chat.completions.create(
    model="gpt-4-turbo",  # Changed model
    # ... other parameters
)
Add New Error Samples: Extend the create_sample_error_files() function

python
error_samples = {
    # ... existing samples
    "new_error.py": '''
# New error example
your problem code here
'''
}
⚠️ Important Notes
API Key Security: Never commit your .env file to version control

Educational Purpose: This bot is designed to promote learning - it won't give complete solutions

Cost Awareness: Each explanation uses OpenAI tokens - monitor your usage

Error Limitations: Works best with standard Python errors, may struggle with complex framework-specific errors

🤝 Contributing
Contributions are welcome! Here's how:

Fork the repository

Create a new branch (git checkout -b feature/improvement)

Commit your changes (git commit -am 'Add new feature')

Push to the branch (git push origin feature/improvement)

Create a new Pull Request

Turn frustration into learning! This bot helps you understand why your code fails, making you a better programmer with each error encountered. 🐍💡

3️⃣ Natural Language to SQL Queries 

4️⃣ Mini RAG (Retrieval-Augmented Generation) System

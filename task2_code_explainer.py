"""
Task 2: Code Error Explanation Bot
Objective: Build a bot that explains Python code errors without providing complete solutions
"""

import os
import openai
from typing import List, Dict
import json
from dotenv import load_dotenv

class CodeExplainerBot:
    def __init__(self, api_key: str):
        """
        Initialize the code explanation bot

        Parameters:
        api_key: OpenAI API key
        """
        self.client = openai.OpenAI(api_key=api_key)

        # Prompt template for teaching assistant
        self.system_prompt = """
You are a Python programming teaching assistant. When students encounter code errors, you need to:

1. Clearly explain the meaning of the error
2. Analyze why this error occurred
3. Provide conceptual repair suggestions (do not give complete runnable code)
4. Help students understand the underlying programming concepts

Important: Do not provide complete code solutions, but guide students to think and learn.
"""

    def explain_error(self, error_code: str, error_message: str = "") -> str:
        """
        Explain code errors
       
        Parameters:
        error_code: Code with errors
        error_message: Error message (optional)
       
        Returns:
        Explanation text
        """
        user_prompt = f"""
Please analyze the following Python code error:

Code:
```python
{error_code}
```

Error message (if any):
{error_message}

Please answer in the following format:

## Error Analysis
[Explain what the error is]

## Cause
[Explain why this error occurred]

## Repair Suggestions
[Provide conceptual repair methods, do not give complete code]

## Learning Points
[Relevant Python knowledge points]
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",  
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,  
                max_tokens=800
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"API call error: {str(e)}"
       
    def process_error_files(self, input_folder: str, output_file: str):
        """
        Batch process error code files
       
        Parameters:
        input_folder: Path to folder containing error code files
        output_file: Path to output markdown file
        """
        explanations = []

        # check if the input folder exists
        if not os.path.exists(input_folder):
            print(f"Error: Input folder '{input_folder}' does not exist")
            return

        # Traverse Python files in the folder
        for filename in os.listdir(input_folder):  
            if filename.endswith('.py'):
                file_path = os.path.join(input_folder, filename)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        code_content = f.read()

                    print(f"Analyzing {filename}...")
                    explanation = self.explain_error(code_content)  

                    explanations.append({
                        'filename': filename,
                        'code': code_content,
                        'explanation': explanation  
                    })
               
                except Exception as e:
                    print(f"Error processing file {filename}: {e}")

        if explanations:
            # Generate markdown report
            self._generate_markdown_report(explanations, output_file)
            print(f"Analysis complete! Result saved to {output_file}")
        else:
            print("No Python files found or processed successfully")

    def _generate_markdown_report(self, explanations: List[Dict], output_file: str):
        """
        Generate markdown format report
        """
        # make sure output file exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Python Code Error Explanation Report\n\n")  
            f.write("---\n\n")
            
            for i, item in enumerate(explanations, 1):  
                f.write(f"## Case {i}: {item['filename']}\n\n")
                f.write("### Original Code\n")
                f.write("```python\n")
                f.write(item['code'])
                f.write("\n```\n\n")
                f.write("### AI Assistant Explanation\n")
                f.write(item['explanation'])  
                f.write("\n\n---\n\n")

def create_sample_error_files():
    """
    Create sample error code files for testing
    """
    error_samples = {
        "syntax_error.py": '''
# Syntax error example
def greet(name):
    print("Hello, " + name)
    # Missing colon in if statement
    if name == "Alice"  # Missing colon here
        print("Special greeting!")
''',

        "variable_error.py": '''
# Variable error example
def calculate_area():
    # Using undefined variables
    area = length * width  # length and width are not defined
    return area

result = calculate_area()
print(result)            
''',

        "type_error.py": '''
# Type error example
def add_numbers(a, b):
    return a + b

# Trying to add string and number
result = add_numbers("5", 7)  
print(result)
''',

        "index_error.py": '''
# Index error example
numbers = [1, 2, 3, 4, 5]

# Trying to access non-existent index
for i in range(10):
    print(numbers[i])  
''',
               
        "logic_error.py": '''
# Logic error example
def find_maximum(numbers):
    max_num = 0  # Logic error: what if all numbers are negative?
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Testing with negative numbers list
negative_numbers = [-5, -2, -8, -1]
result = find_maximum(negative_numbers)
print(f"Maximum: {result}")  # Will incorrectly return 0
'''
    }

    # Create data directory and error_codes subdirectory
    os.makedirs("data/error_codes", exist_ok=True)
    
    for filename, content in error_samples.items():
        file_path = f"data/error_codes/{filename}"
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(content.strip())
    
    print("Sample error code files created in data/error_codes/ directory")

def load_api_key():
    """
    Load API key from environment variables
    Priority: .env file > System environment variables > User input

    Returns:
    str: API key
    """
    # Load .env file
    load_dotenv()

    # Try to get the API key from environment variables
    api_key = os.getenv('OPENAI_API_KEY')

    if api_key:
        print("✅ API key loaded from environment variables")
        return api_key

    # If not in environment variables, prompt user for input
    print("⚠️ No API key found in environment variables")
    print("Please set OPENAI_API_KEY in your .env file or environment variables")
    print("\nTo create a .env file:")
    print("1. Create a file named '.env' in your project root")
    print("2. Add this line: OPENAI_API_KEY=your_api_key_here")
    print("3. Save the file and restart the program")

    api_key = input("\nOr enter your OpenAI API key manually: ").strip()

    if not api_key:
        raise ValueError("API key is required to run this program")

    return api_key

def main():
    """
    Main function - demonstrate how to use the code explanation bot
    """
    print("🤖 Code Error Explanation Bot")
    print("=" * 50)

    try:
        # Automatically load API key
        api_key = load_api_key()

        # First create sample error files
        create_sample_error_files()

        # Create bot instance
        bot = CodeExplainerBot(api_key)

        print("\n✅ Code Error Explanation Bot started!")
        print("=" * 50)

        # Select mode
        mode = input("Select mode:\n1. Single error analysis\n2. Batch analysis of folder\nPlease enter 1 or 2: ").strip()

        if mode == "1":
            # Single error analysis mode
            print("\nPlease enter the error code to analyze (enter 'END' to finish):")
            code_lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                code_lines.append(line)

            error_code = "\n".join(code_lines)
            error_msg = input("\nError message (optional, press Enter to skip): ").strip()

            print("\n🔍 Analyzing...")
            explanation = bot.explain_error(error_code, error_msg)
            print("\n" + "=" * 50)
            print("🤖 AI Assistant Explanation:")
            print("=" * 50)
            print(explanation)

        elif mode == "2":
            # Batch analysis mode
            input_folder = "data/error_codes"
            output_file = "data/error_analysis_report.md"

            print(f"\n📁 Analyzing code in {input_folder} folder...")
            bot.process_error_files(input_folder, output_file)

        else:
            print("❌ Invalid selection")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please check your API key and try again")

if __name__ == "__main__":
    main()
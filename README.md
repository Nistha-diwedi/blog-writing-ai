# blog-writing-ai

**AI Blog Generator**

**Overview:**
_This AI-powered blog generator allows users to input a title, and the system automatically generates a well-structured blog article. It leverages the Gemini 2.0 Flash API to create high-quality content based on the given topic._

**Features:**
=> Automated Blog Writing: Generates a complete blog based on the provided title.
=> User-Friendly Interface: Simple command-line interaction.
=> Error Handling: Checks for empty inputs and handles API request failures gracefully.
=> Integration with Google Gemini API: Uses the gemini-2.0-flash:generateContent model to produce responses.

**Installation & Setup:**

=> The repository:
    https://github.com/Nistha-diwedi/blog-writing-ai

=> Install required dependencies:
    pip install requests

=> Set up your API key:
    Replace API_KEY in the script with your valid Google API key.

**Usage**

=> Run the script using: python app.py
=> Enter a blog title, and the system will generate a blog post.
=> Type exit to quit the application.

**File Structure**
├── ai_blog_generator.py  # Main script for generating blogs
├── README.md             # Documentation file
└── requirements.txt      # Required dependencies

**Error Handling**
=> Returns an error message if the input is empty.
=> Handles API request failures and exceptions.

**Future Enhancements**
=> Add support for multiple blog formats (listicles, guides, opinion pieces).
=> Implement a web-based UI for better usability.
=> Improve response handling for more structured outputs.


**Contributions**
=> Contributions are welcome! Feel free to fork this repository and submit a pull request with your improvements.


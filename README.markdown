# Studyfetch – Your AI Study Partner

Studyfetch is a personalized AI-powered study assistant built with Streamlit, AGNO Agents, OpenAI's GPT models, Exa search tools, and YouTube integration. It helps users learn faster by finding reliable resources, summarizing concepts, recommending videos, and generating custom study plans.

## Features

- **Ask Academic Questions**: Get clear, structured answers to your academic questions.
- **Trusted Search**: Search across trusted sources using the Exa API.
- **Video Recommendations**: Receive recommendations for educational YouTube videos.
- **Curated Resources**: Access a collection of tutorials, articles, and research papers.
- **Concept Simplification**: Break down complex topics into easy-to-understand explanations.
- **Personalized Plans**: Generate custom study plans and get project suggestions.
- **Learning Tips**: Discover tips for motivation, time management, and effective learning techniques.
- **Community Connection**: Find and connect with relevant communities and study groups.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/studyfetch-ai-agent.git
   cd studyfetch-ai-agent
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   # For macOS/Linux
   python -m venv venv
   source venv/bin/activate

   # For Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Setup: Environment Variables

Create a `.env` file in the root directory of the project and add your API keys as follows:

```plaintext
# .env
EXA_API_KEY=your_exa_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

**Important**: Ensure your OpenAI and Exa API keys are valid. You can obtain them from:
- [OpenAI API](https://platform.openai.com/)
- [Exa API](https://exa.ai/)

## Running the App

To run the Streamlit application locally, use the following command:
```bash
streamlit run app.py
```

Make sure to replace `app.py` with the actual name of your main application file if it's different.

## UI Preview

The user interface features a sleek, wide layout designed for a friendly and intuitive chatbot experience.

## Dependencies

All the necessary dependencies are listed in the `requirements.txt` file. The core dependencies include:
- streamlit
- python-dotenv
- agno
- openai
- exa-tools (via agno)
- youtube-tools (via agno)

## How it Works

The application utilizes a custom agent named **StudyScout**. This agent is powered by OpenAI's `gpt-4o-mini` model and is enhanced with the following tools:
- **ExaTools**: For performing real-time, reliable web searches.
- **YouTubeTools**: For fetching relevant educational video recommendations.

## Credits

This project was made possible by the following amazing technologies:
- [AGNO](https://agno.ai/)
- [Streamlit](https://streamlit.io/)
- [OpenAI](https://openai.com/)
- [Exa Search](https://exa.ai/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Future Ideas

- **Export Study Plans**: Add the ability to export generated study plans as a PDF.
- **User Authentication**: Implement user login and session persistence to save history and preferences.
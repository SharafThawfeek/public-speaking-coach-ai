import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = None
chain = None
parser = None


def load_saved_artifacts():
    """Initialize the LLM and structured parser chain."""
    global llm, chain, parser

    llm = ChatGroq(api_key=groq_api_key, model="Gemma2-9b-It") ## temperature = 0

    # Define required JSON fields (added grammar)
    schemas = [
        ResponseSchema(name="opening", description="Feedback on introduction and hook"),
        ResponseSchema(name="content", description="Feedback on main ideas, examples, structure"),
        ResponseSchema(name="delivery", description="Feedback on delivery, tone, fillers, body language"),
        ResponseSchema(name="grammar", description="Grammar and language corrections with examples"),
        ResponseSchema(name="overall", description="Overall impression of the speech"),
        ResponseSchema(name="suggestions", description="List of 3-5 concise improvement tips")
    ]

    parser = StructuredOutputParser.from_response_schemas(schemas)
    format_instructions = parser.get_format_instructions()

    # Prompt with JSON schema enforcement
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a professional public speaking coach. "
            "Analyze the given speech and provide constructive feedback. "
            "Also check for **grammar mistakes** (tense, plurals, articles, etc.) "
            "and suggest corrected forms. "
            "You must ONLY reply in JSON with this structure:\n\n"
            "{{\n"
            "  \"opening\": \"Feedback on introduction and hook\",\n"
            "  \"content\": \"Feedback on main ideas, examples, structure\",\n"
            "  \"delivery\": \"Feedback on delivery, tone, fillers, body language\",\n"
            "  \"grammar\": \"Grammar mistakes with corrections\",\n"
            "  \"overall\": \"Overall impression of the speech\",\n"
            "  \"suggestions\": [\"List of 3-5 concise improvement tips\"]\n"
            "}}\n\n"
            "Do not include any text outside the JSON object."
        ),
        ("human", "Speech:\n{input}")
    ])

    chain = prompt | llm


def analyze(speech: str):
    """
    Analyze a speech and return structured JSON feedback.
    
    The feedback includes:
    - Opening and hook evaluation
    - Content and structure analysis
    - Delivery and confidence feedback
    - Grammar corrections with examples
    - Overall impression
    - 3–5 improvement suggestions
    """
    if chain is None or parser is None:
        raise Exception("Chain not loaded. Call load_saved_artifacts() first.")

    result = chain.invoke({"input": speech})
    text_output = getattr(result, "content", str(result))

    try:
        feedback = parser.parse(text_output)
    except Exception as e:
        print("Parsing failed:", e)
        feedback = {"error": "Failed to parse model output", "raw_output": text_output}

    return feedback


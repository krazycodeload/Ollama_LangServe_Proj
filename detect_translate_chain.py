from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain.chains import SimpleSequentialChain, LLMChain
from langchain_groq import ChatGroq

# llm = ChatOllama(model="mistral")  # or llama3, gemma, etc.
llm=ChatGroq(model="Gemma2-9b-It",groq_api_key="your_groq_api_key")  # or llama3, gemma, etc.

# Step 1: Detect language
detect_prompt = ChatPromptTemplate.from_template(
    "What language is the following text written in?\n\nText: {text}\n\nLanguage:"
)
detect_chain = LLMChain(llm=llm, prompt=detect_prompt)

# Step 2: Translate
translate_prompt = ChatPromptTemplate.from_template(
    "Translate the following text from {source_lang} to {target_lang}:\n\n{text}"
)
translate_chain = LLMChain(llm=llm, prompt=translate_prompt)

# Combine both chains
def detect_and_translate(inputs: dict) -> dict:
    detected_lang = detect_chain.run({"text": inputs["text"]}).strip()
    result = translate_chain.run({
        "text": inputs["text"],
        "source_lang": detected_lang,
        "target_lang": inputs["target_lang"]
    })
    return {"translation": result, "detected_language": detected_lang}

from langchain_core.runnables import RunnableLambda
final_chain = RunnableLambda(detect_and_translate)

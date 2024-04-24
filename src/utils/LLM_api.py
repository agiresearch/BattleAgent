from openai import OpenAI
import anthropic
import os

def run_claude(message):
    api_client = anthropic.Anthropic(
        # api_key = ""
        api_key = os.getenv('CLAUDE_API_KEY')
    )
    # system_prompt = "You are a rational assistant that carefully answer the question."
    message = api_client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=3000,
        temperature=1,
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return message.content[0].text

def run_gpt(text_prompt, temperature: float = 0, model="gpt-4-1106-preview", seed=440):
    # open_ai_key = ""
    open_ai_key = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=open_ai_key)
    
    response = client.chat.completions.create(
        model=model, 
        messages=[{"role": "user", "content": text_prompt}],
        temperature=temperature,
        seed=seed  
    )

    resp = response.choices[0].message.content   
    resp = resp.replace("""```json""", '').replace("""```""", '') 
    return resp

def run_LLM(model_type, prompt):
    if model_type == "gpt":
        return run_gpt(prompt)
    elif model_type == "claude":
        return run_claude(prompt)
    else:
        raise ValueError(f"Unknown model type: {model_type}")
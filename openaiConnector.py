


import openai
import sys

def check_api_key_validity(key):
    """
    Checks if the given OpenAI API key is valid.

    Parameters
    ----------
    key : str
        OpenAI API key

    Returns
    -------
    None

    Raises
    ------
    OpenAIError
        If the given key is invalid
    """
    try:
        openai.api_key = key
        print("OpenAI API key is valid", file=sys.stderr)
    except openai.OpenAIError:
        print("Invalid OpenAI API key", file=sys.stderr)
        exit()


def call_AI_chatGPT(prompt):
    """
    Calls the OpenAI chat completion API with the given prompt.

    Parameters
    ----------
    prompt : str
        Prompt for the chat completion API

    Returns
    -------
    str
        Response from the chat completion API
    """
    messages = [{'role': 'system', 'content': 'You are a excellent programmer. Write the code to execute the given task. Always write only the raw code and nothing more, no quotes. Never write english, nor code delimiters.'}, {'role': 'user', 'content': prompt}]
    model = 'gpt-3.5-turbo'
    temperature = 0
    max_tokens = 2048
    response = openai.ChatCompletion.create(messages=messages, model=model, temperature=temperature, max_tokens=max_tokens)
    response = response.choices[0]
    response = response['message']
    response = response['content']
    return response


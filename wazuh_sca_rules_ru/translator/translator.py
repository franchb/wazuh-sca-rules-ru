import os

import openai


def get_completion(prompt, api_key, model="text-davinci-003"):
    openai.api_key = api_key
    response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=150)
    return response.choices[0].text.strip()


# Example usage
if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    prompt = "Write a short poem about autumn."
    completion = get_completion(prompt, api_key)
    print(completion)

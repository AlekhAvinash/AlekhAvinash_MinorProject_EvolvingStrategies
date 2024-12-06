import os, dotenv # type: ignore
from litellm import completion # type: ignore

dotenv.load_dotenv()

def get_model_response(prompt):
	"""Sends a prompt to the LLM and returns the generated text."""

	response = completion(
		model="gpt-3.5-turbo",
		max_tokens=1024,
		messages=[
			{"role": "user", "content": prompt}
		]
	)

	return response

def llmRand(**kwargs):
	prompt = """
	        Flip a coin. Give me the output in one word.
	        """
	return int("head" in get_model_response(prompt).lower())

def llm(wts, acts, **kwargs):
    prompt = f"""
        You are a prisoner, and given a choice between confess and lie. What would you choose? Give one word reply.
        You've done this before and so far due to your choices you've spent {sum(acts)} years in prison.
        If you choose to lie, your partner may lie as well and you'd spend {wts[0][0]} years in prison, while they spends {wts[0][1]} years.
        If you choose to lie, your partner may cofess and you'd spend {wts[1][0]} years in prison, while they spends {wts[1][1]} years.
        If you choose to confess, your partner may lie and you'd spend {wts[2][0]} years in prison, while they spends {wts[2][1]} years.
        If you choose to confess, your partner may confess as well and you'd spend {wts[3][0]} years in prison, while they spends {wts[3][1]} years.
        """
    return int("confess" in get_model_response(prompt).lower())

def stg(**kwargs):
        return 1

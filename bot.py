import anthropic
import openai

from config import OPEN_API_KEY, OPEN_AI_MODEL, CLAUDE_AI_KEY, CLAUDE_AI_MODEL, BOT

# OpenAI API key
openai.api_key = OPEN_API_KEY

claude = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=CLAUDE_AI_KEY,
)


def chat_with_claude(prompt):
    context = [{"role": "user",
                "content": "Please output the answer the choices of questions, no explain. No repeat the questions. Ignore the rest of the text that seems meaningless " + prompt}]
    response = claude.messages.create(
        model=CLAUDE_AI_MODEL,
        max_tokens=1024,
        messages=context
    )
    answer = response.content[0].text

    # answer = response.choices[0].message.content
    return answer


class Bot:
    def __init__(self):
        # self.gpt_content = "This is the interview session, please answer the questions in definitive statements (adding examples if any)"
        # self.claude_content = [
        #     {
        #         "type": "text",
        #         "text": "You are in the interview session, please answer the questions in definitive statements (adding examples if any)"}
        # ]
        self.context = [
            {
                "role": "system",
                "content": "Please output the answer the choices of questions, no explain. No repeat the questions. Ignore the rest of the text that seems meaningless."
            }
        ]

    def ask_question(self, question):
        if BOT == "gpt":
            return self.chat_with_gpt(question)
        elif BOT == "claude":
            return chat_with_claude(question)
        else:
            return self.chat_with_gpt(question)

    def clear_context(self):
        self.context = [
            {
                "role": "system",
                "content": "Please answer the questions shortly, no need to explain. Ignore the rest of the text that seems meaningless."
            }
        ]

    def chat_with_gpt(self, prompt):
        self.context.append({"role": "user", "content": prompt})
        response = openai.chat.completions.create(
            model=OPEN_AI_MODEL,
            messages=self.context
        )
        answer = response.choices[0].message.content
        self.context.append({"role": "assistant", "content": answer})
        return answer

import gradio as gr

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = "tiiuae/falcon-7b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_path)

model = AutoModelForCausalLM.from_pretrained(
    model_path, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map="auto"
)

from instruct_pipeline import InstructionTextGenerationPipeline

pipeline = InstructionTextGenerationPipeline(
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=128,
    return_full_text=True,
    task="text-generation",
)

from langchain.llms import HuggingFacePipeline

local_llm = HuggingFacePipeline(pipeline=pipeline)


from langchain import ConversationChain
from langchain.memory import ConversationBufferMemory

memory=ConversationBufferMemory()

conversation_buff = ConversationChain(llm=local_llm, memory=memory)

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")


    def user(user_message, history):
        return "", history + [[user_message, None]]


    def bot(history):
        history[-1][1] = conversation_buff(history[-1][0])["response"]
        return history
    

    def reset():
        memory.clear()
        pass

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(reset, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch()
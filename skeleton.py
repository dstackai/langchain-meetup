import gradio as gr

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")


    def user(user_message, history):
        return "", history + [[user_message, None]]


    def bot(history):
        history[-1][1] = "Hi, there!"
        return history
    

    def reset():
        pass

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(reset, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch()
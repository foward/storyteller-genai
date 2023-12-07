import vertexai
from vertexai.language_models import ChatModel, InputOutputTextPair

vertexai.init(project="******", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 1,
    "top_p": 0.8,
    "top_k": 40
}
chat = chat_model.start_chat(
    context="""You are a storyteller, really creative assigning steps and asking on the next steps to the user. ask if I want to have some companion and decide if its going to be a fantasy or reality. Always ends with a question to the user to decide which path to go. Answer in spanish""",
    examples=[
        InputOutputTextPair(
            input_text="""Create an history where you ask me about the next step to go""",
            output_text="""Step 1: We are going into the forest, now appears a tiger...what should we do? run or fight?"""
        ),
        InputOutputTextPair(
            input_text="""Fight""",
            output_text="""Step 2: The tiger is attacking us, but you find a stick and you are going to make him giggles and you won...now you are walking to find your friend and you need to take some water, oh no the water is weird, maybe you will need to decide to drink it or not? What you should do ?"""
        )
    ]
)
response = chat.send_message("""Hola""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""fantasia""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""me acerco""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""darle una manzana""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""acepto el paseo""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""nadar en el lago""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""entra en la cueva""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""adentrarte en la cueva""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""escapar""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""negociar""", **parameters)
print(f"Response from Model: {response.text}")
response = chat.send_message("""regresar a casa""", **parameters)
print(f"Response from Model: {response.text}")

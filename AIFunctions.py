from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def Human_to_AI_Chat():
    print("Sure! Let's start a Human-to-AI chat using DialoGPT-large.")
    try:
        model_name = "microsoft/DialoGPT-large"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name).eval()

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)

        message = input("Enter your message: ")
        history = None
        max_context = 1024

        input_ids = tokenizer.encode(message + tokenizer.eos_token, return_tensors='pt').to(device)
        if history is not None:
            input_ids = torch.cat([history, input_ids], dim=-1)
        if input_ids.shape[-1] > max_context:
            input_ids = input_ids[:, -max_context:]

        output_ids = model.generate(
            input_ids,
            max_length=input_ids.shape[-1] + 100,
            pad_token_id=tokenizer.eos_token_id,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            do_sample=True
        )
        response = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True).strip()
        print("🤖 AI:", response)
    except Exception as e:
        print("Something went wrong:", e)
def AI_to_AI_Chat():
    print("Sure! Let's run an AI-to-AI chat session using DialoGPT-large.")
    try:
        model_name = "microsoft/DialoGPT-large"

        tokenizer_1 = AutoTokenizer.from_pretrained(model_name)
        model_1 = AutoModelForCausalLM.from_pretrained(model_name).eval()

        tokenizer_2 = AutoTokenizer.from_pretrained(model_name)
        model_2 = AutoModelForCausalLM.from_pretrained(model_name).eval()

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model_1.to(device)
        model_2.to(device)

        message = input("Enter starting topic/message: ")
        num_turns = int(input("Enter number of turns: "))

        history_1 = None
        history_2 = None
        past_responses_ai1 = set([message.strip().lower()])
        past_responses_ai2 = set()
        invalid_responses = {" "}
        max_context = 1024
        max_retries = 10

        print("🤖 AI1:", message)

        for turn in range(num_turns):
            # AI1 generates response
            input_ids = tokenizer_1.encode(message + tokenizer_1.eos_token, return_tensors='pt').to(device)
            if history_1 is not None:
                input_ids = torch.cat([history_1, input_ids], dim=-1)
            if input_ids.shape[-1] > max_context:
                input_ids = input_ids[:, -max_context:]

            for attempt in range(max_retries):
                output_ids = model_1.generate(
                    input_ids,
                    max_length=input_ids.shape[-1] + 100,
                    pad_token_id=tokenizer_1.eos_token_id,
                    temperature=0.7,
                    top_k=50,
                    top_p=0.95,
                    do_sample=True
                )
                response_1 = tokenizer_1.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True).strip()
                if response_1.lower() not in past_responses_ai1 and response_1.lower() not in invalid_responses and len(response_1) > 2:
                    break
            else:
                response_1 = tokenizer_1.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True).strip()

            print("🤖 AI1:", response_1)
            past_responses_ai1.add(response_1.lower())
            history_1 = torch.cat([input_ids, output_ids[:, input_ids.shape[-1]:]], dim=-1)
            message = response_1
            if response_1.lower() == "bye":
                break

            # AI2 generates response
            input_ids = tokenizer_2.encode(message + tokenizer_2.eos_token, return_tensors='pt').to(device)
            if history_2 is not None:
                input_ids = torch.cat([history_2, input_ids], dim=-1)
            if input_ids.shape[-1] > max_context:
                input_ids = input_ids[:, -max_context:]

            for attempt in range(max_retries):
                output_ids = model_2.generate(
                    input_ids,
                    max_length=input_ids.shape[-1] + 100,
                    pad_token_id=tokenizer_2.eos_token_id,
                    temperature=0.7,
                    top_k=50,
                    top_p=0.95,
                    do_sample=True
                )
                response_2 = tokenizer_2.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True).strip()
                if response_2.lower() not in past_responses_ai2 and response_2.lower() not in invalid_responses and len(response_2) > 2:
                    break
            else:
                response_2 = tokenizer_2.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True).strip()

            print("🤖 AI2:", response_2)
            past_responses_ai2.add(response_2.lower())
            history_2 = torch.cat([input_ids, output_ids[:, input_ids.shape[-1]:]], dim=-1)
            message = response_2
            if response_2.lower() == "bye":
                break

        print("\n🤝 AI-to-AI chat finished.")
    except Exception as e:
        print("Something went wrong:", e)
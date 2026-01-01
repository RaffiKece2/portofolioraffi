from transformers import GPT2LMHeadModel, GPT2Tokenizer
import pyttsx3
import random
import cv2

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
engine = pyttsx3.init()
engine.setProperty("rate",150)
engine.setProperty("volume",1.0)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
    
model.config.pad_token_id = tokenizer.pad_token_id

face_ref = cv2.CascadeClassifier("face_smile.xml")

cam = cv2.VideoCapture(0)


def face_smile(frame):
    optimized = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    faces = face_ref.detectMultiScale(optimized,scaleFactor = 1.1,minSize = (500,500),minNeighbors = 3)
    return faces
    
    pass



def camera_detection():
    while True:
        _,frame = cam.read()
        cv2.imshow("kamera",frame)
        
       



def generate_responses(prompt):
    input = tokenizer(prompt,return_tensors = "pt",padding = True,truncation = True, max_length = 512)
    
    attention_mask = input['attention_mask'] if 'attention_mask' in input else None
    
    output = model.generate(
        input['input_ids'],
        attention_mask = attention_mask,
        max_length = 50,
        num_return_sequences = 1,
        pad_token_id = tokenizer.pad_token_id,
        no_repeat_ngram_size = 2,
        top_p = 0.9,
        temperature = 0.7,
        do_sample = True
        
    )
    
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response


def generate_responses_1(prompt):
    input = tokenizer(prompt,return_tensors = "pt",padding = True,truncation = True, max_length = 512)
    
    attention_mask = input['attention_mask'] if 'attention_mask' in input else None
    
    output = model.generate(
        input['input_ids'],
        attention_mask = attention_mask,
        max_length = 50,
        num_return_sequences = 1,
        pad_token_id = tokenizer.pad_token_id,
        no_repeat_ngram_size = 2,
        top_p = 0.8,
        temperature = 0.5,
        do_sample = True
        
    )
    
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def generate_responses_2(prompt):
    input = tokenizer(prompt,return_tensors = "pt",padding = True,truncation = True, max_length = 512)
    
    attention_mask = input['attention_mask'] if 'attention_mask' in input else None
    
    output = model.generate(
        input['input_ids'],
        attention_mask = attention_mask,
        max_length = 50,
        num_return_sequences = 1,
        pad_token_id = tokenizer.pad_token_id,
        no_repeat_ngram_size = 2,
        top_p = 0.6,
        temperature = 1.0,
        do_sample = True
        
    )
    
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

jarvis_respon = [
    generate_responses,
    generate_responses_1,
    generate_responses_2
]



greetings = [
    "Halo i am Jarvis",
    "Ash You Wish!!",
    "Hai How Are you",
    "What's Up Now!!!",
    "What's Wrong Sir!!!",
    "Did You Call Me???",
    "Why, is there something to talk about??",
    "Hello, how can I help you today?",
    "Yes Sir?? What is it",
    "I know you will need me, just ask",
    "where have you been today??",
    "hello are you calling me??",
    "Yes sir, just ask, I can answer it"
    
]
    
    
    
def chatbot():
    jarvis_greetings = random.choice(greetings)
    print(jarvis_greetings)
    engine.say(jarvis_greetings)
    engine.runAndWait()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye","exit","quit"]:
            close = generate_responses(user_input)
            print(close)
            engine.say(close)
            engine.runAndWait()
            break
        if user_input.lower() in ["kamera"]:
            camera_feedback = camera_detection()
            if "tidak melihat" in camera_feedback:
                prompt = "There is no one in front of the camera. How can I help?"
            else:
                prompt = f"user said camera {camera_feedback}"
            response = generate_responses(prompt,)
            print(f"Jarvis: {response}")
            engine.say(response)
            engine.runAndWait()
        
        responses = random.choice(jarvis_respon)
        hasil = responses(user_input)
        print(f"Jarvis: {hasil}")
        engine.say(hasil)
        engine.runAndWait()
    
    
if __name__ == "__main__":
    chatbot()
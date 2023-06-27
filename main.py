from argparse import ArgumentParser, Namespace
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from diffusers import StableDiffusionPipeline
from transformers import pipeline

import torch

def main():
    inquirer.text(message="Welcome to this fancy.....CLI app ¯\_(ツ)_/¯").execute()
    choice = inquirer.select(
        message="Pick your choice of whim:", 
        choices=[
            Choice("Generate an art piece", name="Generate Art"),
            Choice("Tell me a joke", name="Joke")
        ]
    ).execute()
    
    if choice == "Generate an art piece":
        model_id = "runwayml/stable-diffusion-v1-5"
        pipeline = StableDiffusionPipeline.from_pretrained(model_id, torch_type=torch.float16)
        # pipeline = pipeline.to("cuda")
        
        text_to_generate = inquirer.text(message="What kind of art do you want to generate today?").execute()
        image = pipeline(text_to_generate).images[0]
        
        image.save("generative_art.png")
    elif choice == "Tell me a joke":
        joke_feed = inquirer.text("Write half a joke so the computer can generate the rest: ").execute()
        generator = pipeline('text-generation',
                     model='huggingtweets/dadsaysjokes')
        generator(joke_feed, num_return_sequences=5)
    
    
if __name__ == "__main__":
    main()
    
    
# parser = ArgumentParser()

# parser.add_argument('square', help='Squares a given number', type=int, default=0, nargs='?')
# parser.add_argument('-v', '--verbose', help='Verbose description. Use -vv for extra verbose', 
#                     action='count')
# args: Namespace = parser.parse_args()
# result: int = args.square**2

# if args.verbose == 1:
#     print(f"The result is: {result}")
# elif args.verbose == 2:
#     print(f"{args.square} squared is: {args.square**2}. ")
# else:
#     print(args.square**2)
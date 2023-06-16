from argparse import ArgumentParser, Namespace
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from diffusers import StableDiffusionPipeline
import torch

def main():
    inquirer.text(message="Welcome to this fancy.....CLI app ¯\_(ツ)_/¯").execute()
    choice = inquirer.select(
        message="Pick your choice of whim:", 
        choices=[
            Choice("Generate an ASCII art", name="Generate ASCII"),
            Choice("Tell me a joke", name="Joke")
        ]
    ).execute()
    
    if choice == "Generate an ASCII art":
        model_id = "runwayml/stable-diffusion-v1-5"
        pipeline = StableDiffusionPipeline.from_pretrained(model_id, torch_type=torch.float16)
        # pipeline = pipeline.to("cuda")
        
        text_to_generate = inquirer.text(message="What do you want to ascii today?").execute()
        image = pipeline(text_to_generate).images[0]
        
        image.save("generative_art.png")
    elif choice == "Tell me a joke":
        print("I'll tell you a joke later")
        # api to generate a random joke of the day text
    
    
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
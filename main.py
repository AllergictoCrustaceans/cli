from argparse import ArgumentParser, Namespace
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from transformers import pipeline

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
        text_to_generate = inquirer.text(message="What do you want to ascii today?").execute()
        text_to_generate.strip()
        print(text_to_generate)
        #  test if huggingface API works here. use default sentiment analysis for now.
        classifier = pipeline(task="sentiment-analysis")
        preds = classifier(text_to_generate)
        preds = [{"score": round(pred["score"], 4), "label": pred["label"]} for pred in preds]
        print(preds)
        # api to generate a picture given string
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
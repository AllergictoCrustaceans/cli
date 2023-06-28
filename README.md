# Generate Artpiece or Joke from the CLI

Exactly what the header says! :D 

This is a CLI application and the `main.py` module is a code sample of how to use [InquirerPy](https://inquirerpy.readthedocs.io/en/latest/index.html) to create a more user-friendly CLI app flow.

### How to Use:
1. `git clone` the repo above
2. Run `python main.py` on the terminal
3. Follow the instructions!

### Libraries and services used:
- InquirerPy -- to add a more user-friendly CLI UX experience
- HuggingFace models ([dadsaysjokes](https://huggingface.co/huggingtweets/dadsaysjokes?text=my+life+is), and [stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5))
  1. dadsaysjokes - a transformer model that generates a joke based on the starter text the user provides
  2. stable diffusion model - a text-to-image diffusion model generates an art piece based on the prompt the user provides
 
### Motivation Behind this Project:
I wanted to dispell my anxiety around building a CLI app, so the best way to do it is to build one. This may be a simple one (and it doesn't even use argparse!), but starting off simple is the first step to getting comfortable with the uncomfortable, the complex, and the bigger CLI applications. Hoping to expand this in the future!

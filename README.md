# Music Blocks Lesson Plan Generation with Llama2
This project takes existing Music Blocks lesson plans, uses the data as input into a local copy of a Llama 2 language model, and outputs a new, unique lesson plan pertaining to music/computing based on the user's inputted prompt.

## Setup
To install the requirements to run this project, make sure you have the latest version of Python installed on your local machine. Create a virtual environment using the command: python -m venv (virtual environment name here).

Next, activate your virtual environment using the command: (virtual environment name here)/scripts/activate

Finally, use the command: pip install -r ./requirements.txt to install the required packages. 

## A Note on LLama2 Models
This project utilizes the LLama2-7B model with q2-k quantization. This model is 2.87 GB, and requires at most 5.37 GB of RAM to run. This model is the most lightweight model available through HuggingFace. You can download different models or read more about these models [here](https://huggingface.co/TheBloke/Llama-2-7B-GGML). 

## How To Run

1. Create a Python virtual environment for this project and run the command 'pip install -r requirements.txt'.
2. Run lessonPlanAnalyzer.py to generate a faiss (Facebook AI Similarity Search) directory using either recursive or natural language chunking. Chunking size and overlaps for recursive chunking can be adjusted. 
3. Run lessonPlanGeneratorNLTK.py to leverage Llama-2 with the 'faissNLTK' directory created from the lesson analyzer file, or run lessonPlanGeneratorRecursive.py to use the files in the 'faissRecursive' directory. When prompted, enter a topic for Llama-2 to generate a lesson plan for. You can customize many parameters in this file to get different results. 




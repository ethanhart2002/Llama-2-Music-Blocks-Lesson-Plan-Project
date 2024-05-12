# Music Blocks Lesson Plan Generation with Llama2
This project takes existing Music Blocks lesson plans, uses the data as input into a local copy of a Llama 2 language model, and outputs a new, unique lesson plan pertaining to music/computing based on the user's inputted prompt.

## A Note on LLama2 Models
This project is dependent on downloading a LLama2-7B model in a 'ggml' format. These models can be downloaded from HuggingFace [here](https://huggingface.co/TheBloke/Llama-2-7B-GGML). The most tested model for this project is titled 'llama-2-7b.ggmlv3.q2_K.bin'. This model is 2.87 GB, and requires at most 5.37 GB of RAM to run. This model is the most lightweight model available through HuggingFace. 

## Setup

1. Visit the [HuggingFace repository](https://huggingface.co/TheBloke/Llama-2-7B-GGML) and download a copy of Llama-2 (most tested and smallest model: 'llama-2-7b.ggmlv3.q2_K.bin'). Place your llama-2-7b .bin file in this project's directory.
2. To install the requirements to run this project, make sure you have the latest version of Python installed on your local machine. Create a virtual environment using the command: python -m venv (virtual environment name here).
3. Next, activate your virtual environment using the command: (virtual environment name here)/scripts/activate
4. Finally, use the command: pip install -r ./requirements.txt to install the required packages. 

## How To Run

1. Run lessonPlanAnalyzer.py to generate a faiss (Facebook AI Similarity Search) directory using either recursive or natural language chunking. Chunking size and overlaps for recursive chunking can be adjusted. 
2. Run lessonPlanGeneratorNLTK.py to leverage Llama-2 with the 'faissNLTK' directory created from the lesson analyzer file, or run lessonPlanGeneratorRecursive.py to use the files in the 'faissRecursive' directory. When prompted, enter a topic for Llama-2 to generate a lesson plan for. You can customize many parameters in this file to get different results. 




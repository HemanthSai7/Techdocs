# Techdocs: A code documentation generator

## Introduction

**Code Documentation Generation** is a tool that generates documentation for your code. It is a simple tool that can be used by anyone who wants to generate documentation for their code. It leverages the power of **OpenAI GPT-3, Huggingface Transformers, Langchain and Clarifai** to generate documentation for your code. 

To use the application, you need to provide your code as input. The tool will analyze your code and generate documentation for it. The documentation will include comments, descriptions, parameters, return values, examples, and more.

It is a useful tool for developers who want to document their code without spending too much time and effort. It can help you improve the readability, maintainability, and quality of your code. It can also help you share your code with others more easily.

## Installation
> Download zip or Clone the repository and run the following command in the terminal to install the required packages. 

> We recommend using a virtual environment for the installation. 

```bash
$ git clone https://github.com/HemanthSai7/Techdocs
$ cd Techdocs
$ pip install -r requirements.txt
$ -- Run backend
$ uvicorn app:app --reload # For running the FastAPI server
$ -- Run frontend
$ streamlit run app.py # For running the Streamlit App
```

## Streamlit App
- Head over to the [Website](https://techdocs.streamlit.app) and `signup/login` to use the tool.
- Once you are logged in, Head over to [Code](techdocs.streamlit.app/Code) page and generate your `API KEY` by clicking on the `Generate API KEY` button. Please note that the API KEY will be visible only once and you need to copy it and save it somewhere safe.
- Copy the API KEY and paste it in the `API KEY` field in the [Code](techdocs.streamlit.app/Code)
- Now, you can paste your code in the `Code` field and click on the `Generate Documentation` button.
- The generated documentation will be displayed in the `Documentation` field.

## Tech Stack Used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Azure](https://img.shields.io/badge/azure_SQL-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-EA6566?style=for-the-badge&logo=streamlit&logoColor=white)
![Langchain](https://img.shields.io/badge/Langchain-F70A8D?style=for-the-badge&logo=langchain&logoColor=white)
![Clarifai](https://img.shields.io/badge/Clarifai-FFA500?style=for-the-badge&logo=clarifai&logoColor=white)
# MSP-ML-Backend

Machine learning backend of a scholarship group project I've worked on. It is powered by multiple ResNet50-based models to classify clothing just with a single image as an input.

## Technical Information

- **Programming Language:** Python 3.12
- **Machine Learning Framework:** PyTorch
- **API Framework:** FastAPI
- **Server:** Uvicorn
- **Deployment:** Docker

Further information can be found within the `requirements.txt` file.

## Features

- Classifies clothing into multiple categories (e.g., article type, base color, season, usage) using self-trained ResNet-50 models. This is also known as Multi-Label Image Classification.
- Easy API access built-in, allowing seamless integration with other services or applications.
- Dockerized setup for quick and easy deployment.

## Project Structure

This is the basic project structure:

```
MSP-ML-Backend
├── .env
├── main.py
├── requirements.txt
├── api
│   ├── v1
│   │   ├── api.py
│   │   └── endpoints.py
├── core
│   ├── labels
│   │   ├── article_types.pkl
│   │   ├── base_colours.pkl
│   │   ├── seasons.pkl
│   │   └── usages.pkl
│   ├── models
│   │   └── place_models_here.txt
│   └── scripts
│       └── classification.py
└── temp
    └── temp_image.jpg
```

- `.env`: Holds necessary variables for the project to work (needs to be created by the user)
- `main.py`: Entry point of the application
- `requirements.txt`: List of all dependencies for the project
- `api`: Holds all api versions and endpoints of the project
- `core`
  - `labels`: Pickled files of the labels
  - `models`: Models for each label
  - `scripts`: Scripts for classification and utils used in the api
- `temp`: Temporary storage for e.g. input images received via an api request

## Basic Usage (Docker)

1. Download each `.pt` model file from my [Hugging Face repo](https://huggingface.co/g-gertz/MSP-ML-Backend-Models/tree/main)
2. Place these models under `core/models`
3. You need to have `docker` installed
4. Set up the docker container with `docker build -t msp-ml-backend .`
5. Run the container with `docker run -d -p 9999:9999 msp-ml-backend`

## Basic Usage (Local)

1. Download each `.pt` model file from my [Hugging Face repo](https://huggingface.co/g-gertz/MSP-ML-Backend-Models/tree/main)
2. Place these models under `core/models`
3. You need to have `Python 3.10` or greater
4. Set up a virtual environment with `python -m venv .venv`
5. Activate the virtual environment with `source .venv/Scripts/activate` (the path and file may change, depending on
   your operating system)
6. Install all dependencies with `pip install -r requirements.txt`
7. Run the project with `python main.py`

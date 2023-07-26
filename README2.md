
# Language Model Prompt Library API

This project is a RESTful API built with Python and Flask. It provides an interface for a language model prompt library.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Docker installed on your machine to build and run the application in a Docker container.

### Installing

To install the application, follow these steps:

1. Clone the repository
2. Navigate to the project directory
3. Build the Docker image:
   ```
   docker build -t prompt-library-api .
   ```
4. Run the Docker container:
   ```
   docker run -p 5000:5000 prompt-library-api
   ```

The application should now be running at `localhost:5000`.

## API Endpoints

The API provides the following endpoints:

- GET /prompts: Retrieve all prompts
- POST /prompts: Create a new prompt
- PUT /prompts/<id>: Update an existing prompt
- DELETE /prompts/<id>: Delete a prompt

## Built With

- [Python](https://www.python.org/) - The programming language used
- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL toolkit and ORM
- [Docker](https://www.docker.com/) - Used for containerization

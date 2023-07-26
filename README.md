# Product Catalog API

This repository contains a RESTful API built with Python, Flask, SQLAlchemy, and Docker. This API provides an interface for a language model prompt library. It's designed to be lightweight, efficient, and easy to understand and modify.

# Design Decisions
## Database

The database is a SQLite database. SQLite is a lightweight, file-based SQL database that is ideal for small applications like this one. The database is stored in the `database/` directory. It contains a single table, `prompts`, which stores the prompts in the library. The database schema is defined in `database/models.py`.

## ORM

The ORM used in this project is SQLAlchemy. SQLAlchemy is a Python library that provides a high-level interface for interacting with SQL databases. It provides a Pythonic interface for defining database schemas and querying databases.

## Web Framework

The API uses Flask as a web framework. Flask was chosen because it's lightweight, easy to use, and works well with SQLAlchemy.


## Deployment

The application is deployed to Azure using Docker.

## Documentation

The API documentation is generated using Swagger. Swagger is a tool that allows developers to document their APIs in a machine-readable format. It provides a web interface for exploring and interacting with the API.


## Project Structure

Here is the project directory structure:
#TODO update this

## Tech Stack

* Python 3.8
* Flask
* SQLAlchemy
* Docker
* Azure (for deployment)



Table of Contents
Technologies
Installation
API Documentation
Tests
Deployment
Contributing


## Future Improvements

Here are some ideas for future improvements:

* Add support for pagination
* Add support for sorting
* Add support for filtering
* Add support for searching





## Usage

This API provides a RESTful interface to a database of prompts. The API provides the following endpoints:

### GET /prompts



### POST /prompts


### PUT /prompts/{id}

This endpoint updates a prompt in the database. It accepts a JSON object as its request body.


### DELETE /prompts/{id}

This endpoint deletes a prompt from the database.

## Testing

You can run the unit tests for this API with the following command:

```bash
python -m unittest discover
```
# below are commande ideas
### Curl Commands
You can use the following curl commands to test the API:

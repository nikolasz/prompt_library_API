# Product Catalog API

This repository contains a RESTful API built with Python, Flask, SQLAlchemy, and Docker. This API provides an interface for a language model prompt library. It's designed to be lightweight, efficient, and easy to understand and modify.

## Project Structure

Here is the project directory structure:
#TODO update this

## Tech Stack

* Python 3.8
* Flask
* SQLAlchemy
* Docker
* Azure (for deployment)

## Usage

This API provides a RESTful interface to a database of prompts. The API provides the following endpoints:

### GET /prompts

This endpoint returns a list of prompts in the database. You can filter the list of prompts by passing query parameters to the endpoint. The following query parameters are supported:

* `category`: filter the list of prompts by category
* `prompt`: filter the list of prompts by prompt
* `max_length`: filter the list of prompts by maximum length
* `min_length`: filter the list of prompts by minimum length
* `limit`: limit the number of prompts returned
* `offset`: offset the returned prompts by the specified amount

### GET /prompts/{id}

This endpoint returns a single prompt by its ID.

### POST /prompts

This endpoint adds a prompt to the database. It accepts a JSON object as its request body. The JSON object should contain the following keys:

* `category`: the category of the prompt
* `prompt`: the prompt text
* `max_length`: the maximum length of the prompt
* `min_length`: the minimum length of the prompt

### PUT /prompts/{id}

This endpoint updates a prompt in the database. It accepts a JSON object as its request body. The JSON object should contain the following keys:

* `category`: the category of the prompt
* `prompt`: the prompt text
* `max_length`: the maximum length of the prompt
* `min_length`: the minimum length of the prompt

### DELETE /prompts/{id}

This endpoint deletes a prompt from the database.

## Testing

You can run the unit tests for this API with the following command:

```bash
python -m unittest discover
```

### Curl Commands

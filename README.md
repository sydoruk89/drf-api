# Django REST Framework / Docker

**Author:** Roman Sydoruk **Version:** 1.0.0

## Description

Django REST Framework to create an API, then “containerize” it with Docker.

## Architecture

* Python 3.8.3
* Poetry
* Django
* Docker

## Usage 
* Rebuild a custom version of Blog API demo project from scratch.
    * Replace Blog and Post with your own application and model.
    * Your model must have at least as many fields as demo’s model.
    * Your model must have one field that is a foreign key to user.
    * NOTE: You are not required to build any templates for this lab.
    * Update Dockerfile and docker-compose.yml if needed.
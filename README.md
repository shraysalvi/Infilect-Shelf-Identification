# Infilect Shelf Identification API

Welcome to the Infilect Shelf Identification API. This AI-driven solution helps retailers optimize their shelf space by precisely analyzing product arrangements, determining the area occupied by each brand, and labeling the area's shape accordingly.

## Problem Statement

Please refer to the `problem-statement.pdf` file for a detailed description of the task. Here's a brief overview:

Given a two-dimensional representation of a grocery store shelf with four Britannia products, the API identifies the shape of each brand. Each brand's area could be labeled as a horizontal rectangle, vertical rectangle, square, or irregular polygon based on its arrangement.

### Sample Inputs & Outputs

Provided in the problem statement are sample shelf layouts and their expected outputs after processing by our API. These can be found in the `problem-statement.pdf` file.

## Technical Implementation

### 1. API

This API is built using the Django Rest Framework. The core logic resides in `/api/views.py` where I:

- Validate the provided 2D matrix.
- Identify the product's shape and its location on the shelf using Depth-First Search (DFS) Graph.
- Respond with the shape and location of each product.

### 2. Docker

The whole application is containerized using Docker for ease of deployment. The Dockerfile sets up a Python environment, installs the necessary dependencies, and runs the application. We also provide a `docker-compose.yml` for easy to execute.

### 3. Testing

For testing the API, we've included a Postman collection. Load this collection in Postman to test various API endpoints and scenarios.

### 4. Note on Location Algorithm
The algorithm to determine the location of a shape was created from scratch, as the exact methodology wasn't specified in the problem statement. Our approach provides a precise position for each shape.

## Getting Started
#### Prerequisites
- Docker

### Running the Application

- Extract the zip file or Clone repository
`git clone [repository-link]`
- Navigate to the directory.
`cd [repository-name]`
- Run the Docker container
`docker-compose up`

- The API should now be accessible at `http://127.0.0.1:8000/api/shelf-identifier/` or `http://localhost:8000/api/shelf-identifier/`

- Load the provided Postman collection to test the API. Ensure that the application is running before initiating the tests.

## Feedback and Contributions
Your feedback is invaluable. Please send your suggestions, bug reports, and pull requests to improve this solution.


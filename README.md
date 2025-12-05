# Cloud-Native Microservice (NatWest Engineering Demo)

A containerized Python/Flask application demonstrating a full CI/CD pipeline using Docker, GitHub Actions, and Cloud PaaS.

**Live Demo:** [Click Here to View App](https://natwest-app.onrender.com/)

## Technologies
* **Core:** Python 3.9, Flask
* **Containerization:** Docker
* **CI/CD:** GitHub Actions (Automated Testing), Render (Auto-Deployment)
* **Testing:** Pytest

## Architecture
1.  **Development:** Code is written locally and containerized using Docker to ensure environment consistency.
2.  **Continuous Integration (CI):** Upon pushing to `main`, GitHub Actions triggers a workflow that installs dependencies and runs unit tests via `pytest`.
3.  **Continuous Deployment (CD):** If tests pass, the container is automatically built and deployed to the cloud (Render).
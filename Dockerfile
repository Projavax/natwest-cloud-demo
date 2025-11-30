# 1. Start with a lightweight version of Python (Linux based)
FROM python:3.9-slim

# 2. Set the folder inside the container where we will work
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install the dependencies inside the container
RUN pip install -r requirements.txt

# 5. Copy the rest of your code into the container
COPY . .

# 6. Tell Docker we want to use port 5001
EXPOSE 5001

# 7. The command to run when the container starts
CMD ["python", "app.py"]
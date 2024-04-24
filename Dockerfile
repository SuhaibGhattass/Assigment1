FROM python:alpine

# Set working directory
WORKDIR /code

# Copy the current directory contents into the container at /Ass1
COPY paragraphs.txt .

COPY Ass1.py .

# Install NLTK
RUN pip install nltk

# Download NLTK resources
RUN python -m nltk.downloader punkt

# Command to run the Python script
CMD python Ass1.py

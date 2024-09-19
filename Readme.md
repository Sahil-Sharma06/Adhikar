# Adhikar

Adhikar is a powerful, AI-driven legal research tool designed to help streamline the process of categorizing and analyzing Indian Commercial Law data. This project leverages modern web technologies like **React**, **FastAPI**, and **PostgreSQL** to create an intuitive interface and scalable backend, enabling users to explore legal documents, predict case outcomes, and categorize data efficiently.

## Features

- **Legal Document Categorization**: Automatically categorize over 4,000 rows of Indian Commercial Law data using machine learning models.
- **Predictive Analytics**: Apply machine learning algorithms to predict the outcomes of legal cases based on historical patterns.
- **Scalable Backend**: Built with FastAPI and PostgreSQL, ensuring real-time data processing and storage.
- **User-Friendly Interface**: Frontend powered by React and Tailwind CSS, delivering a seamless user experience.

## Tech Stack

### Frontend
- **React.js**: JavaScript library for building the user interface.
- **Tailwind CSS**: Utility-first CSS framework for fast UI development.
  
### Backend
- **FastAPI**: Fast, modern, and asynchronous Python web framework.
- **PostgreSQL**: Open-source relational database for secure and scalable data management.

### Machine Learning
- **Scikit-learn**: Used for applying machine learning algorithms to predict legal case outcomes.
  
## Setup & Installation

### Prerequisites

- **Node.js** and **npm** (for frontend)
- **Python 3.8+** (for backend)
- **PostgreSQL** (for database)

### Steps

1. **Clone the repository**

    ```bash
    git clone https://github.com/sushilpandeyy/Adhikar.git
    ```

2. **Frontend Setup**

    ```bash
    cd adhikar/frontend
    npm install
    npm start
    ```

    This will start the React development server.

3. **Backend Setup**

    ```bash
    cd adhikar/backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

4. **Database Setup**

    - Create a PostgreSQL database and configure the connection in `backend/config.py`.

5. **Run the Backend**

    ```bash
    uvicorn main:app --reload
    ```

    This will start the FastAPI server at `http://localhost:8000`.

## Usage

1. Open the frontend by navigating to `http://localhost:3000` in your browser.
2. Use the platform to upload legal documents, explore existing categorized data, and view predictive case outcomes.
3. The backend API will process the data and respond with real-time insights.

## Project Structure


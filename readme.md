# Blog App

This is a Blog App built with **FastAPI**, featuring user authentication, blog management, and secure integration with a PostgreSQL database.

## Features
- **User Authentication**:
  - JWT-based login system for secure access.
- **Blog Management**:
  - Create, update, delete, and view blogs.
- **Database Integration**:
  - Connected to PostgreSQL to store user and blog data.
- **Scalable Architecture**:
  - Modular design for easy scalability and maintainability.

## Tech Stack
- **Backend**: FastAPI
- **Database**: PostgreSQL
- **Authentication**: JSON Web Tokens (JWT)
- **Others**: Python, SQLAlchemy

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL installed and running

### Steps to Run
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/blogapp.git
   cd blogapp
   ```

5. **Start the Server**:
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the App**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

7. **Explore API Docs**:
   FastAPI provides an auto-generated interactive API documentation at:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## Project Structure
```plaintext
blogapp/
├── app/
│   ├── main.py         # Application entry point
│   ├── models.py       # Database models
│   ├── schemas.py      # Pydantic schemas
│   ├── utils.py        # Utility functions
|   ├── deps.py         # Dependency 
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
Feel free to reach out with any questions or suggestions:
- GitHub: [your-username](https://github.com/your-username)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)

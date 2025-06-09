# Tech Path Suggester (Django Version)

This application helps users discover a potential tech path based on their interests and tool comfort levels. It features a React frontend and a Django backend.

## Project Structure

techpath-project/
├── backend/
│   ├── manage.py          # Django management script
│   ├── techpath/          # Django project settings
│   ├── api/               # Django app for suggestion logic
│   └── build/             # Built React frontend static files
├── frontend/              # React Vite app source
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
├── requirements.txt       # Python dependencies (Django, DRF, etc.)
├── README.md
└── .gitignore

## Prerequisites

*   Python 3.8+
*   pip (Python package installer)
*   Node.js (LTS version recommended, includes npm)
*   yarn (can be installed via `npm install --global yarn`)

## Setup and Running

### 1. Backend (Django)

1.  **Navigate to the project root directory:**
    ```bash
    cd techpath-project
    ```

2.  **Create a Python virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

6.  **Run Django database migrations (to create necessary tables, including for admin):**
    ```bash
    python manage.py migrate
    ```

7.  **(Optional) Create a Django superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set a username, email (optional), and password.

### 2. Frontend (React + Vite)

1.  **Navigate to the frontend directory (from project root):**
    ```bash
    cd techpath-project/frontend
    ```

2.  **Install Node.js dependencies:**
    ```bash
    yarn install
    ```

### 3. Build Frontend and Run Django Server

1.  **Build the React application for production (from `techpath-project/frontend`):**
    ```bash
    yarn build
    ```
    This command compiles the React app and places the static assets into `frontend/dist/`. The build script in this project is configured to automatically copy these assets to `backend/build/`. (If this auto-copy is not working, manually copy `frontend/dist/*` to `backend/build/`.)

2.  **Navigate back to the backend directory (from `techpath-project/frontend`):**
    ```bash
    cd ../backend
    ```

3.  **Run the Django development server:**
    ```bash
    python manage.py runserver
    ```
    The application will typically be available at `http://127.0.0.1:8000/`. The Django server will serve both the API endpoints and the React frontend.

## How it Works

1.  The user accesses the web application, and Django serves the React frontend's `index.html` and static assets.
2.  The React app displays a form for users to input their tech interests, tool comfort, and preferred activities.
3.  Upon submission, the frontend sends this data to the `/api/suggest-path/` endpoint on the Django backend.
4.  The Django backend (using Django REST Framework) processes the request, applies a set of predefined rules to suggest a tech path (e.g., "Data Science", "Web Development"), and provides a reason for the suggestion.
5.  The frontend displays this suggestion to the user on a results page.

## Development Notes

*   **Frontend Development Server:** For faster frontend development with hot reloading, you can run the Vite development server separately:
    ```bash
    cd techpath-project/frontend
    yarn dev
    ```
    This will typically start the frontend on `http://localhost:5173`. You'll need to ensure your Django backend is also running (usually on `http://127.0.0.1:8000/`) and that the API calls from the Vite dev server can reach the Django server (CORS is enabled for this). Remember that `yarn dev` uses the development server and does not update the files in `backend/build/`.
*   **API Endpoint:** The API is available at `/api/suggest-path/`.
*   **Static Files:** Django is configured to serve static files from the `backend/build` directory in production-like mode when `DEBUG=False`. During development (`DEBUG=True`), Django's `runserver` can also serve these files. WhiteNoise is included for more robust static file serving.

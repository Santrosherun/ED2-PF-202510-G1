## How to Run This Project

### Prerequisites

- Python 3.10
- [Conda](https://docs.conda.io/en/latest/)
- All dependencies listed in `requirements.txt`

### Setup Instructions

1. **Clone the repository** and navigate to the project directory.

2. **Create and activate a conda environment**:
    ```bash
    conda create -n myenv python=3.10
    conda activate myenv
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set environment variables**  
    You need to set the following environment variables before running the project:
    - `DATABASE_NAME`
    - `DATABASE_PASSWORD`
    - `DATABASE_USERNAME`
    - `DATABASE_HOST`  

### Running the Project

1. **Start the server** (in one terminal):
    ```bash
    python server_side.py
    ```

2. **Start the client** (in another terminal):
    ```bash
    python client_side.py
    ```

---

Feel free to update the environment variable names and values as needed for your setup.
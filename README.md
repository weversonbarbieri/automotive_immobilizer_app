# Immobilizer Assistant

The **Immobilizer Assistant** is an application designed to assist in identifying the security system, download key relearn procedures for various vehicle brands. The application uses dataframes to store information and displays download buttons based on specified conditions.

## Features

- Identification of security system and key relearn procedures for various vehicle brands.
- Display of download buttons for identified procedures.
- Support for multiple vehicle makes and models.

## Project Structure

- `src/`: Contains the main source code for the application.
  - `Immo_Assistant.py`: Main application file containing the logic to identify and display download buttons and the security system.
- `data/`: Directory containing data files used by the application.
- `docs/`: Directory containing documentation files for the project.
- `notebooks/`: Directory containing Jupyter notebooks for data analysis and experimentation.
- `dataframe_each_make_xlsx_file/`: Directory containing Excel files with dataframes for each vehicle brand.
- `venv/`: Virtual environment directory containing installed dependencies.
- `requirements.txt`: File containing a list of dependencies required for the project.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/weversonbarbieri/immobilizer_assistant.app.git
    cd immobilizer_assistant.app
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    streamlit run src/Immo_Assistant.py
    ```

2. Access the application in your browser at:
    ```
    https://immobilizer-assistant.streamlit.app/
    ```

## Contribution

Contributions are welcome! Feel free to open issues and pull requests for improvements and fixes.

## Contact

For more information, contact [Weverson Barbieri](https://github.com/weversonbarbieri).









# Quizzler

Welcome to the Quizzler project! This is a simple quiz application that tests users on random true/false questions. The quiz is implemented using Python and utilizes a graphical user interface (GUI) built with Tkinter. The application fetches questions from an external API and allows users to interactively answer questions.

## Demo Video


https://github.com/user-attachments/assets/ef548eaf-31d6-4700-8ef1-54485d331e05


## Features

- **Fetches Random True/False Questions**: Retrieves quiz questions from the Open Trivia Database.
- **Graphical User Interface**: Provides a user-friendly interface with Tkinter.
- **Score Tracking**: Displays the user's score throughout the quiz and at the end.
- **Feedback on Answers**: Highlights answers in green for correct and red for incorrect responses.

## Table of Contents

- [Configuration](#configuration)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Configuration

The project does not require any specific configuration files. The `data.py` script fetches quiz questions from the Open Trivia Database API, so make sure you have internet access for this functionality.

## Usage

1. **Run the Application**:

   Execute the main script to start the quiz application.

   ```bash
   python main.py
   ```

   The application will open a window displaying the quiz questions and options to answer them.

## Code Overview

### `data.py`

- **Purpose**: Fetches a set of random true/false questions from the Open Trivia Database API and processes the response.
- **Key Variables**:
  - `parameters`: Defines the number of questions and their type.
  - `question_data`: Contains the questions and answers fetched from the API.

### `main.py`

- **Purpose**: Initializes the quiz by creating `Question` objects from the fetched data and sets up the quiz interface.
- **Key Components**:
  - `question_bank`: List of `Question` objects.
  - `quiz`: Instance of the `QuizBrain` class.
  - `quiz_ui`: Instance of the `QuizInterface` class.

### `question_model.py`

- **Purpose**: Defines the `Question` class used to represent quiz questions.
- **Attributes**:
  - `q_text`: The question text.
  - `q_answer`: The correct answer.
  - `q_category`: The category of the question.
  - `q_difficulty`: The difficulty level of the question.

### `quiz_brain.py`

- **Purpose**: Manages the quiz logic, including tracking the current question, checking answers, and providing feedback.
- **Key Methods**:
  - `still_has_question()`: Checks if there are more questions to answer.
  - `next_question()`: Retrieves the next question and increments the question number.
  - `check_answer(user_answer)`: Checks if the user's answer is correct.

### `ui.py`

- **Purpose**: Handles the graphical user interface (GUI) using Tkinter.
- **Key Components**:
  - `QuizInterface`: Initializes and manages the GUI, including buttons and score display.
  - `get_next_question()`: Updates the GUI with the next question or end of quiz message.
  - `pressed_true()` and `pressed_false()`: Handle user responses to the true/false questions.
  - `give_feedback(is_right)`: Provides visual feedback on the user's answer.

## Project Structure

- `data.py`: Script for fetching quiz questions from the API.
- `main.py`: Main script for running the quiz application.
- `question_model.py`: Contains the `Question` class definition.
- `quiz_brain.py`: Manages the quiz logic and user interaction.
- `ui.py`: Implements the Tkinter GUI for the quiz application.
- `requirements.txt`: List of required Python packages.
- `images/true.png`: Image for the "true" button.
- `images/false.png`: Image for the "false" button.

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please submit a Pull Request. Ensure that your contributions are well-documented and tested.


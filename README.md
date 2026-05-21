# Computer Science & Python Programming Basic

A structured collection of Python lessons, exercises, and projects used for teaching fundamental computer science and programming concepts.

---

## 📂 Repository Structure

The codebase is organized into modular sections covering CLI applications, Object-Oriented Programming (OOP), file manipulation, and game development:

```text
├── ConsoleEscapeGame/     # Text-based grid escape game (W, A, S, D controls)
├── StudentManager/        # CLI Student Management application (CRUD operations)
├── pygame/                # Pygame-based 2-player Pong game
├── OOP/                   # Exercises covering OOP classes, methods, and inheritances
│   ├── Lesson1.py         # Garage & Car system
│   ├── Lesson2.py         # Warehouse & Inventory manager
│   └── Lesson3.py         # Library Management System (LMS)
├── File_less/             # File Input/Output (I/O) lessons and notes
├── Dic/                   # Exercises and notes on Python Dictionaries
└── On tap/                # General review exercises and algorithm practices
```

---

## 🚀 Projects & How to Run

### 1. Student Manager CLI (`StudentManager/`)
A command-line interface application to manage student records (add, update, delete, and view profiles).
*   **To Run:**
    ```bash
    python3 StudentManager/main.py
    ```

### 2. Console Escape Game (`ConsoleEscapeGame/`)
A grid-based console game where the player `P` must find the key `K` and escape through the door `D` using `W, A, S, D` keys.
*   **Dependencies:** Requires `getch` module on macOS.
    ```bash
    pip install pygetch
    ```
*   **To Run:**
    ```bash
    python3 ConsoleEscapeGame/game.py
    ```

### 3. Pygame Pong Game (`pygame/`)
A classic 2-player Pong game utilizing the `pygame` library. Left player uses `W / S`, and right player uses `Up / Down` arrows.
*   **Dependencies:** Requires `pygame`.
    ```bash
    pip install pygame
    ```
*   **To Run:**
    ```bash
    python3 pygame/main.py
    ```

---

## 📚 Curriculum Topics Covered
*   **Variables & Data Types**: Fundamental logic, dictionaries, and list structures.
*   **File Handling (I/O)**: Working with text and binary files using standard open/write/append operations (`File_less/`).
*   **Object-Oriented Programming (OOP)**: Building classes, attributes, constructor functions, and instance methods (`OOP/`).
*   **Event-Driven Programming**: Handling user keyboard inputs and rendering sprites/game loops (`pygame/`).

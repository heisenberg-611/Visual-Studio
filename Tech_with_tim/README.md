# Ultimate Speed Typing Test

A feature-rich, terminal-based typing speed test written in Python using `curses`. Test your typing speed with randomized paragraphs, custom themes, and detailed error tracking.

## Features

- **Paragraph Typing**: Practice with meaningful, multi-sentence paragraphs instead of random words.
- **Modern Themes**: Choose from a variety of color themes to suit your style:
    - *Classic* (Green/Black)
    - *Neon* (Cyan/Magenta)
    - *Ocean* (Blue/White)
    - *Matrix* (Green/Black)
    - *Flame* (Yellow/Red)
    - *Candy* (Pink/White)
    - *Retro* (Yellow/Blue)
    - *Catppuccin* (Pastel/Black)
- **Cursor Customization**: Cycle through 7 different block cursor styles with a live preview in the menu.
- **Variable Time Limits**: Set your preferred test duration:
    - 15 Seconds
    - 30 Seconds
    - 60 Seconds (Standard)
    - Unlimited Mode
- **Real-time Feedback**:
    - Live WPM (Words Per Minute) calculation.
    - Error counter.
    - Countdown timer.
- **Robustness**: 
    - Text scrolling for long paragraphs.
    - Crash prevention for special keys.
    - Software cursor for guaranteed visibility on all terminals.

## Installation

1.  **Prerequisites**: You need Python 3 installed.
    *   *Note for Windows Users*: The `curses` library is not included with Python on Windows. You may need to install `windows-curses`:
        ```bash
        pip install windows-curses
        ```

2.  **Files**: Ensure you have the following files in the same directory:
    - `typing_test_improved.py` (The main script)
    - `paragraphs.txt` (Source text file)

## How to Run

Open your terminal or command prompt, navigate to the folder containing the script, and run:

```bash
python3 typing_test_improved.py
```

## How to Use

1.  **Main Menu**: Use the number keys to select an option:
    - `1`: **Start Test** - Begins the typing test immediately.
    - `2`: **Change Theme** - Cycles through available color themes.
    - `3`: **Change Cursor Color** - Cycles through cursor styles. Watch the preview next to the option!
    - `4`: **Set Time Limit** - Toggles between 15s, 30s, 60s, and Unlimited.
    - `5`: **Quit** - Exits the program.

2.  **During Test**:
    - Type the text exactly as shown.
    - **Correct** characters will turn green (or theme color).
    - **Incorrect** characters will turn red.
    - Use `Backspace` to correct mistakes.
    - Press `ESC` to abort the test and return to the menu.

3.  **Completion**:
    - The test ends when the time runs out OR when you finish typing the entire paragraph.
    - A results screen will show your final WPM and total errors.
    - Press any key to return to the menu.

## customization

To add your own text, simply edit the `paragraphs.txt` file. Separate distinct paragraphs with one or more empty lines.

## Legacy Version

The original version of this tool is available as `typing_test.py`. It provides a simpler, lightweight typing experience:
- **Single Line Mode**: Types random single sentences from `text.txt`.
- **Basic Feedback**: Standard green/red color coding for correct/incorrect characters.
- **No Menu**: Starts immediately upon running.
- **Endless Loop**: Automatically loads a new sentence after completion.

To run the legacy version:
```bash
python3 typing_test.py
```

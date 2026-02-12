import curses
from curses import wrapper
import time
import random

# Theme Configurations
THEMES = {
    "Classic": {
        "text": (curses.COLOR_GREEN, curses.COLOR_BLACK),
        "error": (curses.COLOR_RED, curses.COLOR_BLACK),
        "ui": (curses.COLOR_WHITE, curses.COLOR_BLACK)
    },
    "Neon": {
        "text": (curses.COLOR_CYAN, curses.COLOR_BLACK), # Modern Blue/Cyan
        "error": (curses.COLOR_MAGENTA, curses.COLOR_BLACK),
        "ui": (curses.COLOR_YELLOW, curses.COLOR_BLACK)
    },
    "Ocean": {
        "text": (curses.COLOR_BLUE, curses.COLOR_WHITE),
        "error": (curses.COLOR_RED, curses.COLOR_WHITE),
        "ui": (curses.COLOR_BLACK, curses.COLOR_WHITE)
    },
    "Matrix": {
        "text": (curses.COLOR_GREEN, curses.COLOR_BLACK),
        "error": (curses.COLOR_RED, curses.COLOR_BLACK),
        "ui": (curses.COLOR_GREEN, curses.COLOR_BLACK)
    },
    "Flame": {
        "text": (curses.COLOR_YELLOW, curses.COLOR_RED),
        "error": (curses.COLOR_WHITE, curses.COLOR_RED),
        "ui": (curses.COLOR_YELLOW, curses.COLOR_RED)
    },
    "Candy": {
        "text": (curses.COLOR_MAGENTA, curses.COLOR_WHITE),
        "error": (curses.COLOR_RED, curses.COLOR_WHITE),
        "ui": (curses.COLOR_BLUE, curses.COLOR_WHITE)
    },
    "Retro": {
        "text": (curses.COLOR_YELLOW, curses.COLOR_BLUE),
        "error": (curses.COLOR_RED, curses.COLOR_BLUE),
        "ui": (curses.COLOR_WHITE, curses.COLOR_BLUE)
    },
    "Catppuccin": {
        "text": (curses.COLOR_CYAN, curses.COLOR_BLACK),
        "error": (curses.COLOR_RED, curses.COLOR_BLACK),
        "ui": (curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    }
}

# Cursor Colors (Text, Background)
CURSOR_STYLES = [
    (curses.COLOR_WHITE, curses.COLOR_BLACK), # Inverted standard (becomes block)
    (curses.COLOR_WHITE, curses.COLOR_BLUE),
    (curses.COLOR_BLACK, curses.COLOR_WHITE),
    (curses.COLOR_WHITE, curses.COLOR_RED),
    (curses.COLOR_BLACK, curses.COLOR_CYAN),
    (curses.COLOR_WHITE, curses.COLOR_MAGENTA),
    (curses.COLOR_BLACK, curses.COLOR_YELLOW)
]

class TypingTest:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.current_theme = "Classic"
        self.cursor_style_idx = 0 # Default cursor style (inverted)
        self.time_limit = 60 # Default 60s
        self.load_theme()
        try:
            curses.curs_set(1) # Attempt to make hardware cursor visible
        except curses.error:
            pass

    def load_theme(self):
        """Initialize color pairs based on selected theme."""
        theme = THEMES[self.current_theme]
        cursor_style = CURSOR_STYLES[self.cursor_style_idx]
        
        curses.init_pair(1, theme["text"][0], theme["text"][1])    # Correct text / Target
        curses.init_pair(2, theme["error"][0], theme["error"][1])  # Error text
        curses.init_pair(3, theme["ui"][0], theme["ui"][1])        # UI Elements
        curses.init_pair(4, cursor_style[0], cursor_style[1])

    def start_screen(self):
        self.stdscr.clear()
        self.stdscr.attron(curses.color_pair(3))
        self.stdscr.addstr("Welcome to the Ultimate Speed Typing Test!")
        self.stdscr.addstr("\nPress any key to begin!")
        self.stdscr.attroff(curses.color_pair(3))
        self.stdscr.refresh()
        self.stdscr.getkey()

    def load_text(self):
        try:
            with open("paragraphs.txt", "r") as f:
                # Read specific paragraphs separated by newlines
                content = f.read()
                # Split by double newlines to get distinct paragraphs
                paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
            
            if not paragraphs:
                return "No text available in paragraphs.txt."

            # Select a random paragraph
            return random.choice(paragraphs)
        except FileNotFoundError:
            return "Error: paragraphs.txt file is missing!"

    def display_text(self, target, current, wpm=0, errors=0, start_time=0):
        self.stdscr.clear()
        height, width = self.stdscr.getmaxyx()
        
        # Calculate time left
        time_elapsed = max(time.time() - start_time, 1)
        time_left_str = "Unlimited"
        if self.time_limit > 0:
            remaining = max(0, self.time_limit - int(time_elapsed))
            time_left_str = f"{remaining}s"

        # Status Bar
        status = f"WPM: {wpm} | Errors: {errors} | Time Left: {time_left_str}"
        
        # Wrapping Logic
        # We need to manually wrap the text to fit the screen width
        # and handle scrolling if it exceeds height
        
        wrapped_lines = []
        current_line = ""
        
        # Use simple character wrapping or word wrapping? Simple char wrapping is easier for typing tests to match indices
        # strict character wrapping to match input key-by-key
        for char in target:
            if len(current_line) >= width:
                wrapped_lines.append(current_line)
                current_line = ""
            current_line += char
        if current_line:
            wrapped_lines.append(current_line)
            
        # Determine strict line_limit for text view (Height - 2 lines for status)
        view_height = height - 3 
        
        # Calculate visual cursor position
        cursor_index = len(current)
        cursor_row = cursor_index // width
        
        # Scroll Offset: Ensure cursor is visible
        scroll_offset = 0
        if cursor_row >= view_height:
             scroll_offset = cursor_row - view_height + 1

        # Display Visible Lines
        for row_idx in range(view_height):
            text_row_idx = row_idx + scroll_offset
            if text_row_idx >= len(wrapped_lines):
                break
                
            line_content = wrapped_lines[text_row_idx]
            
            # Print entire line in default color first
            self.stdscr.addstr(row_idx, 0, line_content, curses.color_pair(3))
            
            # Overlay typed characters
            # Calculate start index of this row in the original string
            row_start_index = text_row_idx * width
            
            for col_idx, char in enumerate(line_content):
                global_index = row_start_index + col_idx
                
                if global_index < len(current):
                    typed_char = current[global_index]
                    correct_char = target[global_index]
                    
                    color = curses.color_pair(1) # Correct
                    if typed_char != correct_char:
                        color = curses.color_pair(2) # Error
                    
                    self.stdscr.addstr(row_idx, col_idx, typed_char, color)
                elif global_index == len(current):
                    # Software Cursor: Use custom cursor color pair
                    self.stdscr.addstr(row_idx, col_idx, char, curses.color_pair(4) | curses.A_REVERSE)
                else:
                    # Untyped characters
                    self.stdscr.addstr(row_idx, col_idx, char, curses.color_pair(3))

        # Move hardware cursor as backup
        # Calculate where the cursor should be based on current_text length
        cursor_index = len(current)

        # Move cursor to the next character position
        # Calculate where the cursor should be based on current_text length
        cursor_index = len(current)
        cursor_row = (cursor_index // width) - scroll_offset
        cursor_col = cursor_index % width

        # Only move if within visible screen bounds
        if 0 <= cursor_row < view_height:
             try:
                self.stdscr.move(cursor_row, cursor_col)
             except curses.error:
                pass

        # Draw Status Bar at bottom
        try:
            self.stdscr.addstr(height - 1, 0, status[:width-1], curses.color_pair(3))
        except curses.error:
            pass
        
        # Ensure cursor is actually shown (move puts it there, but refresh needs to happen)
        self.stdscr.refresh()

    def run_test(self):
        target_text = self.load_text()
        current_text = []
        wpm = 0
        errors = 0
        start_time = time.time()
        self.stdscr.nodelay(True)

        while True:
            time_elapsed = max(time.time() - start_time, 1)
            
            # Check Time Limit
            if self.time_limit > 0:
                if int(time.time() - start_time) >= self.time_limit:
                    self.stdscr.nodelay(False)
                    return wpm, errors, "Time's Up!"

            # Calculate WPM
            # Standard: (chars / 5) / (minutes)
            wpm = round((len(current_text) / 5) / (time_elapsed / 60))

            self.display_text(target_text, current_text, wpm, errors, start_time)
            # Remove stdscr.refresh() here because it is called inside display_text after moving cursor
            
            # Check Completion
            if len(current_text) == len(target_text):
                self.stdscr.nodelay(False)
                return wpm, errors, "Completed!"

            try:
                key = self.stdscr.getkey()
            except curses.error:
                time.sleep(0.01)
                continue

            # Exit check
            if len(key) == 1 and ord(key) == 27:
                self.stdscr.nodelay(False)
                return wpm, errors, "Aborted"

            # Backspace
            if key in ("KEY_BACKSPACE", '\b', "\x7f"):
                if len(current_text) > 0:
                    current_text.pop()
            
            # Valid Input
            elif len(key) == 1:
                # Only add if we haven't exceeded target length
                if len(current_text) < len(target_text):
                    # Error Counting
                    if key != target_text[len(current_text)]:
                        errors += 1
                    current_text.append(key)
                
                
            # Check Completion (After input)
            if len(current_text) == len(target_text):
                self.stdscr.nodelay(False)
                curses.flushinp() # clear any buffered input preventing result page skip
                return wpm, errors, "Completed!"

    def show_menu(self):
        while True:
            self.stdscr.clear()
            self.stdscr.attron(curses.color_pair(3)) # UI Color
            
            self.stdscr.addstr("=== TYPING TEST IMPROVED ===\n")
            self.stdscr.addstr(f"1. Start Test\n")
            self.stdscr.addstr(f"2. Change Theme (Current: {self.current_theme})\n")
            self.stdscr.addstr(f"3. Change Cursor Color (Style {self.cursor_style_idx + 1}): ")
            self.stdscr.addstr(" C \n", curses.color_pair(4) | curses.A_REVERSE) # Preview
            self.stdscr.addstr(f"4. Set Time Limit (Current: {self.time_limit}s)\n")
            self.stdscr.addstr(f"5. Quit\n")
            
            self.stdscr.addstr("\nSelect an option: ")
            self.stdscr.attroff(curses.color_pair(3))
            self.stdscr.refresh()

            key = self.stdscr.getkey()
            
            if key == '1':
                wpm, errors, msg = self.run_test()
                self.stdscr.clear()
                self.stdscr.addstr(f"Game Over: {msg}\n", curses.color_pair(3))
                self.stdscr.addstr(f"Final WPM: {wpm}\n", curses.color_pair(1))
                self.stdscr.addstr(f"Errors: {errors}\n", curses.color_pair(2))
                self.stdscr.addstr("\nPress any key to return to menu...", curses.color_pair(3))
                self.stdscr.getkey()
                
            elif key == '2':
                # Cycle Themes
                themes = list(THEMES.keys())
                current_idx = themes.index(self.current_theme)
                self.current_theme = themes[(current_idx + 1) % len(themes)]
                self.load_theme()
            
            elif key == '3':
                # Cycle Cursor Styles
                self.cursor_style_idx = (self.cursor_style_idx + 1) % len(CURSOR_STYLES)
                self.load_theme() # Reload causes init_pair(4) to update
                
            elif key == '4':
                # Cycle Time Limits
                limits = [0, 15, 30, 60]
                try:
                    current_idx = limits.index(self.time_limit)
                    self.time_limit = limits[(current_idx + 1) % len(limits)]
                except ValueError:
                    self.time_limit = 60

            elif key == '5':
                break

def main(stdscr):
    app = TypingTest(stdscr)
    app.show_menu()

if __name__ == "__main__":
    wrapper(main)

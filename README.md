# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!# bookbot

# BookBot 📚

**BookBot** is a simple Python script that analyzes a book's text file and outputs useful statistics like word count and character frequency.

---

## 🔧 Requirements

- Python 3.x
- A `.txt` file containing the book (e.g., `frankenstein.txt`)

---

## 📂 Folder Structure

```
bookbot/
├── bookbot.py           # Main script
├── books/
│   └── frankenstein.txt # Sample book
```

---

## 🚀 How to Use

### Option 1: Run with a Hardcoded File Path

1. Open your terminal (or command prompt)
2. Navigate to the `bookbot` directory
3. Run the script:
```bash
python bookbot.py
```

---

### Option 2: Run with a Custom File Path

1. Open your terminal
2. Navigate to the `bookbot` folder
3. Run:
```bash
python bookbot.py books/frankenstein.txt
```

> You can replace the path with any `.txt` file you want to analyze.

---

## 📝 Output

The script will print:
- Total number of words
- Frequency of each character (sorted by most frequent)

---

## 🧪 Example Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
============= END ===============
```

---

## 🤝 License

MIT License – use and share freely!

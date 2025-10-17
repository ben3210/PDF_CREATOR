# 🧾 PDF Creator – Automated Homework Compilation Tool

This Python program automatically generates a well-formatted **PDF book** from multiple text-based files stored in a `tasks/` folder.  
It uses the **FPDF** library to combine all assignments into a single document with a professional header, logo, and footer.

---

## 🚀 Features

- Automatically scans the `tasks/` directory for files.  
- Accepts any text-based files — such as `.txt`, `.py`, `.c`, `.cpp`, `.java`, or others containing readable code or text.  
- No need to convert code to `.txt` — just drop your files directly in the folder.  
- Adds a custom header with a title and logo.  
- Includes a personalized footer with author details and page numbers.  
- Formats each file into its own PDF section with clean typography.  
- Outputs a single, ready-to-print PDF named **Book.pdf**.

---

## 🛠️ Requirements

- Python 3.x  
- [fpdf](https://pypi.org/project/fpdf/) library  

### Folder structure:
```
├── pdf_creator.py
├── tasks/
│   ├── assignment1.py
│   ├── homework2.cpp
│   ├── notes.txt
├── images/
│   └── logos.svg
```

---

## 💡 Usage

1. Place your code or text files inside the `tasks/` folder.  
2. Add your logo in the `images/` directory.  
3. Run:
   ```bash
   python pdf_creator.py
   ```
4. Find the generated **Book.pdf** in your project folder.

---

## 👨‍💻 Author

**Benjamin Irabisohoje** – Simple and elegant PDF automation using Python.

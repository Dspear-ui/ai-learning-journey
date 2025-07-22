## Week 1 Progress
## 📅 Day 1
-Cipher Building + Scientific Computing Foundations

### 🧠 Learning Focus
- Kicked off freeCodeCamp’s **Scientific Computing with Python** certification
- Started building encryption tools using custom Python functions

---

### 🔍 freeCodeCamp Highlights
- Reviewed basic syntax: variables, functions, lists, and string methods
- Practiced foundational logic with exercises like:
  - Reversing strings
  - Conditional blocks and loops
  - Using `.lower()`, `.find()`, and `.index()` correctly

**Key Takeaway:** `.index()` raises an error if the substring isn't found, while `.find()` returns `-1`. This affects encryption math and validation logic.

---

### 🔐 Vigenère Cipher Project
**Goal**: Encrypt and decrypt messages using a keyword with modular character shifting.

**Features:**
- `vigenere()` function accepts message, key, and direction (`1` or `-1`)
- Preserves spaces and non-letter characters using `.isalpha()`
- Direction-based logic allows for both encryption and decryption
- Used wrappers: `encrypt()` and `decrypt()` for cleaner API
- Final result:
  ```python
  Encrypted Text: 'mrttaqrhknsw ih puggrur'
  Key: 'happycoding'
  Decrypted Text: 'hello zaira'



– Card Number Validation + String & Math Logic
🧠 Learning Focus
- Implemented the Luhn Algorithm to verify card numbers
- Explored string manipulation and control flow with digit-level logic

🔍 Core Python Concepts Practiced
- Input sanitization using str.translate() to clean card format
- String slicing and reversing ([::-1]) to organize digit processing
- Loop-based logic to apply mathematical transformations
- Conditional math for splitting and summing two-digit numbers
Key Takeaway: The Luhn Algorithm adds odd-position digits directly, while even-position digits are doubled—if the result is ≥10, their digits are summed separately. The final total must be divisible by 10 to pass validation.

💳 Luhn Validator Project
Goal: Validate credit card numbers using digit manipulation and checksum logic
Features:
- verify_card_number() handles algorithm logic
- Handles non-digit formatting with .translate()
- Final check outputs 'VALID!' or 'INVALID!' using modulus test
- Clean function structure supports modular testing

Card Number: '4111-1111-4555-1142'
Output: VALID!


---

## 📅 Day 2 
– Expense Tracker CLI + Filter Logic & Input Validation

### 🧠 Learning Focus
- Built a **command-line expense tracker** using Python functions and control flow
- Practiced `map()`, `filter()`, and list manipulation for real-world data handling
- Explored input validation and user-friendly formatting for CLI apps

---

### 💻 Expense Tracker Project  
**Goal**: Track personal expenses with category filtering and total calculation via a menu-driven CLI.

**Features:**
- `add_expense()` stores amount and category in a list of dictionaries
- `print_expenses()` displays all entries with formatted output
- `total_expenses()` uses `map()` and `sum()` to calculate totals
- `filter_expenses_by_category()` returns category-matched expenses using `filter()` and `.lower()` for case-insensitive matching
- Menu loop supports adding, listing, filtering, and exiting

```python
Amount: 25.50, Category: Groceries
Total Expenses: 25.50
Expenses for Groceries:
 - $25.50 | Category: Groceries
```

**Key Takeaway:** `filter()` returns an iterator—convert to `list()` before reuse. Also, `.lower()` improves category matching across inconsistent user input.

---

### 🔍 Core Python Concepts Practiced
- Functional programming with `map()` and `filter()`
- Input validation using `try/except` for float conversion
- String formatting with `f-strings` and `.2f` for currency
- Case-insensitive comparisons for better UX
- Modular function design for clean CLI logic

---

### 🧠 Learning Focus  
- Practiced **string transformation and list comprehension** for code formatting tasks  
- Explored character-level logic to convert PascalCase and camelCase to snake_case  
- Refactored loop-based logic into a compact, readable one-liner using conditional expressions

---

### 💻 Snake Case Converter Project  
**Goal**: Convert PascalCase or camelCase strings into snake_case format for consistent variable naming.

**Features:**
- Iterates over each character in the input string
- Prepends an unde rscore to uppercase characters and converts them to lowercase
- Preserves lowercase characters and non-alphabetic symbols
- Uses list comprehension for clean, efficient transformation
- Strips leading underscores to match conventional snake_case formatting

```python
Input: 'IAmAPascalCasedString'
Output: 'i_am_a_pascal_cased_string'
```

**Key Takeaway:** Python strings don’t support `.prepend()`, but concatenation (`'_' + char`) achieves the same result. List comprehensions offer a concise alternative to traditional loops for character-level transformations.

---

### 🔍 Core Python Concepts Practiced  
- List comprehension with inline conditionals  
- String methods: `.isupper()`, `.lower()`, `.join()`, `.strip()`  
- Refactoring verbose loops into clean, functional expressions  
- Building reusable utility functions for code formatting and preprocessing


---

## 🧠 Learning Focus  
Practiced control flow and iterative logic using the bisection method to approximate square roots.  
Explored edge case handling, precision tuning, and mathematical reasoning in Python functions.

---

## 💻 Bisection Method for Square Root Approximation  
**Project Goal**: Approximate the square root of a non-negative number using the bisection method with a tolerance threshold.

**Features**:
- Handles invalid input (`square_target < 0`) with `raise ValueError`
- Returns exact results for `square_target == 0` and `square_target == 1`
- Uses midpoint logic: `mid = (low + high) / 2`
- Compares `square_mid = mid ** 2` to `square_target` and adjusts bounds
- Iterates up to `max_iterations` to converge on root
- Prints result or failure message based on convergence

**Key Takeaway**:  
Parentheses in `(low + high) / 2` are essential — without them, Python divides `high` first, skewing the midpoint.  
Also, `raise` is the correct way to signal invalid input, not `print()`.

---

## 🔍 Core Python Concepts Practiced  
- Exception handling with `raise ValueError(...)`  
- Control flow with multiple `if` and `elif` blocks  
- Iterative approximation using `for _ in range(max_iterations)`  
- Mathematical precision with `tolerance=1e-7`  
- Variable naming and debugging (`sqaure_target` typo broke logic silently)  
- Refactoring logic for clarity and modularity

---

## 📅 Days 3–4 – Arithmetic Formatter Refactor + Structure Mismatch Discovery  
🧠 **Learning Focus**  
Tackled freeCodeCamp’s *Arithmetic Formatter* project from the Scientific Computing with Python certification. Built a function that formats multiple arithmetic problems vertically and side-by-side with optional answer output and strict alignment rules.

🛠 **Design Approach**  
Originally broke the project into modular functions for clarity and scalability:
- `structure_problems()` handled width calculation and formatting
- `problem_solver()` computed answers only when `show_answers=True`
- All string alignment was built using `rjust()` and zipped width values
- Final output was assembled using a clean join strategy with line-specific strings

This design worked exactly as intended in VSCode—returning a correctly formatted multiline string.

🔍 **Challenge Encountered**  
Despite passing all manual tests, the freeCodeCamp validator rejected the submission. Traced the issue to a **structural mismatch**:  
> The platform expects all logic to run inside one function named `arithmetic_arranger()` and will not follow modular returns—even if the formatting and output are correct.

My original solution was returning the formatted string from a helper and routing through `arithmetic_arranger()`, but the test suite failed because it was expecting the string to be returned directly from the main function.

✅ **Resolution**  
Temporarily condensed all logic into a single function block inside `arithmetic_arranger()` for compatibility. The test passed instantly.

However, I’m keeping my original design in the repo because it’s:
- 🧩 More scalable and readable  
- 🧰 Easier to debug and extend  
- 🛠 Structured for real-world use—not just platform expectations

📌 **Key Takeaway**  
FreeCodeCamp's validator checks function structure, not just output. For platform compatibility, it’s important to match exactly what their test runner expects—even if it compromises best practice. My modular version is the clearer, more efficient implementation and will remain my preferred structure for future projects and portfolio review.

----

## 🧪 Day 5 – Secure Password Generator + Regex Validation Logic

🧠 **Learning Focus**  
Built a flexible password generator that enforces complexity requirements using Python’s `secrets` and `re` modules. Focused on cryptographic randomness, dynamic constraint validation, and efficient looping.

🔐 **Project Overview**  
**Goal**: Generate secure passwords with customizable character requirements.

**Core Features:**
- Function `generate_password()` accepts parameters for password length and character types:
  - `nums`, `special_chars`, `uppercase`, `lowercase`
- Uses `secrets.choice()` for cryptographic strength
- Validates password using regex patterns:
  - Digits: `\d`
  - Special characters: `[string.punctuation]`
  - Uppercase letters: `[A-Z]`
  - Lowercase letters: `[a-z]`
- Regenerates until all constraints are satisfied

🔍 **Key Takeaway**  
Regex validation (`re.findall()`) combined with a looped generator ensures constraints are reliably met without sacrificing randomness. `secrets` is the preferred module over `random` for secure operations.

💻 **Core Python Concepts Practiced**
- Dynamic string assembly with `secrets.choice()`
- Regex constraint enforcement using variable patterns and `fr''` syntax
- Control flow with `while True` and `break`
- Modular function design with scalable parameters

🧾 **Output Example**
```bash
Generated password: #A92fdxz!KvYT56c
```

---


  ### 📂 Files Added
- ▶️ Code Demo: [Vigenère Cipher – Day 1](../projects/vigenere_cipher.py)
- ▶️ Code Demo: [Luhn Algorithm – Day 1](../projects/Luhn_Algorithm.py)
- ▶️ Code Demo: [Expense_Tracker – Day 2](../projects/Expense_tracker.py)
- ▶️ Code Demo: [pascal_or_camel_cased_string – Day 2](../projects/pascal_or_camel_cased_string.py)
- ▶️ Code Demo: [bisection_method_for_square_root – Day 2](../projects/bisection_method_for_square_root.py)
- ▶️ Code Demo: [Vetical output – Day 3-4](../projects/Vetical_output.py)
-  ▶️ Code Demo: [Password Generator – Day 5(../projects/password_gen.py)

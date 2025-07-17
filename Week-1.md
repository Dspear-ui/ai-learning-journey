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
- Prepends an underscore to uppercase characters and converts them to lowercase
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



  ### 📂 Files Added
- ▶️ Code Demo: [Vigenère Cipher – Day 1](./vigenere_cipher.py)
- ▶️ Code Demo: [Luhn Algorithm – Day 1](./Luhn_Algorithm.py)
- ▶️ Code Demo: [Expense_Tracker – Day 2](./Expense_tracker.py)
- ▶️ Code Demo: [pascal_or_camel_cased_string – Day 2](./pascal_or_camel_cased_string.py)

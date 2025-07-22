## 📒 Week 1 Summary – Foundations in Python Logic, CLI Design & Regex Precision

You covered a wide range of Python fundamentals and real-world applications—from cryptographic tools to CLI utilities and validator functions. Each day built on the last, reinforcing your understanding of control flow, string manipulation, error handling, and modular design.

---

### 🗓️ Day 1 – Vigenère Cipher & Card Validator Logic

**🧠 Concepts Explored**
- **String manipulation & indexing**: `.lower()`, `.find()`, `.index()` differences
- **Modular function design** with multiple layers (`vigenere()`, `encrypt()`, `decrypt()`)
- **Character shifting and ASCII math** for encryption logic
- **Luhn Algorithm**: input sanitization, positional math, and checksum calculations

**🔍 Examples of Skills**
- Handling missing substrings with `.find()` vs raising exceptions with `.index()`
- Transforming card strings like `'4111-1111-4555-1142'` into digit-only format
- Understanding how even/odd digit positions impact final checksum validation

---

### 🗓️ Day 2 – Expense Tracker CLI + Case Transformation Utilities

**🧠 Concepts Explored**
- **Functional programming**: `map()`, `filter()` with lambda expressions
- **Case-insensitive string matching** using `.lower()` for CLI UX
- **List comprehensions** for compact transformations
- **String formatting** with `.2f` and f-strings

**🔍 Examples of Skills**
- Tracking grocery expenses like `{amount: 25.50, category: "Groceries"}`
- Converting `'PascalCaseString'` → `'pascal_case_string'` using conditional logic inside list comprehension
- Handling inconsistent user input by normalizing category comparisons

---

### 🗓️ Day 3–4 – Arithmetic Formatter Project (and Refactor Discovery)

**🧠 Concepts Explored**
- **String alignment and layout logic** with `.rjust()`
- **Modular structure vs monolithic function constraints** (especially on platforms like freeCodeCamp)
- **Zipping and assembling multiple aligned rows** for vertical formatting
- **Platform validator quirks** that ignore modular design even if output is correct

**🔍 Examples of Skills**
- Dynamically adjusting column widths for expressions like `"32 + 8"`
- Using `zip()` to combine rows like operands, operators, answers
- Refactoring the solution for both clean code and platform expectations (e.g., all logic inside `arithmetic_arranger()`)

---

### 🗓️ Day 5 – Password Generator with Regex Enforcement

**🧠 Concepts Explored**
- **Secure randomness** with `secrets.choice()` over `random.choice()`
- **Regex validation** for dynamic constraints (`\d`, `[A-Z]`, etc.)
- **Flexible parameterization** with default arguments
- **Loop-based verification** to regenerate until valid

**🔍 Examples of Skills**
- Generating a password like `#A92fdxz!KvYT56c` that satisfies:
  - ≥1 digit: `\d`
  - ≥1 symbol: `[string.punctuation]`
  - ≥1 uppercase: `[A-Z]`
  - ≥1 lowercase: `[a-z]`
- Dynamically building regex patterns using `fr''` to embed symbols safely

---

## 🧠 Key Growth Themes Across the Week

| Theme                        | How You Practiced It                          | Real-World Tie-In                                 |
|-----------------------------|-----------------------------------------------|---------------------------------------------------|
| Control flow & conditionals | `if`, `elif`, `for`, `while`, `break`         | Data validation, input filtering, logic branching |
| String & regex mechanics    | `.find()`, `re.findall()`, `.isupper()`       | Text processing, password security, UX cleanup    |
| Modular design thinking     | Wrapper functions, helper utilities           | Scalability, testability, readable code           |
| Debugging & testing mindset | Validator quirks, refactoring for clarity     | Production readiness, platform compatibility      |

---


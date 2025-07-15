## Week 1 Progress
## 📅 Day 1 – Cipher Building + Scientific Computing Foundations

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

  ### 📂 Files Added
- ▶️ Code Demo: [Vigenère Cipher – Day 1](./Vigenere_cipher.py)

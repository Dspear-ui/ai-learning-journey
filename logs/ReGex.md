## 🧠 Regex Essentials Cheat Sheet

### 🔤 Character Classes
| Pattern      | Meaning                             |
|--------------|-------------------------------------|
| `.`          | Any single character (except newline) |
| `[abc]`      | Matches a, b, or c                  |
| `[^abc]`     | Not a, b, or c                      |
| `[a-z]`      | Any lowercase letter                |
| `[A-Z]`      | Any uppercase letter                |
| `[0-9]`      | Any digit                           |
| `\d`         | Digit (`[0-9]`)                     |
| `\D`         | Not a digit                         |
| `\w`         | Alphanumeric + `_` (`[a-zA-Z0-9_]`) |
| `\W`         | Not alphanumeric                    |
| `\s`         | Whitespace (space, tab, newline)    |
| `\S`         | Non-whitespace                      |

---

### 🔁 Quantifiers
| Pattern      | Meaning                             |
|--------------|-------------------------------------|
| `*`          | 0 or more                           |
| `+`          | 1 or more                           |
| `?`          | 0 or 1                              |
| `{n}`        | Exactly n times                     |
| `{n,}`       | n or more times                     |
| `{n,m}`      | Between n and m times               |

---

### 🎯 Anchors & Boundaries
| Pattern      | Meaning                             |
|--------------|-------------------------------------|
| `^`          | Start of string                     |
| `$`          | End of string                       |
| `\b`         | Word boundary                       |
| `\B`         | Not a word boundary                 |

---

### 🧩 Groups & Alternation
| Pattern      | Meaning                             |
|--------------|-------------------------------------|
| `(abc)`      | Grouping: matches "abc"             |
| `(?:abc)`    | Non-capturing group                 |
| `a|b`        | Alternation: matches a or b         |
| `(?P<name>...)` | Named group (Python only)       |

---

### ⚙️ Escaping Special Characters
To match symbols like `.` or `*`, escape them: `\.` or `\*`

---

## 🧪 Common Patterns

| Task                      | Regex Example         |
|---------------------------|-----------------------|
| Match email               | `\b[\w.-]+@[\w.-]+\.\w{2,4}\b` |
| Match phone number        | `\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}` |
| Match hexadecimal color   | `#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})` |
| Match date (YYYY-MM-DD)   | `\d{4}-\d{2}-\d{2}`   |
| Match alphanumeric string | `^[a-zA-Z0-9]+$`      |

<div align="center">
<pre>
██████   ██    ████  ██████ ██   ██ ██████ ██   ██  ████  ██████ ██  ██ ██   ██   ██   ██   ██   ██    ████  ██████ ██   ██ ██████ ██   ██ ██████ 
██  ██  ████  ██     ██     ███ ███ ██     ███ ███ ██  ██ ██  ██  ████  ███ ███  ████  ███  ██  ████  ██     ██     ███ ███ ██     ███  ██   ██   
██████ ██  ██ ██ ███ ████   ██ █ ██ ████   ██ █ ██ ██  ██ ██████   ██   ██ █ ██ ██  ██ ██ █ ██ ██  ██ ██ ███ ████   ██ █ ██ ████   ██ █ ██   ██   
██     ██████ ██  ██ ██     ██   ██ ██     ██   ██ ██  ██ ██ ██    ██   ██   ██ ██████ ██  ███ ██████ ██  ██ ██     ██   ██ ██     ██  ███   ██   
██     ██  ██  ████  ██████ ██   ██ ██████ ██   ██  ████  ██  ██   ██   ██   ██ ██  ██ ██   ██ ██  ██  ████  ██████ ██   ██ ██████ ██   ██   ██   
</pre>
</div>
## 📍 Overview

**LRU Cache Simulation**

This project simulates the **Least Recently Used (LRU)** page replacement algorithm, which is used to manage memory in computers. The program shows how pages are loaded into a cache, evicted when space runs out, and tracks page faults.

### Features:
- Simulates a LRU page replacement algorithm.
- Displays the state of memory (page frames) after each page reference.
- Tracks page faults (when a page is not found in memory and needs to be loaded).

### How It Works:
- A cache with a fixed capacity is created.
- Pages are added to the cache as they are requested.
- If the cache is full, the least recently used page is removed.
- The program keeps track of which pages are in memory and when page faults happen.

### Usage:
1. Run the program.
2. Enter a sequence of page numbers (0-9).
3. The program will display the memory state and page faults.

---

## 📁 Project Structure

```sh
└── PageMemoryManagement/
    └── main.py
```
---

### ⚙️ Installation

Install PageMemoryManagement using one of the following methods:

**Build from source:**

1. Clone the PageMemoryManagement repository:
```sh
❯ git clone https://github.com/DCyfa/PageMemoryManagement
```

2. Navigate to the project directory:
```sh
❯ cd PageMemoryManagement
```

### 🤖 Usage
Run PageMemoryManagement using the following command:
main.py



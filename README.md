# 🚀 SmartTest Sentinel

## 📌 Overview

SmartTest Sentinel is an intelligent API testing system built in Python that combines **API validation, log analysis, and performance testing**.
It is designed to simulate real-world SDET workflows by not only testing APIs but also analyzing failures and system behavior under load.

---

## 🧪 Key Features

* 🔌 API Testing using Python `requests`
* 🧠 Log Analyzer for root cause detection
* ⚡ Performance Testing using Python threading
* 🧪 Test automation using PyTest
* 📊 Configurable test execution via `pytest.ini`

---

## 🛠 Tech Stack

* Python
* PyTest
* Requests

---

## 📁 Project Structure

```
smarttest-sentinel/
│
├── api/                # API client functions
├── analyzer/           # Log analysis module
├── tests/              # Test cases (API + analyzer)
├── performance/        # Load testing scripts
├── logs/               # Sample log files
│
├── pytest.ini          # PyTest configuration
├── README.md
```

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run all tests

```
pytest -s
```

---

## ⚡ Performance Testing

The project simulates concurrent users using Python threading:

* Multiple threads act as users
* Each thread sends multiple API requests
* Measures total execution time

### Sample Output

```
Status: 200
Status: 200
...
Total time: 5.89 seconds
```

---

## 🧠 Log Analyzer

The log analyzer module:

* Parses error logs
* Detects patterns (timeout, 500 errors, connection issues)
* Suggests possible root causes

### Example

```
Input: ERROR: Database connection timeout
Output: Possible cause: Slow response or network latency
```

---

## 🎯 Use Cases

* API validation and testing
* Debugging production issues using logs
* Basic load/performance testing
* Backend system validation

---

## 📈 Future Enhancements

* Integration with CI/CD (Jenkins / GitHub Actions)
* Advanced performance metrics (latency, throughput)
* AI-based failure prediction
* Dashboard for log visualization

---

## 👨‍💻 Author

Srishti Jaiswal

---

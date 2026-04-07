# ICMP Network Diagnostic Tool

## 📌 Overview

This project implements a secure client-server based network diagnostic system using ICMP tools like **ping** and **traceroute**.

## ⚙️ Features

* Secure communication using SSL/TLS
* Remote network diagnostics
* Ping (connectivity check)
* Traceroute (path analysis)

## 🧠 Technologies Used

* Python
* Socket Programming
* SSL/TLS
* Subprocess module

## ▶️ How to Run

### 1. Start Server

```bash
python server.py
```

### 2. Run Client

```bash
python client.py
```

### 3. Enter Host

Example:

```
google.com
```

## 📊 Output

* Ping results (RTT, packets)
* Traceroute path

## ⚠️ Note

* Works on Windows (uses ping -n and tracert)
* SSL certificate required (cert.pem, key.pem)

## 👩‍💻 Author

Mini Project Submission

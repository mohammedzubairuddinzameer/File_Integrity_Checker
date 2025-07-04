# File_Integrity_Checker

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: MOHAMMED ZUBAIR UDDIN ZAMEER

*INTERN ID*: CITSOD850

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

##DESCRIPTION
The **File Integrity Checker** is a Python-based application developed to monitor and ensure the integrity of files by computing and comparing their cryptographic hash values. File integrity is a crucial aspect of data security, ensuring that files have not been tampered with, altered, or corrupted either intentionally or accidentally. This tool leverages the **SHA-256 hashing algorithm** provided by Python's built-in `hashlib` module, which produces a unique fixed-size string for each file, acting like a digital fingerprint. Even a minor change in the file content will result in a completely different hash value, making it an effective way to detect changes.

The program begins by automatically generating two sample files: `test1.txt` and `data/file2.csv`. These files are created with predefined content to allow users to test the integrity checker immediately without needing to supply their own files. The script then calculates the SHA-256 hash values of these files and stores them in a local JSON file called `hash_store.json`. This file acts as a reference point and keeps track of the current state of the monitored files. When the script is executed again, it recalculates the hash values of the files and compares them with the values stored in the JSON file. If the current hash matches the stored hash, the file is reported as "unchanged." If the hash is different, the tool reports the file as "modified," and if a file appears that wasn’t previously recorded, it is marked as "newly added."

This system ensures that any unauthorized or unexpected changes to the files are promptly detected. It is especially useful in scenarios where the integrity of configuration files, system logs, or sensitive data must be maintained. For example, system administrators can use this tool to monitor important system files, ensuring they haven't been altered by malware or unauthorized users. Similarly, developers and data analysts can use it to verify the integrity of scripts, data files, or backup contents.

The tool uses several core Python modules, such as `hashlib` for hashing, `os` for file and directory handling, and `json` for storing and retrieving hash values in a structured format. By maintaining simplicity and relying only on standard libraries, the tool is lightweight, cross-platform, and easy to deploy or integrate into larger systems. It provides console-based output that clearly indicates the status of each monitored file, whether unchanged, modified, or new.

In summary, the File Integrity Checker is a practical and educational tool that demonstrates the use of cryptographic hash functions for real-world file monitoring. It automates the process of file hash calculation, comparison, and change detection, providing users with a reliable way to verify file authenticity. Its simple design, combined with effective functionality, makes it suitable for anyone from beginners learning about cybersecurity concepts to professionals seeking a quick solution for file integrity verification. This task highlights the importance of file validation and showcases how Python can be effectively used to implement security-oriented utilities.

##OUTPUT

![Screenshot 2025-07-04 170009](https://github.com/user-attachments/assets/f7bd2e0d-c1e1-412a-afcb-2285a00a716d)

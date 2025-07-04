import hashlib
import os
import json

# File to store the original hash values
HASH_STORE_FILE = "hash_store.json"

def create_sample_files():
    """Create sample files for integrity checking if they don't exist."""
    os.makedirs("data", exist_ok=True)

    if not os.path.exists("test1.txt"):
        with open("test1.txt", "w") as f:
            f.write("This is a test file for integrity checking.\n")
            f.write("It contains some example text.\n")
            f.write("File: test1.txt\n")
        print("[INFO] Created sample file: test1.txt")

    if not os.path.exists("data/file2.csv"):
        with open("data/file2.csv", "w") as f:
            f.write("id,name,score\n")
            f.write("1,Alice,85\n")
            f.write("2,Bob,90\n")
            f.write("3,jhon,78\n")
        print("[INFO] Created sample file: data/file2.csv")

def calculate_hash(file_path):
    """Calculate SHA-256 hash of the given file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None

def load_hash_store():
    """Load previously stored hash values from JSON file."""
    if os.path.exists(HASH_STORE_FILE):
        with open(HASH_STORE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hash_store(hash_data):
    """Save current hash values to JSON file."""
    with open(HASH_STORE_FILE, "w") as f:
        json.dump(hash_data, f, indent=4)

def check_integrity(files):
    """Check integrity of given list of files."""
    hash_store = load_hash_store()
    updated_store = {}

    for file_path in files:
        current_hash = calculate_hash(file_path)
        if current_hash is None:
            continue

        updated_store[file_path] = current_hash

        if file_path in hash_store:
            if hash_store[file_path] == current_hash:
                print(f"[OK] No change in {file_path}")
            else:
                print(f"[ALERT] File modified: {file_path}")
        else:
            print(f"[INFO] New file added to monitoring: {file_path}")

    # Update hash store after check
    save_hash_store(updated_store)

if __name__ == "__main__":
    print("=== FILE INTEGRITY CHECKER ===")
    
    # Step 1: Create sample files if not already present
    create_sample_files()
    
    # Step 2: Files to check
    files_to_check = ["test1.txt", "data/file2.csv"]
    
    # Step 3: Perform integrity check
    check_integrity(files_to_check)

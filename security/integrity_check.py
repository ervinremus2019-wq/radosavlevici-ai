# System Integrity Check
# © 2026 Ervin Remus Radosavlevici

import hashlib
from core.identity.author_metadata import verify_author


def check_integrity(file_path, metadata):
    verify_author(metadata)
    # Calculate file hash
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    # Compare with known good hash
    return file_hash == "KNOWN_GOOD_HASH"


# Example usage
if __name__ == "__main__":
    metadata = {"AUTHOR_NAME": "Ervin Remus Radosavlevici"}
    is_intact = check_integrity("core/identity/author_metadata.py", metadata)
    print(f"System intact: {is_intact}")
"""
Example usage showing how to integrate `security.secrets_loader.load_roberto_memory` into existing codepaths.
Replace any direct file reads of `roberto_permanent_memory.json` with this loader call.
"""
from security.secrets_loader import load_roberto_memory


def get_memory_summary():
    mem = load_roberto_memory()
    if not mem:
        return {"error":"No memory loaded"}
    # Example: return some safe fields only
    return {
        "creator": mem.get('creator', '<unknown>'),
        "core_identity": {
            "full_name": '<REDACTED>' if mem.get('core_identity', {}).get('full_name') else None
        }
    }


if __name__ == '__main__':
    print(get_memory_summary())

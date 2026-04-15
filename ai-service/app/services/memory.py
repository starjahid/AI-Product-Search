import json
import os

MEMORY_FILE = "data/memory_store.json"


def load_memory():
    # create file if not exists
    if not os.path.exists(MEMORY_FILE):
        return {}

    try:
        with open(MEMORY_FILE, "r") as f:
            content = f.read().strip()

            # empty file fix
            if not content:
                return {}

            return json.loads(content)

    except:
        return {}


def save_memory(memory):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def get_cached_product(key: str):
    memory = load_memory()
    return memory.get(key)


def set_cached_product(key: str, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)
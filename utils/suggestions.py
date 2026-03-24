# utils/suggestions.py

import os

def get_suggestion(file_path, platform):
    size_kb = os.path.getsize(file_path) / 1024

    if platform == "instagram":
        return 1080, 70, "Best for Instagram (1080x1080)"
    elif platform == "whatsapp":
        return 800, 60, "Best for WhatsApp sharing"

    # General suggestion
    if size_kb > 3000:
        return 800, 60, "High compression recommended"
    elif size_kb > 1000:
        return 1000, 75, "Medium compression recommended"
    else:
        return 1200, 85, "Low compression (high quality)"
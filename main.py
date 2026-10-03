import html
import json
import re


def json_to_highlighted_html(json_text: str) -> str:
    """Convert JSON text into syntax-highlighted HTML for a <pre> block."""
    data = json.loads(json_text)
    output = html.escape(json.dumps(data, indent=2, ensure_ascii=False), quote=False)

    # JSON object keys
    output = re.sub(
        r'(?m)^(\s*)("(?:(?:\\.)|[^"\\])*")(?=\s*:)',
        r'\1<span class="k">\2</span>',
        output,
    )

    # String values
    output = re.sub(
        r'(:\s*)("(?:(?:\\.)|[^"\\])*")',
        r'\1<span class="s">\2</span>',
        output,
    )

    # Boolean and null values
    output = re.sub(
        r'(:\s*)(true|false|null)(?=\s*[,}\]])',
        r'\1<span class="b">\2</span>',
        output,
    )

    # Numeric values
    output = re.sub(
        r'(:\s*)(-?\d+(?:\.\d+)?)(?=\s*[,}\]])',
        r'\1<span class="n">\2</span>',
        output,
    )

    return f"<pre>{output}</pre>"


# Example: paste valid JSON here
json_input = """
[
  {
    "Address": "Delhi",
    "Age": "30-40",
    "Gender": "MALE",
    "MaskedMobile": "######2995",
    "Status": "461641615604 Exists"
  }
]
"""

print(json_to_highlighted_html(json_input))
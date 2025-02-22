import re

def extract_sections(text):
    sections = {}
    
    # Define section headers and their corresponding regex patterns
    headers = ["Introduction:", "Storyline:", "Climax:", "Moral:"]
    
    for i in range(len(headers)):
        start = headers[i]
        end = headers[i + 1] if i + 1 < len(headers) else None
        
        if end:
            pattern = f"{start}(.*?){end}"  # Non-greedy match between headers
        else:
            pattern = f"{start}(.*)"  # Capture till the end for the last section
        
        match = re.search(pattern, text, re.DOTALL)
        if match:
            sections[start.strip(":").lower()] = match.group(1).strip()
    
    return sections
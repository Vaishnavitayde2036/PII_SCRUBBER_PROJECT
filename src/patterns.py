# src/patterns.py

PII_PATTERNS = {
    # 1. Contact Info
    "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "PHONE": r"\b(?:\+?61|0) ?[2-478](?:[ -]?[0-9]){8}\b",
    
    # 2. Dates & IDs 
    "DOB": r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",      
    "APPT_ID": r"\b[A-Z]{3,}-\d{5,}\b",               
    
    # 3. ADDRESS 
    "ADDRESS": r"\b\d{1,5}\s[\w\s\.]+(?:Rd|St|Ave|Blvd|Lane|Dr|Way|Road|Street)(?:,\s[\w\s]+(?:VIC|NSW|QLD|WA|SA|TAS|ACT|NT)\s\d{4})?\b"
}
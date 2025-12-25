import re

class PIIScrubber:
    def __init__(self):
        # We define regex patterns for sensitive data
        self.patterns = {
            "EMAIL": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            "PHONE": r'(?:\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}|(?:\+?61[\s-]?|04|02|03|07|08)\d{2,4}[\s-]?\d{3,4}[\s-]?\d{0,3})',
            "DOB": r'(?:DOB|Date of Birth)[:\s]*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',          
            "REF_ID": r'(?:Ref ID|Invoice|Booking|BKG|INV)[\s:-]*([A-Z0-9-]+)',
            "NAME_CONTEXT": r'((?:Dr\.?|Patient|Partner|Name)[:]?\s+(?:[A-Z]\.?\s*)?[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)',
            "PROVIDER": r'([A-Z][\w\’\']+(?:\s+[A-Z][\w\’\']+)*\s+(?:Clinic|Hospital|Labs?|Fertility|Pathology|Centre|Center|IVF))',
            "ADDRESS": r'((?:(?:Flat|Apt|Unit)\s+[A-Z0-9]+[,\s]+)?\d+\s+[A-Z][a-z]+\s+(?:Rd|Road|St|Street|Ln|Lane|Ave|Avenue|Dr|Drive)[, a-zA-Z0-9\s]+)',
            "MEDICARE": r'(?:Medicare(?: number)?[:\s]*)(\d{4}\s\d{5}\s\d)',
            "SSN": r'(\b\d{3}-\d{2}-\d{4}\b)',
            "INSURANCE_ID": r'(?:Insurance policy ID|Policy ID|Member ID)[\s:-]*([A-Z0-9-]+)',
            "GOV_ID": r'(\b\d{4}\s\d{4}\s\d{4}\b)',
            "URL": r'(https?://\S+)'
        }

    def scrub(self, text):
        detected_spans = []
        
        # 1. Find matches
        for pii_type, pattern in self.patterns.items():
            for match in re.finditer(pattern, text):
                if match.lastindex:
                    start, end = match.span(1)
                    actual_type = "NAME" if "NAME" in pii_type else pii_type
                else:
                    start, end = match.span()
                    actual_type = pii_type

                detected_spans.append({
                    "type": actual_type,
                    "start": start,
                    "end": end
                })

        # 2. Sort spans by start position to handle overlaps
        detected_spans.sort(key=lambda x: x['start'])
        
        # 3. Resolve Overlaps 
        cleaned_spans = []
        if detected_spans:
            curr = detected_spans[0]
            for next_span in detected_spans[1:]:
                if next_span['start'] < curr['end']:
                    continue # Skip overlapping span
                else:
                    cleaned_spans.append(curr)
                    curr = next_span
            cleaned_spans.append(curr)

        # 4. Replace text (Working backwards to keep indices valid)
        scrubbed_text_list = list(text)
        types_found = set()
        
        for span in reversed(cleaned_spans):
            t = span['type']
            types_found.add(t)
            replacement = f"[{t}]"
            # Replace the slice of text with the placeholder
            scrubbed_text_list[span['start']:span['end']] = replacement
            
        return {
            "scrubbed_text": "".join(scrubbed_text_list),
            "detected_spans": cleaned_spans,
            "types_found": list(types_found)
        }
import argparse
import json
import sys
import os

from src.scrubber import PIIScrubber 

def main():
    parser = argparse.ArgumentParser(description="Ashwam PII Scrubber")
    parser.add_argument("--input", required=True, help="Path to input .jsonl file")
    parser.add_argument("--output", required=True, help="Path to output .jsonl file")
    args = parser.parse_args()

    
    if os.path.abspath(args.input) == os.path.abspath(args.output):
        print("Error: Input and Output files cannot be the same. This would erase your data!")
        sys.exit(1)

    scrubber = PIIScrubber()
    
    try:
        with open(args.input, 'r', encoding='utf-8') as infile, \
             open(args.output, 'w', encoding='utf-8') as outfile:
            
            count = 0
            for line in infile:
                if not line.strip(): continue
                data = json.loads(line)
                
                # Process
                result = scrubber.scrub(data['text'])
                
                # Format Output
                output_record = {
                    "entry_id": data['entry_id'],
                    "scrubbed_text": result['scrubbed_text'],
                    "detected_spans": result['detected_spans'],
                    "types_found": result['types_found'],
                    "scrubber_version": "v1.0"
                }
                
                
                outfile.write(json.dumps(output_record, ensure_ascii=False) + "\n")
                count += 1
                
                json.dumps(output_record, ensure_ascii=False)
                count += 1
                
        print(f"Success! Scrubbed {count} entries. Output saved to {args.output}")

    except FileNotFoundError:
        print(f"Error: File {args.input} not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
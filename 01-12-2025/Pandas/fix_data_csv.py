"""
Fixes malformed CSV where fields are split across lines (broken line breaks inside fields) by
reassembling lines until a complete record (with expected comma count) is formed. Saves a fixed CSV.
"""
import csv
from pathlib import Path

input_file = Path(__file__).parent / 'data.csv'
backup_file = Path(__file__).parent / 'data_raw_backup.csv'
output_file = Path(__file__).parent / 'data_fixed.csv'

EXPECTED_COMMAS = 10  # header + 10 commas mean 11 columns

# Read entire file contents
raw_content = input_file.read_text(encoding='utf-8')

# create a backup copy
backup_file.write_text(raw_content, encoding='utf-8')
print(f"Backup saved to: {backup_file}")

lines = [ln.rstrip('\n') for ln in raw_content.splitlines() if ln.strip() != '']

cleaned_rows = []
buffer = ''
for ln in lines:
    if buffer:
        buffer += ' ' + ln.strip()
    else:
        buffer = ln.strip()

    # Count commas - if we reached the expected commas, treat buffer as a full row
    if buffer.count(',') >= EXPECTED_COMMAS:
        # Fix common broken tokens (like 'Credit Card' split as 'Credit Card' with added spaces)
        # Already joined with spaces; remove double spaces
        row = buffer.replace('\t', ' ').replace('  ', ' ')
        # Optionally fix weird spaces around commas
        parts = [p.strip() for p in row.split(',')]
        cleaned_rows.append(parts)
        buffer = ''

if buffer:
    print('Warning: leftover buffer when parsing. Appending as last row.')
    cleaned_rows.append([p.strip() for p in buffer.split(',')])

# Write to output CSV using csv module to ensure proper quoting
# Normalize header if it looks malformed
if cleaned_rows:
    header = cleaned_rows[0]
    # Fix header broken token 'Pay mentMethod' if present
    header = [h.replace('Pay mentMethod', 'PaymentMethod') for h in header]
    cleaned_rows[0] = header

with output_file.open('w', encoding='utf-8', newline='') as fout:
    writer = csv.writer(fout)
    for parts in cleaned_rows:
        writer.writerow(parts)

print(f"Converted {len(cleaned_rows)} rows to {output_file}")

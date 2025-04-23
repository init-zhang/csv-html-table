import re

# `(?<!\\),` negative look behind to ignore `\,`.
comma_pattern = re.compile(r"(?<!\\),")
# Use a lazy quantifer for content between table tags.
# Avoids issues with multple tables in text.
table_pattern = re.compile(r"^<table>\n(.*?)\n</table>$", re.MULTILINE | re.DOTALL)

def table_replacement(match):
    """
    Replacement function used in `csv_to_table` to replace csv into HTML.
    
    Replaces escaped commas with commas.
    Ignores empty rows.
    First row is `<th>`, unless there's only 1 row, otherwise it's `<td>`.
    """ 
    
    csv = match.group(1).strip()

    if not csv:
        return ""

    # Process csv, split into rows, and then split via comma delimator.
    # Ignore empty rows.
    rows = [[e.strip().replace(r"\,", ",") for e in comma_pattern.split(row)]
            for row in csv.split("\n") if row.strip()]

    if len(rows) == 1:
        return f"<table><tr><td>{'</td><td>'.join(rows[0])}</td></tr></table>"

    table_rows = []
    table_rows.append(f"<tr><th>{'</th><th>'.join(rows[0])}</th></tr>")

    for row in rows[1:]:
        table_rows.append(f"<tr><td>{'</td><td>'.join(row)}</td></tr>")
    
    return f"<table>{''.join(table_rows)}</table>"

def csv_to_table(text):
    """
    Converts CSV data within `<table></table` into HTML table rows.
    
    Opening and closing table tags must be on their own lines.
    Uses commas as a delimator, use `\,` to escape commas.
    Strips slashs from escaped commas and ignores empty lines.
    Creates a header row when csv has multple rows.
    """
    return table_pattern.sub(table_replacement, text)

# CSV HTML Table

CSV to HTML table converter

I love Markdown but its tables use a lot of characters and takes time to make. I wanted something that still looks like a structured table but takes a fraction of the time to write.

To fix this issue, I wrote a CSV to HTML table converter that can convert CSV within my Markdown files into HTML tables.

## Features

- Commas are used as the delimiter, to include a literal comma within a cell, use a backslash to escape it `\,`
  - Escaped commas `\,` are converted back into normal commas
- There can be any number of leading or trailing spaces around the commas, it's all trimmed during conversion
- Empty lines between the rows are ignored
- First row uses table header `<th>` tags, unless the CSV only has 1 row, otherwise it uses table data `<td>` tags
- Supports multiple CSV tables within the same text

## Usage

Wrap your CSV data with `<table>` and `</table>` tags on their own lines:

```
<table>
Col 1  , Col 2
Cell 1 , Cell 2
</table>
```

And call the `csv_to_table` function from the library with the string containing the CSV:

```py
from csv_to_table import csv_to_table

output = csv_to_table(text)
# "<table><tr><th>Col 1</th><th>Col 2</th></tr><tr><td>Cell 1</td><td>Cell 2</td></tr></table>"
```

## Examples

```
<table>
Name      , Age , Location       
Alice     , 30  , New York       
Bob       , 25  , Los Angeles    
Charlie   , 35  , San Francisco
</table>
```

<table><tr><th>Name</th><th>Age</th><th>Location</th></tr><tr><td>Alice</td><td>30</td><td>New York</td></tr><tr><td>Bob</td><td>25</td><td>Los Angeles</td></tr><tr><td>Charlie</td><td>35</td><td>San Francisco</td></tr></table>

```
<table>
Product    , Price , Stock  

Laptop     , 999   , 10     
Smartphone , 499   , 25
</table>  
```

<table><tr><th>Product</th><th>Price</th><th>Stock</th></tr><tr><td>Laptop</td><td>999</td><td>10</td></tr><tr><td>Smartphone</td><td>499</td><td>25</td></tr></table>

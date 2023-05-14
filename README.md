# PWP7000
Python serial encoder to talk to PWP7000LT Daisy Wheel Printer

The printer can do most ASCII printable characters, but it repurposes these ASCII characters as follows:
{ -> é
} -> ¼
\ -> ¿
| -> ½
< -> ¢
> -> ç

The daisy wheel also has ¶ and § (my favorite typographic mark), but I haven't tried to see what byte it corresponds to.

Right now, "1/2" and "1/4" are converted to ½ and ¼ respectively. I may add the functionality to pass the above allowable unicode characters, but right now it will directly send the bytes for non-ascii characters which will cause unexpected results.

The program automatically adds line breaks and prompts the user to change to a new sheet of paper after 55 lines. At the end of the document, the form feed character is sent and the printer ejects the last sheet of paper.

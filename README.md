# PWP7000
Python serial encoder to talk to PWP7000LT Daisy Wheel Printer

<p>The printer can do most ASCII printable characters, but it repurposes these ASCII characters as follows:</p>
<p>{ -> é</p>
<p>} -> ¼</p>
<p>\ -> ¿</p>
<p>| -> ½</p>
<p>< -> ¢</p>
<p>> -> ç</p>

<p>The daisy wheel also has ¶ and § (my favorite typographic mark), but I haven't tried to see what byte it corresponds to.

<p>Right now, "1/2" and "1/4" are converted to ½ and ¼ respectively. I may add the functionality to pass the above allowable unicode characters, but right now it will directly send the bytes for non-ascii characters which will cause unexpected results.

<p>The program automatically adds line breaks and prompts the user to change to a new sheet of paper after 55 lines. At the end of the document, the form feed character is sent and the printer ejects the last sheet of paper.

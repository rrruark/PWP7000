# PWP7000
<p>Python serial encoder to talk to PWP7000LT Daisy Wheel Printer. The intion of this code is to serve as a working reference for interfacing with this printer. Its not intended to be used as a complete general purpose driver, but it handles most plain text alright.</p>

<p>The program automatically adds line breaks and prompts the user to change to a new sheet of paper after 55 lines. At the end of the document, the form feed character is sent and the printer ejects the last sheet of paper.</p>

<p>The printer can do most ASCII printable characters, but it repurposes these ASCII characters as follows:</p>
<p>{ -> é</p>
<p>} -> ¼</p>
<p>\ -> ¿</p>
<p>| -> ½</p>
<p>< -> ¢</p>
<p>> -> ç</p>

<p>It also repurposes two control characters for two additional printable characters:</p>
<p>0x1E [RS] -> ¶</p>
<p>0x1F [US] -> §</p>

<p>The example code converts "1/2" and "1/4" to ½ and ¼ respectively. The code passes unicode bytes directly which results in unexpected results when those unicode bytes are non-ASCII, however.</p>

<p>The character spacing of the printer can also be adjusted with ASCII control characters. 0x0F [SI] reduces character spacing and 0x12 [TAPE] returns it to standard monospacing. In the reduced character spacing mode, spaces are still normal width. I don't include this in the example code since I haven't tested it out: I discovered this while using a microcontroller to print to the printer directly for a different project. </p>

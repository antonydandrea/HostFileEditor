Host File Editor README

--------------------------------------------------------------------------------
0 - Contents
--------------------------------------------------------------------------------
1 - Version
2 - Licensing
3 - Brief Introduction
4 - Features/Change Log
5 - How To Use
6 - Contact 
--------------------------------------------------------------------------------
1 - Version
--------------------------------------------------------------------------------
README file version: 1.0.0
Date: 21/02/2013
Ianus version: 0.2
Date: 21/03/2013

--------------------------------------------------------------------------------
2 - Licensing
--------------------------------------------------------------------------------
Copyright (c) 2012 Antony D'Andrea

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in the 
Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the 
following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software and the README.txt file.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
--------------------------------------------------------------------------------
3 - Brief Introduction
--------------------------------------------------------------------------------
I was fed up of constantly going through the process of opening the host file and editing
with vi.
At the same time, I wanted to learn Python.
So I made this script. It still has a lot of useful things missing but it is a step in 
the right direction.
At the moment it is only compatible with Ubuntu (I have only tested on 12.04.1), this is something
I want to extend to Windows in the future.
You must still run the script with elevated privalidges too, this is something I want to incorparate
into the script.
Because it is so incomplete, I haven't called it version 1 just yet.

--------------------------------------------------------------------------------
4 - Features/Change Log
--------------------------------------------------------------------------------
- Add new entries to the host file.
- If an entry with the domain name already exists, it will overide the existing IP address.

--------------------------------------------------------------------------------
5 - How To Use
--------------------------------------------------------------------------------
- You must have Python already installed onto your machine.
- Download HostFileEditor.py and store it somewhere.
- Simply run sudo python /path/to/HostFileEditor.py
--The sudo is necassary for editing the hosts file.
--------------------------------------------------------------------------------
6 - Contact
--------------------------------------------------------------------------------
Email: contactme@antonydandrea.com
Twitter: @antonydandrea1

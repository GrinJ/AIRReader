=========
AIRReader
=========

About
=====
Simple python class that allows to read and convert data from AIR files.
Created with the support of Hydrometcentre of Russia.

**License**: GNU GPL version 3.

**Requirements**: Python 2 or 3 with re module


Usage
=====

**AIRReader(filename)**
    To create the object o the class

**convertData()**
    To convert all available variables from AIR TEMPMAKT specification format to normal format

**isNull([values], num)**
    To check the validity of all parameters passed in tuple for index num

Or create a symbolic link

`ln -s /projectsDir/AIRReader/src/SYNReader/AIRReader.py projectsDir/newProj/`
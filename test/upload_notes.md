# Online docs

https://twine.readthedocs.io/en/latest/

More documentation on using Twine to upload packages to PyPI is in the 
Python Packaging User Guide:

    https://packaging.python.org/tutorials/packaging-projects/


<br/>
<br/>
<br/>

# Commands

```
twine upload dist/*

```

Twine will prompt for your username and password.


Like many other command line tools, Twine does not show any characters 
when you enter your password


<br/>

## Note:

If you’re using Windows and trying to paste your username, password, or 
token in the Command Prompt or PowerShell, Ctrl-V and Shift+Insert won’t 
work

Instead, you can use “Edit > Paste” from the window menu, or enable :
“Use Ctrl+Shift+C/V as Copy/Paste” in “Properties” 

This is a known issue with Python’s getpass module

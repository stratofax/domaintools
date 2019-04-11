# domaintools #

Python scripts to check, monitor, and analyze domains and subdomains.

## About domaintools ##

Python script(s) to

* Check IP addresses, domain registration, nameservers, zone records
* Version 0.2 - Alpha code shared to public on GitHub 
* Version 0.1 - created on April 9, 2019

### How do I get set up? ###

* Use pipenv to set up depencies
* Configuration: python3
* Requires: socket (standard library), click, whois
* How to run tests: just do it!
* Deployment instructions

### Contribution guidelines ###

* Tests: if you find a bug, let me know and I'll fix it and write a test
* Code review: please contact me if you have comments or suggestions.
* Other guidelines: currently, 

### Who do I contact? ###

* Neil Johnson: neil@cadent.com

## Known Issues

### domaincheck.py

A list of features to add and bugs to fix

This script does **not**:

* Check to see if the hostname you passed is a legitmate hostname. TODO: add Regex testing to filter out badly formed hostnames.
* Handle an error if the hostname IP address isn't found by a DNS query. TODO: test to see if you can look up an IP address, stop if not available.
* Handle all the possible date formats that may be returned from a whois query. TODO: convert date formats to strings.


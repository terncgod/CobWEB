# CobWEB
## CobWEB Email OSINT Tool

CobWEB is a Email and information gathering tool which searches for leaks in databases and websites (IP, Hosts, etc.) to find Email information as well as IP Addresses and other information using search engines like (google, pgp key servers, shodan) to find as much information about a particular target as possible. This is a very simple tool with lots of capability in mind...

**Installation**

```
git clone https://github.com/Cr7pt0nic/CobWEB.git
cd CobWEB
sudo python setup.py install
sudo python cobweb.py --help
```
**Usage**

```
sudo python cobweb.py --domain roblox.com -s --breach-check -v 3
```
```
sudo python cobweb.py --osint example@admin.com --breach-check -v 3
```

# Security Toolbox

Most familiar tools I've used or recommend based on context

## Web Proxy

1. Burpsuite Pro (requires work email; $500)
2. Zap (Free!)

## Fingerprinting

1. Wappalyzer (Chrome extension) ```a pretty good web-based app for learning about a website's tech stack```
2. Whatweb <https://www.kali.org/tools/whatweb/> - ``` root@kali:~# whatweb -v -a 3 [target IP]```
3. nmap scan - ```nmap -sC -oA -p 22,80, 443 script_scan <target_ip>```
4. mxtoolbox - <https://mxtoolbox.com/> - ```DNS and reverse DNS lookup```

## Phishing

1. use anonymous mail - <https://anonymousemail.me/>

## Reconnaissance

1. nmap + host files
2. When you have a large IP range: masscan - <https://www.kali.org/tools/masscan/> ```masscan -p22,80,445 [target ip]```
3. recon-ng (associated modules) ```recon-ng -w name``` creates a workspace, then you add domains, finally import modules and run them
4. Banner grab with netcat - ```nc -nv <target> <port>```
5. Search Engine(s) to use - Shodan
6. Subfinder - <https://www.kali.org/tools/subfinder/> ```subfinder -h```
7. amass - <https://www.kali.org/tools/amass/> ```amass -h```
8. dig - <https://www.geeksforgeeks.org/dig-command-in-linux-with-examples/>
9. Sublist3r - <https://www.kali.org/tools/sublist3r/> ```sublist3r -d [target] -t 3 -e [search engine]```

## Mapping

1. gobuster - <https://www.kali.org/tools/gobuster/> ```gobuster dir -u <target> -w /usr/share/dirb/wordlists/common.txt```
2. dirbuster - <https://www.kali.org/tools/dirbuster/> ```dirbuster -h```
3. Ffuf - ```ffuf -h```
4. wfuzz - ```wfuzz -c -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404 target/FUZZ```
5. DNSDumpster - <https://dnsdumpster.com/>

## Discovery

1. eyewitness - <https://www.kali.org/tools/eyewitness/> - ```eyewitness --delay 15 -filename <file> --results```
2. gowitness - <https://www.kali.org/tools/gowitness/> - ```gowitness -h```

## Exploit/VULNS

1. Payload all the things - <https://github.com/swisskyrepo/PayloadsAllTheThings>
2. Get sensitive data w. trufflehog - <https://www.kali.org/tools/trufflehog/> ```snifftest --help```
3. ExploitDB - <https://www.kali.org/tools/exploitdb/> ```exploitdb -h```
4. Metasploit

## CVEs

1. Searchsploit - <https://www.exploit-db.com/searchsploit>
2. CVE.org - <https://cve.org>

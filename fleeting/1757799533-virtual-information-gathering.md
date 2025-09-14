---
id: 1757799533-virtual-information-gathering
aliases:
  - virtual information gathering
tags:
  - cyber security
---

# virtual information gathering

## Commands grimoire

### ping

```bash
ping google.com
```

The response is something like this:

```
PING google.com (142.251.133.14) 56(84) bytes of data.
64 bytes from pngrua-bv-in-f14.1e100.net (142.251.133.14): icmp_seq=1 ttl=118 time=77.7 ms
64 bytes from pngrua-bv-in-f14.1e100.net (142.251.133.14): icmp_seq=2 ttl=118 time=76.5 ms
64 bytes from pngrua-bv-in-f14.1e100.net (142.251.133.14): icmp_seq=3 ttl=118 time=79.8 ms
64 bytes from pngrua-bv-in-f14.1e100.net (142.251.133.14): icmp_seq=4 ttl=118 time=74.9 ms
64 bytes from pngrua-bv-in-f14.1e100.net (142.251.133.14): icmp_seq=5 ttl=118 time=77.6 ms
^C
--- google.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4004ms
rtt min/avg/max/mdev = 74.904/77.298/79.819/1.611 ms
```

### nslookup

```bash
nslookup archlinux.org
```

The response is something like this:

```
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
Name:   archlinux.org
Address: 95.217.163.246
Name:   archlinux.org
Address: 2a01:4f9:c010:6b1f::1
```

### whois

```bash
whois archlinux.org
```

It can generate the following response:

```
Domain Name: archlinux.org
Registry Domain ID: REDACTED
Registrar WHOIS Server: http://whois.antagus.de
Registrar URL: http://www.vautron.de
Updated Date: 2025-04-19T04:32:46Z
Creation Date: 2002-03-05T04:32:27Z
Registry Expiry Date: 2026-03-05T04:32:27Z
Registrar: Vautron Rechenzentrum AG
Registrar IANA ID: 1443
Registrar Abuse Contact Email: abuse@vautron.de
Registrar Abuse Contact Phone: +49.9415990570
Domain Status: ok https://icann.org/epp#ok
Registry Registrant ID: REDACTED
Registrant Name: REDACTED
Registrant Organization: Software in the Public Interest Inc. - Arch Linux Project
Registrant Street: REDACTED
Registrant City: REDACTED
Registrant State/Province: US
Registrant Postal Code: REDACTED
Registrant Country: US
Registrant Phone: REDACTED
Registrant Phone Ext: REDACTED
Registrant Fax: REDACTED
Registrant Fax Ext: REDACTED
Registrant Email: REDACTED
Registry Admin ID: REDACTED
Admin Name: REDACTED
Admin Organization: REDACTED
Admin Street: REDACTED
Admin City: REDACTED
Admin State/Province: REDACTED
Admin Postal Code: REDACTED
Admin Country: REDACTED
Admin Phone: REDACTED
Admin Phone Ext: REDACTED
Admin Fax: REDACTED
Admin Fax Ext: REDACTED
Admin Email: REDACTED
Registry Tech ID: REDACTED
Tech Name: REDACTED
Tech Organization: REDACTED
Tech Street: REDACTED
Tech City: REDACTED
Tech State/Province: REDACTED
Tech Postal Code: REDACTED
Tech Country: REDACTED
Tech Phone: REDACTED
Tech Phone Ext: REDACTED
Tech Fax: REDACTED
Tech Fax Ext: REDACTED
Tech Email: REDACTED
Name Server: helium.ns.hetzner.de
Name Server: hydrogen.ns.hetzner.com
Name Server: oxygen.ns.hetzner.com
DNSSEC: unsigned
URL of the ICANN Whois Inaccuracy Complaint Form: https://icann.org/wicf/
>>> Last update of WHOIS database: 2025-09-13T22:21:43Z <<<

For more information on Whois status codes, please visit https://icann.org/epp

Terms of Use: Access to Public Interest Registry WHOIS information is provided to assist persons in determining the contents of a domain name registration record in the Public Interest Registry registry database. The data in this record is provided by Public Interest Registry for informational purposes only, and Public Interest Registry does not guarantee its accuracy. This service is intended only for query-based access. You agree that you will use this data only for lawful purposes and that, under no circumstances will you use this data to (a) allow, enable, or otherwise support the transmission by e-mail, telephone, or facsimile of mass unsolicited, commercial advertising or solicitations to entities other than the data recipient's own existing customers; or (b) enable high volume, automated, electronic processes that send queries or data to the systems of Registry Operator, a Registrar, or Identity Digital except as reasonably necessary to register domain names or modify existing registrations. All rights reserved. Public Interest Registry reserves the right to modify these terms at any time. By submitting this query, you agree to abide by this policy.  The Registrar of Record identified in this output may have an RDDS service that can be queried for additional information on how to contact the Registrant, Admin, or Tech contact of the queried domain name.
```

### whatweb

```bash
whatweb archlinux.org
whatweb -v archlinux.org
whatweb 192.168.1.1-192.168.1.255
whatweb 192.168.1.1-192.168.1.255 --aggression 3 -v --no-errors
```

The result could be something like this:

```
http://archlinux.org [301 Moved Permanently] Country[UKRAINE][UA], HTTPServer[nginx], IP[95.217.163.246], RedirectLocation[https://archlinux.org/], Title[301 Moved Permanently], nginx
https://archlinux.org/ [200 OK] Country[UKRAINE][UA], Email[aaron@archlinux.org,anthraxx@archlinux.org,arch-general@lists.archlinux.org,jvinet@zeroflux.org], HTML5, HTTPServer[nginx], IP[95.217.163.246], OpenSearch[/opensearch/packages/], Script[application/ld+json,text/javascript], Strict-Transport-Security[max-age=31536000; includeSubdomains; preload], Title[Arch Linux], UncommonHeaders[x-content-type-options,referrer-policy,cross-origin-opener-policy,alt-svc,x-cache-status], X-Frame-Options[DENY], nginx
```

### theharvester

```bash
theHarvester -d archlinux.org -b all
```

No good result was acquired. Some api keys are necessary for the tool. Another tool that was recommended was [`hunter.io`](https://hunter.io).

In github there are good tools as well. You can search for `information gathering tool github` and there you can check the options.

---
tags: Linux, Networking, DNS
---

# Local DNS Plus Cache


## Flushing the Cache on Linux

Any of the following might work.

```bash
# Saw this one, doesn't work for Ubuntu
sudo /etc/init.d/networking restart

# NCSD
sudo /etc/init.d/nscd restart
service nscd restart

# Systemd Resolve
sudo systemd-resolve --flush-caches
sudo systemctl restart systemd-resolved
```

## Cache Flush Example

```bash
sudo systemd-resolve --flush-caches
sudo systemd-resolve --statistics
# DNSSEC supported by current servers: no
#
# Transactions               
# Current Transactions: 0    
#  Total Transactions: 26574
#                           
# Cache                      
#  Current Cache Size: 4    
#          Cache Hits: 15666
#        Cache Misses: 11009
#                           
# DNSSEC Verdicts            
#              Secure: 0    
#            Insecure: 0    
#               Bogus: 0    
#       Indeterminate: 0    
sudo systemctl restart systemd-resolved
sudo systemd-resolve --statistics
# DNSSEC supported by current servers: no
# 
# Transactions            
# Current Transactions: 0 
#   Total Transactions: 18
#                         
# Cache                   
#   Current Cache Size: 2 
#           Cache Hits: 7 
#         Cache Misses: 11
#                         
# DNSSEC Verdicts         
#               Secure: 0 
#             Insecure: 0 
#                Bogus: 0 
#        Indeterminate: 0 
```

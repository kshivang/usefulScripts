#!/bin/bash
if ifconfig | grep addr:172.20.181.223 
then
    sudo ifconfig eth0 172.24.9.223 netmask 255.255.248.0
    sudo route delete default
    sudo route add default 172.24.15.254 
else 
    sudo ifconfig eth0 172.20.181.223 netmask 255.255.252.0
    sudo route delete default
    sudo route add default 172.20.183.254 
fi

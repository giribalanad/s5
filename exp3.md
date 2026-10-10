## Experiment 3: Configure Routers and Switches

### Algorithm

1. Open Cisco Packet Tracer and create a topology with a router, switches, PCs, and a cloud.
2. Connect the devices using appropriate cables.
3. Assign IP addresses to router interfaces and PCs.
4. Configure router interfaces using `no shutdown`.
5. Configure DHCP or static IP addresses for PCs.
6. Configure routing, VLANs, and NAT if required.
7. Test connectivity using `ping`.
8. Stop.

### Router Configuration (Short)

```
enable
configure terminal
interface FastEthernet0/0
ip address 192.168.10.1 255.255.255.0
no shutdown
exit
end
```

### Output

```
PC> ping 192.168.10.1

Reply from 192.168.10.1: bytes=32 time<1ms
Reply from 192.168.10.1: bytes=32 time<1ms

Packets: Sent = 2, Received = 2, Lost = 0
```

Result: Router and switch configuration was completed, and network connectivity was verified using ping.&#x20;

22AI502 - Computer Networks - Lab Manual.pdf

## Experiment 1 — Design LAN for 5 Laboratories

### Algorithm

1. Open Cisco Packet Tracer.
2. Place 1 router, 5 switches, and PCs for each laboratory.
3. Connect each lab's PCs to its switch.
4. Connect each switch to the router.
5. Assign a unique IP subnet to each laboratory.
6. Configure router subinterfaces using VLANs and `encapsulation dot1Q`.
7. Configure switch trunk ports and access VLANs.
8. Test inter-lab connectivity using `ping`.

### Router Configuration (Cisco CLI)

```
enable
configure terminal

interface FastEthernet0/0
no shutdown
exit

interface FastEthernet0/0.10
encapsulation dot1Q 10
ip address 192.168.1.1 255.255.255.0
exit

interface FastEthernet0/0.20
encapsulation dot1Q 20
ip address 192.168.2.1 255.255.255.0
exit

interface FastEthernet0/0.30
encapsulation dot1Q 30
ip address 192.168.3.1 255.255.255.0
exit

interface FastEthernet0/0.40
encapsulation dot1Q 40
ip address 192.168.4.1 255.255.255.0
exit

interface FastEthernet0/0.50
encapsulation dot1Q 50
ip address 192.168.5.1 255.255.255.0
exit

end
write memory
```

### Sample IP Addressing

| Laboratory | Network        | Router gateway |
| ---------- | -------------- | -------------- |
| Lab 1      | 192.168.1.0/24 | 192.168.1.1    |
| Lab 2      | 192.168.2.0/24 | 192.168.2.1    |
| Lab 3      | 192.168.3.0/24 | 192.168.3.1    |
| Lab 4      | 192.168.4.0/24 | 192.168.4.1    |
| Lab 5      | 192.168.5.0/24 | 192.168.5.1    |

Configure each switch's router-facing port as a trunk and assign the PC-facing ports to their respective VLANs.

### Sample Output

```
PC1> ping 192.168.3.10

Reply from 192.168.3.10: bytes=32 time<1ms
Reply from 192.168.3.10: bytes=32 time<1ms

Packets: Sent = 2, Received = 2, Lost = 0
```

Result: A LAN connecting five laboratories was designed and inter-lab communication was verified using Cisco Packet Tracer.&#x20;

22AI502 - Computer Networks - Lab Manual.pdf

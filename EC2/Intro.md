# Elastic Compute Cloud (EC2) Basics

- **EC2** = a virtual server that you rent in AWS.  
- You only **pay for what you use**.  
- In AWS, each virtual server is called an **Instance**.  

---

## Steps to Create an EC2 Instance (via AWS Management Console)

1. **Open Console** → Navigate to **Services > Compute > EC2**  
2. Click **Launch Instance**  
3. **Choose Amazon Machine Image (AMI)**  
   - Examples: Linux, macOS, Windows  
4. **Choose Instance Type**  
   - Defines CPU, memory, performance (e.g., `t2.micro` for free tier)  
5. **Configure Instance Details**  
   - Number of instances, networking (VPC, subnet), IAM role  
6. **Add Storage**  
   - Configure root volume size and type  
7. **Add Tags**  
   - Example: `Key = environment`, `Value = dev`  
8. **Configure Security Group**  
   - Works like a firewall  
   - Example: allow **RDP (3389)** for Windows or **SSH (22)** for Linux  
9. **Review and Launch**  
   - Double-check all configuration details  
   - Click **Launch**  
10. **Create / Select Key Pair**  
    - Create a new key pair (e.g., `my-key.pem`) or use an existing one  
    - Download and keep it safe (needed to connect to instance)  

---

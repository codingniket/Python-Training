# Comparison Cloud File

Cloud platforms like AWS, Azure, and GCP offer similar service models but with different naming, ecosystem depth, and tooling. This document compares IaaS, PaaS, SaaS, storage, and shows how to create a VM on all three in three high-level steps.

---

## Service Models Overview

IaaS (Infrastructure as a Service) provides core compute, storage, and networking resources where the user manages OS and above.

PaaS (Platform as a Service) provides a managed runtime and application platform abstracting OS, scaling, and much of the infrastructure.

SaaS (Software as a Service) delivers complete applications over the internet that users consume without managing infrastructure or runtimes.

---

## AWS, Azure, GCP: IaaS, PaaS, SaaS Examples

### IaaS

- **AWS**: EC2 (compute), EBS (block storage), VPC (networking)
- **Azure**: Virtual Machines, Managed Disks, Virtual Network
- **GCP**: Compute Engine, Persistent Disk, VPC Network

### PaaS

- **AWS**: Elastic Beanstalk, AWS Fargate (containers), RDS, Lambda (serverless)
- **Azure**: App Service, Azure Functions, Azure SQL Database, AKS
- **GCP**: App Engine, Cloud Run, Cloud SQL, Cloud Functions

### SaaS

- **AWS**: Amazon WorkDocs, Amazon Chime, Amazon Connect (SaaS-like services)
- **Azure**: Microsoft 365 (Office 365), Dynamics 365, Power BI Service
- **GCP**: Google Workspace (Gmail, Docs, Sheets), Google Meet, BigQuery BI features

---

## Storage Services Comparison

### AWS Storage

- **Amazon S3**: Object storage for unstructured data, backups, static websites.
- **Amazon EBS**: Block storage volumes attached to EC2 instances.
- **Amazon EFS**: Managed NFS file system for Linux workloads.
- **Glacier / S3 Glacier**: Archival, low-cost, infrequently accessed data.

### Azure Storage

- **Blob Storage**: Object storage for unstructured data.
- **Azure Disk Storage**: Managed block storage disks for VMs.
- **Azure Files**: SMB file shares hosted in Azure.
- **Azure Archive Storage**: Low-cost archival tier for rarely accessed data.

### GCP Storage

- **Cloud Storage**: Object storage with multiple classes (Standard, Nearline, Coldline, Archive).
- **Persistent Disk**: Block storage for Compute Engine VMs.
- **Filestore**: Managed NFS file storage for applications needing shared file systems.

---

## IaaS vs PaaS vs SaaS Behavior Across Cloud Providers

| Aspect              | IaaS (EC2/VMs/Compute Engine)                                 | PaaS (App Service/App Engine/etc.)                                           | SaaS (M365/Workspace/etc.)                       |
|---------------------|---------------------------------------------------------------|-------------------------------------------------------------------------------|--------------------------------------------------|
| Control level       | High (OS, runtime, patches, scaling logic)                    | Medium (code and config; platform handles OS, scaling)                        | Low (use app; no infra control)                  |
| Responsibility      | You manage OS, middleware, app, security hardening           | You manage app and some config; provider manages platform and scaling         | Provider manages everything                      |
| Use cases           | Legacy apps, custom infra, fine-grained control              | Web APIs, microservices, standard web workloads, event-driven apps           | Email, collaboration, CRM, analytics             |
| Flexibility         | Maximum flexibility, more complexity                         | Balanced flexibility and simplicity                                          | Minimal flexibility, maximum simplicity          |

---

## Three-Step VM Creation: AWS, Azure, GCP

Below is a simplified 3-step, console-based flow for creating a VM on each provider. In reality, each step contains several sub-options, but this gives the conceptual process.

---

### Create a VM on AWS (EC2)

**Step 1: Launch and Choose Basics**

- In AWS Management Console, go to **EC2** and click **Launch instance**.  
- Enter an instance name, select an **AMI** (e.g., Amazon Linux, Ubuntu, Windows) and pick an instance type (e.g., t3.micro).

**Step 2: Configure Networking, Storage, and Access**

- Choose a **VPC** and subnet, decide if public IP is needed, and configure security group (inbound rules like SSH 22 or RDP 3389).  
- Configure storage (EBS volume size/type) and select or create a **key pair** for SSH/RDP access.

**Step 3: Review and Launch**

- Review all settings, confirm that security group and key pair are correct, then click **Launch instance**.  
- After the instance state becomes “running”, use the public IP/DNS with your key pair (or password for Windows) to connect.

---

### Create a VM on Azure (Virtual Machine)

**Step 1: Start VM Creation**

- In Azure Portal, click **Create a resource** → **Virtual machine**.  
- Under the **Basics** tab, choose subscription, resource group, VM name, region, availability options, and image (Ubuntu, Windows, etc.), and select a VM size.

**Step 2: Configure Authentication, Disks, and Networking**

- Choose authentication type (SSH public key or password) and provide username and credentials.  
- Configure OS disk type and, if needed, add data disks; choose virtual network, subnet, public IP, and NSG rules (e.g., SSH/RDP).

**Step 3: Review + Create and Connect**

- Click **Review + create**, let Azure validate settings, then click **Create**.  
- When deployment completes, go to the VM’s overview page and connect via SSH/RDP using the given IP or DNS.

---

### Create a VM on GCP (Compute Engine)

**Step 1: Open Compute Engine and Start Instance**

- In Google Cloud Console, go to **Compute Engine** → **VM instances** and click **Create instance**.  
- Specify instance name, region, and zone.

**Step 2: Configure Machine Type, Image, Disk, and Network**

- Select a machine family and type (e.g., e2-micro, n2-standard) and choose a boot disk image (Debian, Ubuntu, Windows, custom).  
- Configure boot disk size/type and network (VPC network, subnetwork), and decide if external IP is needed; set firewall flags (allow HTTP/HTTPS if required).

**Step 3: Create and Access Instance**

- Click **Create** to provision the VM.  
- Once status is “RUNNING”, connect via browser-based SSH (for Linux) or RDP (for Windows) using the external IP/DNS.

---

## Conceptual 3-Step Process (All Clouds)

Conceptually, VM creation across all three providers follows the same pattern:

1. **Define basics**  
   - Choose region, instance/VM name, OS image, and size/flavor (CPU/RAM).

2. **Configure infra bindings**  
   - Attach storage (disks), configure network (VPC/VNet, subnet, IP), define firewall/security group/NSG rules, set credentials (SSH key/password).

3. **Provision and connect**  
   - Review configuration, create the instance, wait until it is running, then connect using SSH or RDP from your local machine or browser.

---

## When to Use IaaS vs PaaS vs SaaS in Practice

- Use **IaaS** when you need full OS control, custom networking, or must lift-and-shift legacy apps.  
- Use **PaaS** when you want to deploy code fast with minimal infra management, auto-scaling, and integrated DevOps.  
- Use **SaaS** when your goal is business functionality (email, CRM, collaboration, analytics) without running any infrastructure.

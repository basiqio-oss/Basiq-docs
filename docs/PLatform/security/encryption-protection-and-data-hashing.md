---
title: Encryption
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
# Data encryption

At Basiq we secure CDR data in transit and at rest by encrypting file systems, end-user devices, portable storage media and backup media. Cryptographic keys are securely stored, backed-up and retained.

Basiq transmits data over public networks using strong encryption, using an SSL/TLS secure tunnel to transfer data, and then stored using 256-bit AES encryption. 

We support the latest recommended secure cipher suites to encrypt all traffic in transit, including 

* The use of TLS 1.2 protocols 
* AES-256 encryption, and 
* SHA2 signatures, as supported by the clients. 

We are constantly monitoring the cryptographic landscape to adapt and upgrade cipher suite choices. This ensures we are consistently aligned with the industry standard while still maintaining our compatibility with older clients. 

Data at rest in our production network is encrypted using FIPS 140-2 compliant encryption standards. This applies to all types of data at rest within our systems—object and relational databases, file stores, database backups, etc. Encryption keys are stored in a secure server on a segregated network with very limited access using Amazon’s Key Management Service.

Each customer’s data is hosted on Basiq’s shared infrastructure and segregated logically by the Basiq application, and we use a combination of storage technologies to ensure customer data is protected from hardware failures and returns quickly when requested.

# Data protection

All of the data that is stored at rest is encrypted using AES-256 bit encryption, using the envelope-encryption technique, ensuring each record is encrypted with a unique key - and inherently means that the data is protected two-fold. Our keys are stored within Amazons KMS (Key Management Service) which are restricted and can never leave.

 

<Image width="80%" src="https://files.readme.io/73ba07e-Group_2062_1.png" />

 

As an additional level of precaution, Basiq uses advanced techniques to detect credit card numbers within our data set and apply data-scrubbing which ensures that only the last 4 digits are persisted to the database. All other parts of the credit card number are permanently removed and never stored within our system.

# Data hashing algorithm

Our hashed-data storage scheme relies on three different layers of cryptographic protections. For ease of elucidation, in the figure and below we omit any mention of binary encoding (base64). We rely on bcrypt as our core hashing algorithm with a per-user salt and an encryption key (or global pepper), stored separately. Our approach differs from basic bcrypt in a few significant ways.

 

<div align="center">
<img height="350" src="https://files.readme.io/4bbbecb-Group_2063.png" align="center"/>
</div >

 

### **1.** The plaintext data is transformed into a hash value using SHA512.

This addresses two particular issues with bcrypt. Some implementations of bcrypt truncate the input to 72 bytes, which reduces the entropy of the data. Other implementations don’t truncate the input and are therefore vulnerable to DoS attacks due to allowing the input of arbitrarily long passwords. By applying SHA, we can quickly convert  long data into a fixed length 512 bit value, solving both problems.

### **2.** This SHA512 hash is hashed again using bcrypt with a cost of 10, and a unique, per-user salt.

Unlike cryptographic hash functions like SHA, bcrypt is designed to be slow and hard to speed up via custom hardware and GPUs. A work factor of 10 translates into roughly 100ms for all these steps on our servers.

### **3.** The resulting bcrypt hash is encrypted with AES256 using a secret key, referred to as "pepper".

The pepper is a defense in depth measure. The pepper value is stored separately in a manner that makes it difficult to discover by an attacker (i.e. not in a database table). As a result, if only the data storage is compromised, the data hashes are encrypted and of no use to an attacker.

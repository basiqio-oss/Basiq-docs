---
title: Banking
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
Because of the way webhooks work, attackers can impersonate services by simply sending a fake webhook to an endpoint. Think about it: it's just an HTTP POST from an unknown source. This is a potential security hole for many applications, or at the very least, a source of problems.

This guide details best practices to make sure your webhooks remain secure and function well for your integration with BASIQ.

# Signatures:

Webhooks signature verification is recommended to reduce spoofing and replay attacks. BASIQ utilises `HMAC-SHA256` as the signature scheme for signing and verifying webhooks. Under this scheme BASIQ signs both the payload and additional metadata such as ID and timestamp. 

BASIQ signs every webhook and its metadata with a unique key for each endpoint. This signature can then be used to verify the webhook message indeed comes from BASIQ.

Another potential security hole is what's called replay attacks. A replay attack is when an attacker intercepts a valid payload (including the signature), and re-transmits it to your endpoint. 

To mitigate this attack, BASIQ includes a timestamp for when the webhook attempt occurred. Our libraries automatically reject webhooks with a timestamp that are more than five minutes away (past or future) from the current time. This requires your server's clock to be synchronised and accurate, and it's recommended that you use [NTP](https://en.wikipedia.org/wiki/Network_Time_Protocol) to achieve this.

## Verifying signatures

Each webhook call contains three headers that provide additional information for verification purposes:

**webhook-id:** This header contains a unique identifier for the webhook message. The identifier remains the same if the same webhook is resent, such as in the case of a previous failure.

**webhook-timestamp:** This header indicates the timestamp of the webhook message in [seconds since the epoch](https://en.wikipedia.org/wiki/Unix_time).

**webhook-signature:** This header contains a [Base64](https://en.wikipedia.org/wiki/Base64) encoded list of signatures, separated by spaces.


## Constructing the signed content

The content to sign is composed by concatenating the `id`, `timestamp` and `payload`, separated by the full-stop character (.). In code, it will look something like:
[block:code]
{
  "codes": [
    {
      "code": "signedContent = `${webhook_id}.${webhook_timestamp}.${payload}`",
      "language": "javascript",
      "name": "signedContent"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "danger",
  "body": "Where body is the raw body of the request. The signature is sensitive to any changes, so even a small change in the body will cause the signature to be completely different. This means that you should not change the body in any way before verifying."
}
[/block]
## Determining the expected signature

BASIQ uses [HMAC](https://en.wikipedia.org/wiki/HMAC) with [SHA-256](https://en.wikipedia.org/wiki/SHA-2) to sign its webhooks.

To calculate the expected signature, you need to HMAC the signedContent from above using the base64 portion of your signing secret. The signing secret is the part after the `whsec_` prefix. 

**For example**, if your secret is `whsec_MA4V6bD7rB0Hcm2aw8ghgDeQ5UAak24DwnX0rX6`, you should use `MA4V6bD7rB0Hcm2aw8ghgDeQ5UAak24DwnX0rX6` as the key.

Here's an example of how you can calculate the signature in Node.js:
[block:code]
{
  "codes": [
    {
      "code": "const crypto = require('crypto');\n\nsignedContent = `${webhook_id}.${webhook_timestamp}.${payload}`\nconst secret = \"whsec_MA4V6bD7rB0Hcm2aw8ghgDeQ5UAak24DwnX0rX6\";\n\n// Need to base64 decode the secret\nconst secretBytes = new Buffer(secret.split('_')[1], \"base64\");\nconst signature = crypto\n  .createHmac('sha256', secretBytes)\n  .update(signedContent)\n  .digest('base64');\nconsole.log(signature);\n\nif (signature !== webhook_signature) {\n// don't proceed further\n}",
      "language": "javascript",
      "name": "Code"
    }
  ]
}
[/block]
The generated signature should match one of the signatures sent in the `webhook-signature` header.

The `webhook-signature` header is composed of a list of space delimited signatures and their corresponding version identifiers. The signature list is most commonly of length one. Though there could be any number of signatures. **For example:** 
[block:code]
{
  "codes": [
    {
      "code": "v1,AvFmwEcSZu/WBDciXDcwDaSdA61PJNI2uup6nihXJfE=",
      "language": "json",
      "name": "webhook-signature header"
    }
  ]
}
[/block]
Make sure to remove the version prefix and delimiter (e.g. v1,) before verifying the signature.

## Verify timestamp

As mentioned above, BASIQ also sends the timestamp of the attempt in the `webhook-timestamp` header. You should compare this timestamp against your system timestamp and make sure it's within your tolerance in order to prevent timestamp and replay attacks.


# Firewalls (Source IP Addresses)

Many larger organisations implement stringent firewall rules to control the IPs that can send traffic to their systems. Although this alone may not provide robust security, it can be valuable when combined with other measures like webhook signatures. To accommodate such organisations and meet their requirements, BASIQ ensures that webhooks requests are sent exclusively from a predefined set of IPs.

In case your webhook receiving endpoint is behind a firewall or NAT, you may need to allow traffic from BASIQ's IP addresses.

Here is the complete list of IP addresses of the sender from which webhooks may originate:
[block:code]
{
  "codes": [
    {
      "code": "44.228.126.217\n50.112.21.217\n52.24.126.164\n54.148.139.208\n52.215.16.239\n54.216.8.72\n63.33.109.123\n13.126.41.108\n15.207.218.84\n65.2.133.31",
      "language": "text",
      "name": "Source IP addresses"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "success",
  "title": "Quick Links",
  "body": "  * [Create a Webhook](https://api.basiq.io/reference/addwebhook) \n  * [Retrieve a Webhook](https://api.basiq.io/reference/getwebhook)\n  * [Send a test message](https://api.basiq.io/reference/testmessage) "
}
[/block]
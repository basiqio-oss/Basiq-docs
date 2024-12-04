---
title: Delivery Schedule and Retries
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# Introduction:

In the world of web development and API integrations, webhook failures are an occasional reality. Despite our best efforts, "stuff happens," and webhooks may fail to deliver their intended payloads. But fear not! This guide is here to equip you with the necessary details to gracefully handle these failures and ensure the seamless operation of your integrations.

This guide provides detailed information about what constitutes a webhook message delivery failure, retry schedules and more.

# Webhook Message Delivery Failures:

In the context of webhook integrations, a message delivery failure refers to the inability to successfully deliver a webhook payload to its intended recipient. In our system, we consider any HTTP response status outside the 2xx range as a failure, indicating that the delivery was unsuccessful. These failures could occur due to various reasons, such as network issues, server errors, or unavailability of the recipient system. Recognising and appropriately handling these failures is essential to ensure the reliability and accuracy of data flow between systems. 

# Delivery Schedule:

Each webhook message follows a specific delivery schedule, which includes multiple attempts at different time intervals using an exponential backoff strategy. This means that each subsequent attempt is made at progressively increasing time intervals. This approach allows for a reasonable delay between attempts while avoiding overwhelming the endpoint or network with frequent retries. The schedule is as follows:

**Immediately:** The first attempt to deliver the webhook message is made immediately after it is generated.

**5 seconds:** If the first attempt fails, a second attempt is made after a 5-second interval.

**5 minutes:** If the second attempt fails, a third attempt is scheduled after a 5-minute interval.

**30 minutes:** If the third attempt fails, a fourth attempt is scheduled after a 30-minute interval.

**2 hours:** If the fourth attempt fails, a fifth attempt is scheduled after a 2-hour interval.

**5 hours:** If the fifth attempt fails, a sixth attempt is scheduled after a 5-hour interval.

**10 hours:** If the sixth attempt fails, a seventh attempt is scheduled after a 10-hour interval.

**10 hours (in addition to the previous)**: If the seventh attempt fails, an eighth and final attempt is made after another 10-hour interval. 

**For example,** let's consider a scenario where a webhook message fails to be delivered three times before eventually succeeding. The delivery timeline for this scenario would be approximately 35 minutes and 5 seconds following the first attempt. This delay allows for potential temporary issues to be resolved and ensures a higher chance of successful delivery.

# Navigating Webhook Failures in the Endgame and Beyond:

After all retry attempts have been exhausted, the webhook endpoint will be subject to removal or disabling, depending on the specific circumstances. This ensures that continuous unsuccessful delivery attempts do not persist indefinitely.
[block:callout]
{
  "type": "info",
  "body": "**Note:** Once an endpoint is removed or its delivery is disabled, further delivery attempts to that endpoint will be automatically disabled as well. This ensures that no additional delivery attempts will be made after the endpoint has been intentionally removed or disabled.",
  "title": ""
}
[/block]
# Conclusion:

Basiq's webhook delivery system employs a reliable retry schedule with exponential backoff to maximize the chances of successful message delivery. By following this schedule, we aim to provide a robust integration experience and minimize any potential disruptions in the flow of data between Basiq and your applications.

In case of any issues, please contact our support channels.
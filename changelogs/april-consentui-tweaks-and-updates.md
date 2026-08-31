---
title: April '23 - ConsentUI Tweaks and Updates
author: Ashman Malik
hidden: false
published_at: '2023-04-06T00:40:35.537Z'
type: added
---
# April '23 :rabbit:

## :hammer: What's Improved?

## Introduced `jobIds` parameter

Basiq allows your users to create multiple connections within a single flow when the `Allow multiple connections` feature is enabled in the Basiq dashboard. With the new `jobIds` parameter, you can retrieve all the `jobIds` from connection attempts appended to the `Redirect URL`.

This parameter makes it easier and more streamlined for you to track the progress of multiple connections within the same session. The `Redirect URL` contains all `jobIds` from that session, including the newest `jobId` like so: 

```text Sample Redirect url with jobIds
http://www.your-redirect-url.com/?jobId=789&jobIds=123,456,789
```

Refer to the [Dashboard configuration](https://api.basiq.io/docs/dash-configuration#4-configuring-any-optional-fields) page for more information on how to enable the Allow multiple connections feature.

## Updated Disclosure object

With this update, the Disclosure object (supporting party) will now be correctly stored when a consent is updated. This ensures that all necessary information related to the supporting party is accurately captured and stored.

Overall, these updates will help improve the functionality and user experience of the ConsentUI tool. Users will now have more comprehensive information at their disposal, enabling better tracking and management of consent-related tasks. Additionally, the improved consent storage will ensure that all necessary information is accurately captured and stored for future reference.
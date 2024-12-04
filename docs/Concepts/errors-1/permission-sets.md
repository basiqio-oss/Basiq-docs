---
title: Permission Sets
excerpt: >-
  Permission sets allow partners to define a group of endpoints which a specific
  API key or Member can access.
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/aee8dac-permissionsGif.gif",
        "permissionsGif.gif",
        1440,
        810,
        "#e8e9eb"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
## Creating a permission set

Navigate to your application settings, and select **New permission set.** From here you can name this and select exactly which endpoints this permission set will allow access to. **E.g.** You may want to delegate `READ ONLY` (GET requests only) access for all of your support engineers in order to troubleshoot for your partners, without granting more power than necessary. 

Once you have saved this permission set you are now able to apply it to the necessary use cases. 

## Applying a permission set

### Dashboard team members
When inviting members to your application, you can select a permission set you have specifically created. By doing this, when your dashboard member accepts the invite, their access privileges are restricted to those specified on setup. This is crucial to ensure your application and its data is secure. 
&nbsp;
&nbsp;
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/de477fb-Screen_Shot_2022-05-26_at_11.23.30_am.png",
        "Screen Shot 2022-05-26 at 11.23.30 am.png",
        2606,
        1666,
        "#eef0f5"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
&nbsp;

### API keys 

Applying a permission set an an API key level will allow you to restrict access to certain environments or third parties. All you need to do is apply the relevant permission set when you generate the new API key, and pass this on. The party using this API key will then only have the access specified in the permission set applied on creation.
&nbsp;
&nbsp;
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/33cc3e6-Screen_Shot_2022-05-26_at_11.22.25_am.png",
        "Screen Shot 2022-05-26 at 11.22.25 am.png",
        2084,
        1664,
        "#ebeef1"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
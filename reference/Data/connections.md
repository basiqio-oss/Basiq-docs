---
title: Connections
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
> 🚧 Connections
>
> The connection object is created whenever a user links their financial institution with your app. Connections act as conduits that retrieve account holders' data (i.e. accounts and transactions) from the institution and store it against the User object. Connections can be deleted and recreated so it is recommended that apps access accounts via the User object rather than the connection.
>
> After a connection is successfully established, you can fetch data created after this point by refreshing the connection. This process ensures on-demand data synchronization between your system and Institution itself. Basiq recommends using the Smart Cache to ensure you always have access to the latest data.
>
> **Note:** You must create your connections from consent UI in version 3.0.

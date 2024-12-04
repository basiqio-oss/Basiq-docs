---
title: TA
description: Recipe Description
hidden: true
recipe:
  color: '#000000'
  icon: ❕
---
```javascript JavaScript
const options = {
  method: 'POST',
  headers: {
    accept: 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
    Authorization: '<<apiKey>>'
  }
};

fetch('https://au-api.basiq.io/token', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```

```json Response Example
{"success":true}
```

# Trusted Advisor

<!-- javascript@ -->

How to Spin up the Trusted advisor?
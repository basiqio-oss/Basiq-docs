---
title: Delete a consent
excerpt: Permanently deletes a users consent, this action cannot be undone.
api:
  file: core.json
  operationId: deleteConsent
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Use this endpoint with caution

Deleting a user consent will permanently delete the entire user consent object including any associated connections and cannot be undone. 

<HTMLBlock>{`
<script src="https://code.jquery.com/jquery-3.5.0.js"></script>
<script>
  setTimeout(() => {    
    const toolTip =  "<p class='toolTip'>&#8505;&#65039; &nbsp; Populate your request using the input fields provided</p>";
    $(toolTip).insertAfter($('.rm-PlaygroundRequest'));
	}, 100)
</script>
`}</HTMLBlock>

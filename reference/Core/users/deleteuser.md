---
title: Delete a user
excerpt: >-
  Permanently deletes a user along with all of their associated connection
  details. All data associated with this user will deleted. You need only supply
  the unique user identifier that was returned upon user creation.
api:
  file: core.json
  operationId: deleteUser
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

Deleting a user will permanently delete the entire user object including any associated connections and their aggregated data and cannot be undone. 

<HTMLBlock>{`
<script src="https://code.jquery.com/jquery-3.5.0.js"></script>
<script>
  setTimeout(() => {    
    const toolTip =  "<p class='toolTip'>&#8505;&#65039; &nbsp; Populate your request using the input fields provided</p>";
    $(toolTip).insertAfter($('.rm-PlaygroundRequest'));
	}, 100)
</script>
`}</HTMLBlock>

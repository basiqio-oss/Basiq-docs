---
title: Create an auth_link
excerpt: >-
  Create a new auth_link object by making a POST request to the auth_link
  endpoint. The new auth_link will effectively delete previous auth_link for
  that user, rendering the previous URL(s) invalid.


  The 'mobile' attribute is used for 2FA SMS verification and is conditionally
  required. If it is not specified, we will look up the mobile on the user
  object; if that is not specified either, you will get an error.  If both are
  specified, the mobile number on the auth_link will take precedence.
api:
  file: core.json
  operationId: postAuthLink
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
<HTMLBlock>{`
<script src="https://code.jquery.com/jquery-3.5.0.js"></script>
<script>
  setTimeout(() => {    
    const toolTip =  "<p class='toolTip'>&#8505;&#65039; &nbsp; Populate your request using the input fields provided</p>";
    $(toolTip).insertAfter($('.rm-PlaygroundRequest'));
	}, 100)
</script>
`}</HTMLBlock>

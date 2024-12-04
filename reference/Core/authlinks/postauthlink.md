---
title: Create an auth_link
excerpt: >-
  Create a new auth_link object by making a POST request to the auth_link
  endpoint. The new auth_link will effectively delete previous auth-links for
  that User/applicant, rendering the previous URL(s) invalid. The 'mobile'
  attribute is optional. If it is specified this number will take preference
  over the User object mobile number for 2FA SMS verification.


  Returns a created auth_link resource, if the operation succeeded. Returns an
  error if the post failed (e.g. not supplying required properties).
api:
  file: core.json
  operationId: postAuthLink
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
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

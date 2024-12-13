---
title: Callouts
fullscreen: false
hidden: true
---
### Custom Callout Example

<div
  style={{
  border: "2px solid #4caf50", 
  borderRadius: "8px", 
  backgroundColor: "#e8f5e9", 
  padding: "16px", 
  margin: "16px 0", 
  fontFamily: "Arial, sans-serif"
}}
>
  <strong>📢 Attention!</strong> This is a callout box made directly in MDX using inline HTML and CSS.
<a href="#" onClick={() => Intercom('showNewMessage', 'Feedback on the new reports feature:')}>
  your feedback on the reports feature
</a>
  <ul>
    <li>Simple to create.</li>
    <li>No extra libraries required.</li>
    <li>Fully customizable with CSS.</li>
  </ul>
</div>

Here is the rest of your MDX content!

```jsx title="/src/components/HelloCodeTitle.js"
function HelloCodeTitle(props) {
  return <h1>Hello, {props.name}</h1>;
}
```
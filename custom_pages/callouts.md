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

  <div style={{ display: 'flex', alignItems: 'center' }}>
    <span
      style={{
      marginLeft: '10px',
      fontSize: '18px', // Increase text size
      whiteSpace: 'nowrap', // Ensure text stays in one line
    }}
    >
      If you have any queries, reach out
    </span>

    <button
      onClick={() => Intercom('showNewMessage', 'issues on FAQs:')}
      style={{
      padding: '12px 30px',
      backgroundColor: '#007bff',
      color: '#ffffff',
      border: 'none',
      borderRadius: '50px',
      fontSize: '16px',
      fontWeight: '600',
      textTransform: 'uppercase',
      cursor: 'pointer',
      boxShadow: '0 4px 10px rgba(0, 123, 255, 0.2)',
      transition: 'background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease',
      outline: 'none',
      display: 'flex',
      justifyContent: 'center',
      height: '45px',
      position: 'relative',
      overflow: 'hidden',
      marginLeft: '10px', // Add space between text and button
      minWidth: '150px', // Ensure the button has enough width for the text
    }}
      onMouseEnter={(e) => {
      e.target.style.transform = 'scale(1.1)';
      e.target.style.boxShadow = '0 6px 15px rgba(0, 123, 255, 0.4)';
    }}
      onMouseLeave={(e) => {
      e.target.style.transform = 'scale(1)';
      e.target.style.boxShadow = '0 4px 10px rgba(0, 123, 255, 0.2)';
    }}
    >
      Support team
    </button>
  </div>
</div>

Here is the rest of your MDX content!

```jsx title="/src/components/HelloCodeTitle.js"
function HelloCodeTitle(props) {
  return <h1>Hello, {props.name}</h1>;
}
```
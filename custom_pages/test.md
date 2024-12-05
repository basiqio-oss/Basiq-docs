---
title: Test Page on the Go
fullscreen: false
hidden: true
metadata:
  title: ''
  description: ''
---
# Hello, world!

Below is an example of markdown in JSX.

<div style={{backgroundColor: 'violet', padding: '1rem'}}>
  Try and change the background color to `tomato`.
</div>

<>
  <blockquote>
    <p>A greater than…</p>
  </blockquote>
</>

// @filename: types.d.ts
import type {} from 'mdx'
// @filename: example.jsx
/// <reference lib="dom" />
/\* @jsxImportSource react \*/
import Example from './example.mdx'
// ---cut---
console.log(

<Example
  components={{
      // Map `h1` (`# heading`) to use `h2`s.
      h1: 'h2',
      // Rewrite `em`s (`*like so*`) to `i` with a goldenrod foreground color.
      em(props) {
        return <i style={{color: 'goldenrod'}} {...props} />
      },
      // Pass a layout (using the special `'wrapper'` key).
      wrapper({components, ...rest}) {
        return <main {...rest} />
      },
      // Pass a component.
      Planet() {
        return 'Neptune'
      },
      // This nested component can be used as `<theme.text>hi</theme.text>`
      theme: {
        text(props) {
          return <span style={{color: 'grey'}} {...props} />
        }
      }
    }}
/>

)
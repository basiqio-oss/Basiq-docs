---
title: Playground
fullscreen: false
hidden: false
---
<br />

***

title: Add Subscribers
description: Add contacts to Basiq Changelog Notifications via the Intercom API
-------------------------------------------------------------------------------

import { useState } from "react"

export function AddSubscriberForm() {
  const [email, setEmail] = useState("")
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)

async function handleSubmit(e) {
  e.preventDefault()
  setLoading(true)
  setResult(null)

  try {
    const res = await fetch("https://v0-rss-to-email-system.vercel.app/api/subscribe", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email }),
    })

    const text = await res.text()
    let data

    try {
      data = text ? JSON.parse(text) : {}
    } catch {
      throw new Error(`Expected JSON but received: ${text.slice(0, 200)}`)
    }

    if (!res.ok) {
      throw new Error(data.error || `Request failed with status ${res.status}`)
    }

    setResult(data)
    if (data.ok) setEmail("")
  } catch (err) {
    console.error(err)
    setResult({
      ok: false,
      error: err instanceof Error ? err.message : "Request failed",
    })
  } finally {
    setLoading(false)
  }
}
  

  return (
    <form onSubmit={handleSubmit} style={{ display: "flex", gap: "8px", flexWrap: "wrap", margin: "16px 0" }}>
      <input
        type="email"
        required
        placeholder="user@example.com"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        disabled={loading}
        style={{
          flex: 1,
          minWidth: "220px",
          padding: "8px 12px",
          borderRadius: "6px",
          border: "1px solid #e2e8f0",
          fontSize: "14px",
          outline: "none",
        }}
      />
      <button
        type="submit"
        disabled={loading || !email}
        style={{
          padding: "8px 16px",
          borderRadius: "6px",
          background: "#3b82f6",
          color: "#fff",
          border: "none",
          fontSize: "14px",
          cursor: loading ? "not-allowed" : "pointer",
          opacity: loading || !email ? 0.6 : 1,
        }}
      >
        {loading ? "Adding..." : "Add Subscriber"}
      </button>
      {result && (
        <p style={{
          width: "100%",
          margin: "4px 0 0",
          fontSize: "13px",
          color: result.ok ? "#16a34a" : "#dc2626",
        }}>
          {result.ok
            ? `${result.contact?.email} has been subscribed successfully.`
            : result.error ?? "Something went wrong."}
        </p>
      )}
    </form>
  )
}

## Add a Subscriber

Use the form below or call the API directly to add a contact to Intercom tagged `basiq-changelog-v2`.

<AddSubscriberForm />

<br />

```js
```

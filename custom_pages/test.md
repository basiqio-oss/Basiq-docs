---
title: Modal Opener
fullscreen: false
hidden: true
metadata:
  title: ''
  description: ''
---
"use client"

import { useState, useEffect } from "react"

export const SimpleCryptoChart = () => {
  const [cryptoData, setCryptoData] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [chartType, setChartType] = useState("bar") // 'bar' or 'area'

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Fetch cryptocurrency data from CoinGecko API
        const response = await fetch(
          "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=6&page=1&sparkline=false&price_change_percentage=24h,7d,30d",
        )

        if (!response.ok) {
          throw new Error("Failed to fetch data")
        }

        const data = await response.json()
        setCryptoData(data)
        setLoading(false)
      } catch (err) {
        console.error("Error fetching data:", err)
        setError(err.message)
        setLoading(false)
      }
    }

    fetchData()
  }, [])

  // Sample data based on the API response format shared
  const sampleData = [
    {
      id: "bitcoin",
      symbol: "btc",
      name: "Bitcoin",
      image: "https://coin-images.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
      current_price: 86013,
      price_change_percentage_24h: 3.47979,
      price_change_percentage_7d_in_currency: 2.78949,
      price_change_percentage_30d_in_currency: -10.20201,
    },
    {
      id: "ethereum",
      symbol: "eth",
      name: "Ethereum",
      image: "https://coin-images.coingecko.com/coins/images/279/large/ethereum.png?1696501628",
      current_price: 2028.41,
      price_change_percentage_24h: 1.25,
      price_change_percentage_7d_in_currency: -3.45,
      price_change_percentage_30d_in_currency: -15.78,
    },
    {
      id: "binancecoin",
      symbol: "bnb",
      name: "BNB",
      image: "https://coin-images.coingecko.com/coins/images/825/large/bnb-icon2_2x.png?1696501970",
      current_price: 570.12,
      price_change_percentage_24h: 2.15,
      price_change_percentage_7d_in_currency: 1.23,
      price_change_percentage_30d_in_currency: -8.45,
    },
    {
      id: "solana",
      symbol: "sol",
      name: "Solana",
      image: "https://coin-images.coingecko.com/coins/images/4128/large/solana.png?1696504756",
      current_price: 145.78,
      price_change_percentage_24h: 5.67,
      price_change_percentage_7d_in_currency: 8.92,
      price_change_percentage_30d_in_currency: -5.34,
    },
    {
      id: "ripple",
      symbol: "xrp",
      name: "XRP",
      image: "https://coin-images.coingecko.com/coins/images/44/large/xrp-symbol-white-128.png?1696501442",
      current_price: 0.58,
      price_change_percentage_24h: -1.23,
      price_change_percentage_7d_in_currency: -2.45,
      price_change_percentage_30d_in_currency: -12.67,
    },
    {
      id: "cardano",
      symbol: "ada",
      name: "Cardano",
      image: "https://coin-images.coingecko.com/coins/images/975/large/cardano.png?1696502090",
      current_price: 0.45,
      price_change_percentage_24h: 0.89,
      price_change_percentage_7d_in_currency: -1.56,
      price_change_percentage_30d_in_currency: -9.87,
    },
  ]

  // Use actual data if available, otherwise use sample data
  const data = cryptoData.length > 0 ? cryptoData : sampleData

  if (loading) {
    return (
      <div className="w-full h-64 flex items-center justify-center bg-gray-100 rounded-lg">
        <div className="text-gray-500">Loading cryptocurrency data...</div>
      </div>
    )
  }

  if (error) {
    return <div className="w-full p-4 bg-red-100 text-red-700 rounded-lg">Error: {error}</div>
  }

  // Render bar chart
  const renderBarChart = () => {
    // Find the maximum absolute percentage change for scaling
    const maxPercentage = Math.max(...data.map((coin) => Math.abs(coin.price_change_percentage_24h || 0)))

    return (
      <div className="mt-6">
        <div className="flex items-end h-64 space-x-6 mb-4">
          {data.map((coin) => {
            const percentage = coin.price_change_percentage_24h || 0
            const isPositive = percentage >= 0
            const barHeight = `${(Math.abs(percentage) / maxPercentage) * 80}%`

            return (
              <div key={coin.id} className="flex-1 flex flex-col items-center">
                <div className="text-sm font-medium mb-2">
                  {percentage > 0 ? "+" : ""}
                  {percentage.toFixed(2)}%
                </div>
                <div className="relative w-full flex justify-center">
                  <div
                    className={`w-16 ${isPositive ? "bg-green-500" : "bg-red-500"} rounded-t-md`}
                    style={{ height: barHeight }}
                  ></div>
                </div>
                <div className="mt-2 flex flex-col items-center">
                  <img src={coin.image || "/placeholder.svg"} alt={coin.name} className="w-6 h-6 rounded-full" />
                  <div className="mt-1 text-sm font-medium">{coin.symbol.toUpperCase()}</div>
                </div>
              </div>
            )
          })}
        </div>
        <div className="text-center text-sm text-gray-500">24-hour Price Change Percentage</div>
      </div>
    )
  }

  // Render area chart
  const renderAreaChart = () => {
    const maxPrice = Math.max(...data.map((coin) => coin.current_price))

    return (
      <div className="mt-6">
        <div className="relative h-64 mb-4">
          {/* Grid lines */}
          {[0, 25, 50, 75, 100].map((percent) => (
            <div key={percent} className="absolute w-full h-px bg-gray-200" style={{ bottom: `${percent}%` }}>
              <span className="absolute -left-10 -translate-y-1/2 text-xs text-gray-400">
                ${((maxPrice * percent) / 100).toLocaleString()}
              </span>
            </div>
          ))}

          {/* Area chart */}
          <svg className="w-full h-full" viewBox={`0 0 ${data.length * 100} 100`} preserveAspectRatio="none">
            <defs>
              <linearGradient id="areaGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stopColor="#3b82f6" stopOpacity="0.8" />
                <stop offset="100%" stopColor="#3b82f6" stopOpacity="0.1" />
              </linearGradient>
            </defs>

            {/* Area path */}
            <path
              d={`
                M0,${100 - (data[0].current_price / maxPrice) * 100}
                ${data.map((coin, i) => `L${i * 100 + 50},${100 - (coin.current_price / maxPrice) * 100}`).join(" ")}
                L${(data.length - 1) * 100 + 50},100 L0,100 Z
              `}
              fill="url(#areaGradient)"
            />

            {/* Line path */}
            <path
              d={`
                M0,${100 - (data[0].current_price / maxPrice) * 100}
                ${data.map((coin, i) => `L${i * 100 + 50},${100 - (coin.current_price / maxPrice) * 100}`).join(" ")}
              `}
              fill="none"
              stroke="#3b82f6"
              strokeWidth="2"
            />

            {/* Data points */}
            {data.map((coin, i) => (
              <circle
                key={i}
                cx={i * 100 + 50}
                cy={100 - (coin.current_price / maxPrice) * 100}
                r="4"
                fill="#3b82f6"
                stroke="#fff"
                strokeWidth="2"
              />
            ))}
          </svg>

          {/* X-axis labels */}
          <div className="absolute bottom-0 left-0 right-0 flex justify-between px-6">
            {data.map((coin) => (
              <div key={coin.id} className="flex flex-col items-center">
                <img src={coin.image || "/placeholder.svg"} alt={coin.name} className="w-6 h-6 rounded-full" />
                <div className="mt-1 text-sm font-medium">{coin.symbol.toUpperCase()}</div>
              </div>
            ))}
          </div>
        </div>
        <div className="text-center text-sm text-gray-500">Current Price (USD)</div>
      </div>
    )
  }

  return (
    <div className="w-full bg-white p-6 rounded-xl shadow-md">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-bold text-gray-800">Cryptocurrency Market Data</h2>
        <div className="flex space-x-2">
          <button
            onClick={() => setChartType("bar")}
            className={`px-3 py-1 text-sm rounded ${
              chartType === "bar" ? "bg-blue-500 text-white" : "bg-gray-200 text-gray-700"
            }`}
          >
            Bar
          </button>
          <button
            onClick={() => setChartType("area")}
            className={`px-3 py-1 text-sm rounded ${
              chartType === "area" ? "bg-blue-500 text-white" : "bg-gray-200 text-gray-700"
            }`}
          >
            Area
          </button>
        </div>
      </div>

      {chartType === "bar" ? renderBarChart() : renderAreaChart()}

      <div className="text-center text-xs text-gray-400 mt-4">
        Data from CoinGecko API • Last updated: {new Date().toLocaleTimeString()}
      </div>
    </div>
  )
}

export default SimpleCryptoChart
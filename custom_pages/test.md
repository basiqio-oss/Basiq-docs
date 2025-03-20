---
title: Modal Opener
fullscreen: false
hidden: true
metadata:
  title: ''
  description: ''
---
import { useState, useEffect } from "react"

export const DynamicCryptoBarChart = () => {
  const [chartData, setChartData] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [hoveredBar, setHoveredBar] = useState(null)
  const [timeRange, setTimeRange] = useState("24h") // 24h, 7d, 30d

  useEffect(() => {
    const fetchCryptoData = async () => {
      try {
        // Fetch top cryptocurrencies from CoinGecko API
        const response = await fetch(
          "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=8&page=1&sparkline=false&price_change_percentage=24h,7d,30d",
        )

        if (!response.ok) {
          throw new Error("Failed to fetch data from CoinGecko")
        }

        const cryptoData = await response.json()

        // Transform the data for our chart
        const transformedData = cryptoData.map((coin) => ({
          id: coin.id,
          symbol: coin.symbol.toUpperCase(),
          name: coin.name,
          image: coin.image,
          currentPrice: coin.current_price,
          marketCap: coin.market_cap,
          priceChange24h: coin.price_change_percentage_24h || 0,
          priceChange7d: coin.price_change_percentage_7d_in_currency || 0,
          priceChange30d: coin.price_change_percentage_30d_in_currency || 0,
          volume: coin.total_volume,
        }))

        setChartData(transformedData)
        setLoading(false)
      } catch (err) {
        console.error("Error fetching crypto data:", err)
        setError(err.message)
        setLoading(false)
      }
    }

    fetchCryptoData()
  }, [])

  // Get the appropriate price change based on selected time range
  const getPriceChange = (coin) => {
    switch (timeRange) {
      case "7d":
        return coin.priceChange7d
      case "30d":
        return coin.priceChange30d
      default:
        return coin.priceChange24h
    }
  }

  // Fallback sample data in case API fails
  const data =
    chartData.length > 0
      ? chartData
      : [
          {
            id: "bitcoin",
            symbol: "BTC",
            name: "Bitcoin",
            currentPrice: 50000,
            priceChange24h: 2.5,
            priceChange7d: 5.2,
            priceChange30d: -3.1,
            volume: 30000000000,
            image: "https://assets.coingecko.com/coins/images/1/large/bitcoin.png",
          },
          {
            id: "ethereum",
            symbol: "ETH",
            name: "Ethereum",
            currentPrice: 3000,
            priceChange24h: 1.8,
            priceChange7d: 4.3,
            priceChange30d: -2.5,
            volume: 15000000000,
            image: "https://assets.coingecko.com/coins/images/279/large/ethereum.png",
          },
          {
            id: "binancecoin",
            symbol: "BNB",
            name: "Binance Coin",
            currentPrice: 400,
            priceChange24h: -0.5,
            priceChange7d: 2.1,
            priceChange30d: -5.3,
            volume: 2000000000,
            image: "https://assets.coingecko.com/coins/images/825/large/bnb-icon2_2x.png",
          },
          {
            id: "cardano",
            symbol: "ADA",
            name: "Cardano",
            currentPrice: 1.5,
            priceChange24h: 3.2,
            priceChange7d: -1.4,
            priceChange30d: 7.8,
            volume: 1500000000,
            image: "https://assets.coingecko.com/coins/images/975/large/cardano.png",
          },
          {
            id: "solana",
            symbol: "SOL",
            name: "Solana",
            currentPrice: 100,
            priceChange24h: 5.7,
            priceChange7d: 12.3,
            priceChange30d: 22.5,
            volume: 3000000000,
            image: "https://assets.coingecko.com/coins/images/4128/large/solana.png",
          },
          {
            id: "polkadot",
            symbol: "DOT",
            name: "Polkadot",
            currentPrice: 30,
            priceChange24h: -1.2,
            priceChange7d: -3.5,
            priceChange30d: 4.2,
            volume: 1000000000,
            image: "https://assets.coingecko.com/coins/images/12171/large/polkadot.png",
          },
        ]

  // Get absolute max value for scaling (ignoring negative values)
  const values = data.map((coin) => Math.abs(getPriceChange(coin)))
  const maxValue = Math.max(...values, 10) // Ensure we have a reasonable minimum

  // Generate colors based on the price change (green for positive, red for negative)
  const getBarColor = (value, isHovered) => {
    const isPositive = value >= 0
    const hue = isPositive ? 142 : 0 // Green or red
    const saturation = 75 + (Math.min(Math.abs(value), maxValue) / maxValue) * 25
    const lightness = isHovered ? 45 : 40
    return `hsl(${hue}, ${saturation}%, ${lightness}%)`
  }

  if (loading) {
    return (
      <div className="w-full h-96 flex flex-col items-center justify-center bg-gradient-to-br from-gray-50 to-gray-100 rounded-xl shadow-sm">
        <div className="relative w-16 h-16">
          {[0, 1, 2].map((i) => (
            <div
              key={i}
              className="absolute top-0 left-0 w-full h-full border-4 border-t-blue-500 border-r-transparent border-b-transparent border-l-transparent rounded-full"
              style={{
                animation: `spin ${1 + i * 0.2}s linear infinite`,
                animationDelay: `${i * 0.1}s`,
                opacity: 1 - i * 0.2,
              }}
            />
          ))}
        </div>
        <div className="mt-4 text-blue-500 font-medium">Loading cryptocurrency data...</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="w-full p-8 bg-red-50 border border-red-200 rounded-xl shadow-sm">
        <div className="flex items-center justify-center">
          <div className="w-10 h-10 flex items-center justify-center rounded-full bg-red-100 text-red-500">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              className="w-6 h-6"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
              />
            </svg>
          </div>
          <div className="ml-3 text-red-700 font-medium">Error: {error}</div>
        </div>
      </div>
    )
  }

  return (
    <div className="w-full bg-gradient-to-br from-gray-50 to-gray-100 p-6 rounded-xl shadow-lg">
      <h2 className="text-3xl font-bold text-center mb-2 bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-purple-600">
        Cryptocurrency Price Changes
      </h2>
      <p className="text-center text-gray-500 mb-4">Data from CoinGecko API</p>

      {/* Time range selector */}
      <div className="flex justify-center mb-6 space-x-2">
        {["24h", "7d", "30d"].map((range) => (
          <button
            key={range}
            onClick={() => setTimeRange(range)}
            className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
              timeRange === range ? "bg-blue-500 text-white shadow-md" : "bg-gray-200 text-gray-700 hover:bg-gray-300"
            }`}
          >
            {range}
          </button>
        ))}
      </div>

      {/* Chart container */}
      <div className="relative h-80 mb-6">
        {/* Zero line */}
        <div className="absolute left-0 right-0 h-px bg-gray-300" style={{ top: "50%" }}></div>

        {/* Y-axis grid lines and labels */}
        <div className="absolute inset-0 flex flex-col justify-between pointer-events-none">
          {[-100, -75, -50, -25, 0, 25, 50, 75, 100].map((percent, i) => {
            const position = 50 - percent / 2
            return (
              <div
                key={i}
                className={`w-full h-px ${percent === 0 ? "bg-gray-400" : "bg-gray-200"}`}
                style={{ top: `${position}%` }}
              >
                <span className="absolute -left-8 -translate-y-1/2 text-xs text-gray-500">{percent}%</span>
              </div>
            )
          })}
        </div>

        {/* Bars container */}
        <div className="absolute inset-0 flex items-center justify-around pl-8">
          {data.map((coin, idx) => {
            const isHovered = hoveredBar === idx
            const priceChange = getPriceChange(coin)
            const isPositive = priceChange >= 0
            const barHeight = Math.min((Math.abs(priceChange) / maxValue) * 100, 100)
            const barColor = getBarColor(priceChange, isHovered)

            return (
              <div
                key={idx}
                className="group relative flex flex-col items-center h-full"
                style={{ width: `${100 / data.length}%` }}
                onMouseEnter={() => setHoveredBar(idx)}
                onMouseLeave={() => setHoveredBar(null)}
              >
                {/* Value indicator */}
                <div
                  className={`absolute ${isPositive ? "bottom-full mb-1" : "top-full mt-1"} left-1/2 -translate-x-1/2 px-2 py-1 rounded text-white text-xs font-bold transition-all duration-300 z-10 ${isHovered ? "opacity-100 scale-100" : "opacity-0 scale-90"}`}
                  style={{ backgroundColor: barColor }}
                >
                  {priceChange > 0 ? "+" : ""}
                  {priceChange.toFixed(2)}%
                </div>

                {/* Bar */}
                <div
                  className="relative w-full max-w-[40px] transition-all duration-500 cursor-pointer"
                  style={{
                    height: `${barHeight}%`,
                    background: `linear-gradient(${isPositive ? "to top" : "to bottom"}, ${barColor}, ${barColor.replace("hsl", "hsla").replace(")", ", 0.8)")}`,
                    boxShadow: isHovered
                      ? `0 0 15px ${barColor.replace("hsl", "hsla").replace(")", ", 0.5)")}`
                      : "none",
                    transform: isHovered ? `scale${isPositive ? "Y" : "Y"}(1.05)` : "scale(1)",
                    animation: `barGrow 1s ease forwards ${idx * 0.15}s`,
                    position: "absolute",
                    [isPositive ? "bottom" : "top"]: "50%",
                    borderRadius: isPositive ? "4px 4px 0 0" : "0 0 4px 4px",
                  }}
                >
                  {/* Shine effect */}
                  <div className="absolute inset-0 overflow-hidden">
                    <div
                      className="absolute top-0 left-0 w-full h-full bg-gradient-to-br from-white/30 to-transparent"
                      style={{
                        clipPath: "polygon(0 0, 100% 0, 70% 100%, 0% 100%)",
                        opacity: isHovered ? 0.4 : 0.2,
                      }}
                    />
                  </div>

                  {/* Animated dots */}
                  {isHovered && (
                    <>
                      {[...Array(3)].map((_, i) => (
                        <div
                          key={i}
                          className="absolute w-1 h-1 rounded-full bg-white/70"
                          style={{
                            left: `${Math.random() * 100}%`,
                            top: `${Math.random() * 100}%`,
                            animation: `float 3s ease-in-out infinite`,
                            animationDelay: `${i * 0.2}s`,
                          }}
                        />
                      ))}
                    </>
                  )}
                </div>

                {/* Coin icon */}
                <div className="absolute top-1/2 -translate-y-1/2 w-6 h-6 rounded-full overflow-hidden bg-white shadow-md">
                  <img
                    src={coin.image || "/placeholder.svg"}
                    alt={coin.name}
                    className="w-full h-full object-cover"
                    onError={(e) => {
                      e.target.onerror = null
                      e.target.src = `https://via.placeholder.com/32/CCCCCC/808080?text=${coin.symbol.charAt(0)}`
                    }}
                  />
                </div>

                {/* Label */}
                <div className="absolute bottom-0 text-sm font-medium text-gray-700">{coin.symbol}</div>

                {/* Tooltip */}
                <div
                  className={`absolute top-1/2 -translate-y-1/2 ${idx > data.length / 2 ? "right-full mr-4" : "left-full ml-4"} w-56 p-3 rounded-lg bg-white shadow-xl border border-gray-200 transition-all duration-300 z-20 ${isHovered ? "opacity-100 translate-x-0" : "opacity-0 translate-x-2 pointer-events-none"}`}
                  style={{ display: isHovered ? "block" : "none" }}
                >
                  <div className="flex items-center mb-2">
                    <div className="w-8 h-8 rounded-full overflow-hidden bg-white shadow-sm mr-2">
                      <img
                        src={coin.image || "/placeholder.svg"}
                        alt={coin.name}
                        className="w-full h-full object-cover"
                      />
                    </div>
                    <div>
                      <div className="text-sm font-bold text-gray-800">{coin.name}</div>
                      <div className="text-xs text-gray-500">{coin.symbol}</div>
                    </div>
                  </div>

                  <div className="space-y-1">
                    <div className="flex justify-between text-xs">
                      <span className="text-gray-500">Price:</span>
                      <span className="font-semibold text-gray-700">${coin.currentPrice.toLocaleString()}</span>
                    </div>
                    <div className="flex justify-between text-xs">
                      <span className="text-gray-500">24h Change:</span>
                      <span className={`font-semibold ${coin.priceChange24h >= 0 ? "text-green-600" : "text-red-600"}`}>
                        {coin.priceChange24h > 0 ? "+" : ""}
                        {coin.priceChange24h.toFixed(2)}%
                      </span>
                    </div>
                    <div className="flex justify-between text-xs">
                      <span className="text-gray-500">7d Change:</span>
                      <span className={`font-semibold ${coin.priceChange7d >= 0 ? "text-green-600" : "text-red-600"}`}>
                        {coin.priceChange7d > 0 ? "+" : ""}
                        {coin.priceChange7d.toFixed(2)}%
                      </span>
                    </div>
                    <div className="flex justify-between text-xs">
                      <span className="text-gray-500">30d Change:</span>
                      <span className={`font-semibold ${coin.priceChange30d >= 0 ? "text-green-600" : "text-red-600"}`}>
                        {coin.priceChange30d > 0 ? "+" : ""}
                        {coin.priceChange30d.toFixed(2)}%
                      </span>
                    </div>
                    <div className="flex justify-between text-xs">
                      <span className="text-gray-500">Volume:</span>
                      <span className="font-semibold text-gray-700">${(coin.volume / 1000000000).toFixed(2)}B</span>
                    </div>
                  </div>

                  <div
                    className="absolute top-1/2 -translate-y-1/2 w-2 h-2 bg-white border border-gray-200 transform rotate-45 
                    ${idx > data.length / 2 ? 'right-0 translate-x-1 border-l-0 border-b-0' : 'left-0 -translate-x-1 border-r-0 border-t-0'}"
                  ></div>
                </div>
              </div>
            )
          })}
        </div>
      </div>

      {/* Legend */}
      <div className="flex justify-center items-center space-x-6 mt-8">
        <div className="flex items-center">
          <div className="w-3 h-3 rounded-full bg-green-500 mr-2"></div>
          <span className="text-xs text-gray-600">Price Increase</span>
        </div>
        <div className="flex items-center">
          <div className="w-3 h-3 rounded-full bg-red-500 mr-2"></div>
          <span className="text-xs text-gray-600">Price Decrease</span>
        </div>
      </div>

      <div className="text-center text-xs text-gray-400 mt-4">
        Data refreshes every time the component loads. Last updated: {new Date().toLocaleTimeString()}
      </div>

      {/* Animation keyframes */}
      <style jsx>{`
        @keyframes barGrow {
          0% { transform: scaleY(0); opacity: 0; }
          100% { transform: scaleY(1); opacity: 1; }
        }
        
        @keyframes float {
          0%, 100% { transform: translateY(0); }
          50% { transform: translateY(-5px); }
        }
        
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  )
}

export default DynamicCryptoBarChart
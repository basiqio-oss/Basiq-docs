---
title: Modal Opener
fullscreen: false
hidden: true
metadata:
  title: ''
  description: ''
---
import \{ useEffect, useState } from 'react';

export const AnimatedBarChart = () => \{
&#x20; const \[bars, setBars] = useState(\[]);

&#x20; useEffect(() => \{
&#x20;   const chartData = \[
&#x20;     \{ label: 'Jan', value: 45 },
&#x20;     \{ label: 'Feb', value: 60 },
&#x20;     \{ label: 'Mar', value: 35 },
&#x20;     \{ label: 'Apr', value: 80 },
&#x20;     \{ label: 'May', value: 55 },
&#x20;     \{ label: 'Jun', value: 70 },
&#x20;   ];
&#x20;   setBars(chartData);
&#x20; }, \[]);

&#x20; return (
&#x20;   \<div className="flex flex-col items-center py-8">
&#x20;     \<div className="flex items-end justify-center gap-4 h-64 px-6 border-b border-gray-200 relative">
&#x20;       \{bars.map((bar, i) => (
&#x20;         \<div key=\{i} className="group relative flex flex-col items-center">
&#x20;           \<div
&#x20;             className="w-12 rounded-t-md transition-all duration-500 ease-in-out transform group-hover:-translate-y-2"
&#x20;             style=\{\{
&#x20;               height: \`$\{bar.value \* 2}px\`,
&#x20;               background: \`linear-gradient(to top, #3b82f6, #60a5fa)\`,
&#x20;               boxShadow: '0 4px 8px rgba(0,0,0,0.2)',
&#x20;             }}
&#x20;           \>
&#x20;             \<div
&#x20;               className="absolute inset-x-0 -bottom-1 h-2 transform skew-x-\[45deg] bg-blue-400 opacity-50"
&#x20;               style=\{\{ transformOrigin: 'top left' }}
&#x20;             />
&#x20;           \</div>
&#x20;           \<span className="mt-2 text-gray-600">\{bar.label}\</span>
&#x20;         \</div>
&#x20;       ))}
&#x20;     \</div>
&#x20;     \<h3 className="text-xl font-semibold mt-6">Monthly Performance\</h3>
&#x20;   \</div>
&#x20; );
};
\<div>
&#x20; \<AnimatedPieChart />
&#x20; \<AnimatedBarChart />
\</div>
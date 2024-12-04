---
title: test
fullscreen: false
hidden: true
metadata:
  title: ''
  description: ''
---
[block:html]
{
  "html": "<html lang=\"en\">\n<head>\n  <meta charset=\"UTF-8\" />\n  <title>Three.js 101</title>\n  <!--  Simple reset to delete the margins  -->\n  <style>\n    body { margin: 0; }\n    canvas { width: 100%; height: 100% }\n  </style>\n  <!--  Three.js CDN  -->\n  <script src=\"https://cdnjs.cloudflare.com/ajax/libs/three.js/r83/three.min.js\"></script>\n</head>\n<body>\n  <!--  Our code  -->\n  <script>\n  var scene = new THREE.Scene();\n\n// Create a basic perspective camera\nvar camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );\ncamera.position.z = 4;\n\n// Create a renderer with Antialiasing\nvar renderer = new THREE.WebGLRenderer({antialias:true});\n\n// Configure renderer clear color\nrenderer.setClearColor(\"#000000\");\n\n// Configure renderer size\nrenderer.setSize( window.innerWidth, window.innerHeight );\n\n// Append Renderer to DOM\ndocument.body.appendChild( renderer.domElement );\n\n// ------------------------------------------------\n// FUN STARTS HERE\n// ------------------------------------------------\n\n// Create a Cube Mesh with basic material\nvar geometry = new THREE.BoxGeometry( 1, 1, 1 );\nvar material = new THREE.MeshBasicMaterial( { color: \"#433F81\" } );\nvar cube = new THREE.Mesh( geometry, material );\n\n// Add cube to Scene\nscene.add( cube );\n\n// Render Loop\nvar render = function () {\n  requestAnimationFrame( render );\n\n  cube.rotation.x += 0.01;\n  cube.rotation.y += 0.01;\n\n  // Render the scene\n  renderer.render(scene, camera);\n};\n\nrender();\n\n  \n  </script>\n</body>\n</html>"
}
[/block]
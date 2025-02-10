# 360° VR Platform

A web-based platform for viewing 360° panoramic photos in VR, with special support for Oculus devices.

## Features

- 360° panoramic photo viewing
- VR mode support through WebXR
- Head tracking in VR mode
- Desktop and VR UI
- Scene selection and hotspots
- Loading screen with progress indicator
- Responsive design

## Technical Requirements

- A WebXR-compatible browser (e.g., Oculus Browser, Chrome, Firefox)
- HTTPS connection (required for WebXR)
- Modern web browser with JavaScript enabled

## Setup

1. Host the files on a web server with HTTPS enabled
2. Place your 360° panoramic images in an `images` directory
3. Update the scene list in `index.html` with your panoramic images
4. Access the site through a WebXR-compatible browser

## Development

To run locally for development:

1. Use a local development server with HTTPS
2. For Oculus testing, host on a public HTTPS server
3. Ensure all 360° images are in equirectangular format (2:1 aspect ratio)

## Usage

### Desktop Mode
- Use mouse to look around
- Click and drag to rotate view
- Use scene selector to switch between different panoramas

### VR Mode
- Click "Enter VR" button (appears automatically on compatible devices)
- Use head movement to look around
- Use controller to interact with hotspots (when available)

## Optimization Tips

- Optimize panoramic images for web (recommended max size: 4096x2048)
- Use progressive loading for better performance
- Consider using different resolution images for desktop/VR modes

## Browser Support

- Oculus Browser
- Google Chrome (with WebXR)
- Mozilla Firefox (with WebXR)
- Other WebXR-compatible browsers

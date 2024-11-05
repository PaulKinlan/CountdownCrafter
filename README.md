# Countdown Timer Web App

A Flask-based countdown timer web application that allows users to create, customize, and share countdown timers for various events. The application features a responsive design, multiple themes, and home screen installation support.

## Features

- **Timer Creation**: Create countdown timers for any future event
- **Customizable Themes**:
  - Default: Clean, modern look
  - Neon: Vibrant, glowing design
  - Minimal: Simple, distraction-free interface
  - Retro: Classic, nostalgic style

- **Flexible Layouts**:
  - Standard: Balanced presentation
  - Compact: Space-efficient display
  - Expanded: Large, prominent countdown

- **Sharing Capabilities**:
  - Web Share API support for mobile devices
  - Fallback clipboard copying for desktop
  - Shareable links without edit access

- **Timer Management**:
  - Edit timer details
  - Update event name and end date
  - Delete timers
  - Secure edit access with tokens

- **Progressive Web App Features**:
  - Add to Home Screen functionality
  - Standalone window mode
  - Custom app icon

## Installation

1. Clone the project on Replit or use the "Fork" button
2. The project automatically sets up:
   - Python environment
   - Required packages (Flask, SQLAlchemy)
   - PostgreSQL database

3. Environment variables are automatically configured in Replit's Secrets tab:
   - `DATABASE_URL`: PostgreSQL connection string
   - `FLASK_SECRET_KEY`: Application secret key

## Usage

### Creating a Timer

1. Visit the home page
2. Enter the event name
3. Set the end date and time
4. Choose a theme (Default, Neon, Minimal, or Retro)
5. Select a layout (Standard, Compact, or Expanded)
6. Click "Create Timer"

### Managing Timers

- **Editing**: Use the "Edit Timer" button (requires edit token)
  - Modify event name
  - Update end date/time
  - Change theme or layout

- **Deleting**: Use the "Delete Timer" button (requires edit token)

### Sharing Timers

1. Click the "Share Timer" button
2. On mobile:
   - Uses native share sheet
   - Share via apps or copy link
3. On desktop:
   - Copies link to clipboard
   - Share manually

### Installing to Home Screen

1. Click "Add to Home Screen" when prompted
2. Or use browser's install PWA option
3. App launches in standalone mode

## Development

The application uses:
- Flask for the backend
- SQLAlchemy for database operations
- Bootstrap for responsive design
- JavaScript for real-time updates

## Security

- Edit tokens protect timer modifications
- Shared URLs exclude edit access
- Database connections use connection pooling
- SQL injection protection via SQLAlchemy

## Deployment

The application is designed to run on Replit:
1. Environment setup is automatic
2. Database provisioning is handled by Replit
3. Secrets management through Replit's Secrets tab

## Support

For issues or suggestions:
1. Check your browser console for errors
2. Verify database connection
3. Ensure all required environment variables are set

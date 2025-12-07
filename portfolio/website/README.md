# 🌐 Website User Guide: How to Edit Your Portfolio
*You don't need to be a Web Developer to change this text.*

## 1. How to Open the Website
*   **Method A (Offline)**: Double-click `index.html`. It will open in Chrome/Edge.
*   **Method B (Online)**: Use the GitHub Pages URL (if you set it up).

## 2. How to Edit the Text
You want to change the "About Me" or "Skills"?
1.  Right-click `index.html` -> Open with VS Code.
2.  **Ctrl+F** (Find) the text you want to change (e.g., "Prasanna").
3.  Type your new text.
4.  Save (`Ctrl+S`).
5.  Refresh the browser.

## 3. How to Change Colors
1.  Open `style.css` in VS Code.
2.  Look for `:root` at the top.
    ```css
    :root {
        --primary-color: #2563eb; /* Blue */
    }
    ```
3.  Change the Hex Code (e.g., `#ff0000` for Red).

## 4. How to Update Project Links
In `index.html`, look for the `<a>` tags:
```html
<a href="https://github.com/..." ...>
```
Replace the `href` link with your new Project URL.

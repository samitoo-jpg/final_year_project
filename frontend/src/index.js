import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';  // Importing your CSS file for styling
import App from './App';  // Importing the main App component
import reportWebVitals from './reportWebVitals';  // Importing the web vitals report function

// Rendering the React App component to the DOM inside the element with the id 'root'
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />  {/* Rendering the App component */}
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
reportWebVitals();



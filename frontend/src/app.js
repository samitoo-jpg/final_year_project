import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./auth/Login"; // Use correct casing
import InventoryDashboard from "./components/InventoryDashboard"; // Ensure this file exists

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<InventoryDashboard />} />
      </Routes>
    </Router>
  );
};

export default App;


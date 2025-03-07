import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./components/Login";
import ProductList from "./components/ProductList";
import InventoryDashboard from "./components/InventoryDashboard";
import ProtectedRoute from "./components/ProtectedRoute"; // Ensure you have this component
import "./App.css";

const App = () => {
  return (
    <Router>
    <div>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <InventoryDashboard />
            </ProtectedRoute>
          }
        />
        <Route
          path="/products"  // 🔥 Changed from "/inventory" to "/products"
          element={
            <ProtectedRoute>
              <ProductList />
            </ProtectedRoute>
          }
        />
      </Routes>
    </div>
  </Router>
  
  );
};

export default App;





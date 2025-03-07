import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./components/Login";
import ProductList from "./components/ProductList";
import InventoryDashboard from "./components/InventoryDashboard";
import ManageProducts from "./components/ManageProducts"; // ✅ Import ManageProducts
import EditProduct from "./components/EditProduct"; // ✅ Import EditProduct
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
            path="/products"
            element={
              <ProtectedRoute>
                <ProductList />
              </ProtectedRoute>
            }
          />
          <Route
            path="/manage-products"
            element={
              <ProtectedRoute>
                <ManageProducts />
              </ProtectedRoute>
            }
          />
          <Route
            path="/edit-product/:id"
            element={
              <ProtectedRoute>
                <EditProduct />
              </ProtectedRoute>
            }
          />
        </Routes>
      </div>
    </Router>
  );
};

export default App;






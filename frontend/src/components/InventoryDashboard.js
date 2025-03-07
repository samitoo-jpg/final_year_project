import React, { useEffect, useState } from "react";
import api from "../axiosConfig";
import { Link } from "react-router-dom";

const InventoryDashboard = () => {
  const [inventory, setInventory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchInventory();
  }, []);

  // ✅ Fetch inventory data
  const fetchInventory = async () => {
    try {
      const response = await api.get("/api/get-inventory/");
      setInventory(response.data);
      setLoading(false);
    } catch (error) {
      console.error("Error fetching inventory:", error);
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Inventory Dashboard</h2>
      <nav>
        <ul>
          <li>
            <Link to="/products">Manage Products</Link>
          </li>
        </ul>
      </nav>

      {loading ? (
        <p>Loading inventory...</p>
      ) : (
        <table border="1">
          <thead>
            <tr>
              <th>ID</th>
              <th>Product</th>
              <th>Stock</th>
              <th>Last Updated</th>
            </tr>
          </thead>
          <tbody>
            {inventory.map((item) => (
              <tr key={item.id}>
                <td>{item.id}</td>
                <td>{item.product_name}</td>
                <td>{item.stock_quantity}</td>
                <td>{new Date(item.updated_at).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default InventoryDashboard;





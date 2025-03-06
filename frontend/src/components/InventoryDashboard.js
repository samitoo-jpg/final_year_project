import React, { useEffect, useState } from "react";
import api from "../api/axiosConfig"; // ✅ Import API instance

const InventoryDashboard = () => {
    const [products, setProducts] = useState([]);
    const token = localStorage.getItem("access_token"); // Get stored token

    useEffect(() => {
        if (!token) {
            console.error("No token found. Redirecting to login...");
            window.location.href = "/login"; // Redirect if not logged in
            return;
        }

        fetchInventory(); // Call API request function
    }, [token]);

    const fetchInventory = async () => {
        try {
            const response = await api.get("/get-inventory/");
            console.log("Fetched products:", response.data); // Log the response data
    
            setProducts(response.data); // Store the fetched data
        } catch (error) {
            console.error("Error fetching products:", error);
            if (error.response && error.response.status === 401) {
                alert("Session expired. Please log in again.");
                localStorage.removeItem("access_token"); // Remove invalid token
                window.location.href = "/login"; // Redirect to login
            }
        }
    };    

    return (
        <div>
            <h1>Inventory Dashboard</h1>
            <ul>
                {products.length > 0 ? (
                    products.map((product) => (
                        <li key={product.id}>
                            {product.name} - {product.stock_quantity} units
                        </li>
                    ))
                ) : (
                    <p>Loading products...</p>
                )}
            </ul>
        </div>
    );
};

export default InventoryDashboard;




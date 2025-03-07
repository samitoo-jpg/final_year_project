import React, { useState } from "react";
import api from "../axiosConfig";

const AddProduct = ({ onProductAdded }) => {
  const [product, setProduct] = useState({
    name: "",
    category: "",
    supplier: "",
    quantity: "",
    price: "",
  });

  // ✅ Handle input change
  const handleChange = (e) => {
    setProduct({ ...product, [e.target.name]: e.target.value });
  };

  // ✅ Submit form
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("/api/products/", product);
      onProductAdded(); // Refresh product list
    } catch (error) {
      console.error("Error adding product:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Add New Product</h3>
      <input type="text" name="name" placeholder="Product Name" onChange={handleChange} required />
      <input type="text" name="category" placeholder="Category ID" onChange={handleChange} required />
      <input type="text" name="supplier" placeholder="Supplier ID" onChange={handleChange} required />
      <input type="number" name="quantity" placeholder="Quantity" onChange={handleChange} required />
      <input type="number" name="price" placeholder="Price" onChange={handleChange} required />
      <button type="submit">Add Product</button>
    </form>
  );
};

export default AddProduct;

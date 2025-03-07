import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import api from "../axiosConfig";

const EditProduct = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [product, setProduct] = useState({ name: "", price: "", stock: "" });

  useEffect(() => {
    fetchProduct();
  }, []);

  const fetchProduct = async () => {
    try {
      const response = await api.get(`/api/products/${id}/`);
      setProduct(response.data);
    } catch (error) {
      console.error("Error fetching product:", error);
    }
  };

  const handleChange = (e) => {
    setProduct({ ...product, [e.target.name]: e.target.value });
  };

  const handleUpdate = async () => {
    try {
      await api.put(`/api/products/${id}/`, product);
      alert("Product updated successfully!");
      navigate("/manage-products");
    } catch (error) {
      console.error("Error updating product:", error);
    }
  };

  return (
    <div>
      <h2>Edit Product</h2>
      <input type="text" name="name" value={product.name} onChange={handleChange} />
      <input type="number" name="price" value={product.price} onChange={handleChange} />
      <input type="number" name="stock" value={product.stock} onChange={handleChange} />
      <button onClick={handleUpdate}>Update Product</button>
    </div>
  );
};

export default EditProduct;

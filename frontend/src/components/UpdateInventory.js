import React, { useState } from "react";
import api from "../api/axios"; // ✅ Import axios instance

const UpdateInventory = () => {
  const [productId, setProductId] = useState("");
  const [quantity, setQuantity] = useState("");
  const [changeType, setChangeType] = useState("added");

  const handleUpdate = async () => {
    try {
      const response = await api.post("/api/update-inventory/", {
        product_id: productId,
        quantity: quantity,
        change_type: changeType,
      });
      alert(response.data.message);
    } catch (error) {
      console.error("Error updating inventory:", error);
      alert("Failed to update inventory");
    }
  };

  return (
    <div>
      <h2>Update Inventory</h2>
      <input
        type="text"
        placeholder="Product ID"
        value={productId}
        onChange={(e) => setProductId(e.target.value)}
      />
      <input
        type="number"
        placeholder="Quantity"
        value={quantity}
        onChange={(e) => setQuantity(e.target.value)}
      />
      <select value={changeType} onChange={(e) => setChangeType(e.target.value)}>
        <option value="added">Add Stock</option>
        <option value="removed">Remove Stock</option>
      </select>
      <button onClick={handleUpdate}>Update Inventory</button>
    </div>
  );
};

export default UpdateInventory;

import React from "react";

const Logout = () => {
  const handleLogout = () => {
    localStorage.removeItem("access_token"); // ✅ Remove token
    alert("Logged out successfully");
    window.location.href = "/login";
  };

  return <button onClick={handleLogout}>Logout</button>;
};

export default Logout;

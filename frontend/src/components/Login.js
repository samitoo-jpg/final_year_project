import React, { useState } from "react";
import api from "../axiosConfig";  // ✅ Ensure this path is correct

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(""); // ✅ Track errors

  const handleLogin = async () => {
    setError(""); // Clear previous errors

    try {
      const response = await api.post("/api/token/", {
        username: username,
        password: password,
      });

      // ✅ Save token in localStorage
      localStorage.setItem("access_token", response.data.access);
      localStorage.setItem("refresh_token", response.data.refresh);

      alert("Login Successful ✅");
      window.location.href = "/dashboard"; // ✅ Redirect after login
    } catch (error) {
      console.error("Login error:", error);
      setError("Invalid credentials. Please try again."); // Show error message
    }
  };

  return (
    <div>
      <h2>Login</h2>
      {error && <p style={{ color: "red" }}>{error}</p>} {/* ✅ Display errors */}

      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;










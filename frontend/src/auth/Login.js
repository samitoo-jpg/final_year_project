import React, { useState } from "react";
import api from "../api/axiosConfig"; 

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try {
      const response = await api.post("/api/token/", {
        username: username,
        password: password,
      });

      localStorage.setItem("access_token", response.data.access); // ✅ Save token
      alert("Login Successful");
      window.location.href = "/dashboard"; // ✅ Redirect after login
    } catch (error) {
      console.error("Login error:", error);
      alert("Invalid credentials");
    }
  };

  return (
    <div>
      <h2>Login</h2>
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









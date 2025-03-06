import axios from "axios";

// ✅ Backend API URL (Change if needed)
const BASE_URL = "http://127.0.0.1:8000"; 

// ✅ Get token from localStorage
const getAuthToken = () => {
  return localStorage.getItem("access_token");
};

// ✅ Create axios instance
const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// ✅ Attach token to every request
api.interceptors.request.use(
  (config) => {
    const token = getAuthToken();
    if (token) {
      config.headers["Authorization"] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;


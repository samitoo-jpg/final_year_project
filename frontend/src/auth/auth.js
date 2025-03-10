// src/auth.js
export const getAccessToken = () => {
    return localStorage.getItem("accessToken");
  };
  
  export const getRefreshToken = () => {
    return localStorage.getItem("refreshToken");
  };
  
  export const saveTokens = (accessToken, refreshToken) => {
    localStorage.setItem("accessToken", accessToken);
    localStorage.setItem("refreshToken", refreshToken);
  };
  
  export const clearTokens = () => {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
  };
  
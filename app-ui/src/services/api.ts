import axios from "axios";
import { v4 as uuidv4 } from 'uuid'; // Import UUID generation function

const Api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || "http://localhost:8000/api",
});

// Request interceptor for adding common headers (e.g., Authorization, Trace ID)
Api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token"); // Example: Retrieving token from local storage
  const traceId = uuidv4(); // Generate a UUID for traceability

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  config.headers["X-Trace-ID"] = traceId;
  
  console.log(`Starting request to ${config.url} with Trace ID: ${traceId}`, config);
  return config;
});

// Response interceptor for logging and handling errors
Api.interceptors.response.use(
  (response) => {
    console.log(`Response from ${response.config.url}`, response);
    return response;
  },
  (error) => {
    return handleErrorResponse(error); // Centralized error handling
  }
);

// Centralized error handling
const handleErrorResponse = (error: any) => {
  console.error("API Error:", error);
  
  if (error.response) {
    // Server responded with a status other than 2xx
    console.error(`Error Status: ${error.response.status}`);
    console.error(`Error Data: ${error.response.data}`);
  } else if (error.request) {
    // Request was made but no response was received
    console.error("No response received:", error.request);
  } else {
    // Something else triggered an error
    console.error("Error setting up request:", error.message);
  }

  return Promise.reject(error);
};

// Export the configured Axios instance
export default Api;

import "./styles/index.css";
import App from "./App";
import { Provider } from "react-redux";
import store from "./store";
import ErrorBoundary from "./components/ErrorBoundary/ErrorBoundary";

import { createRoot } from "react-dom/client";

const container = document.getElementById("app");

if (container) {
  const root = createRoot(container);
  root.render(
    <Provider store={store}>
      <ErrorBoundary>
        <App />
      </ErrorBoundary>
    </Provider>
  );
} else {
  console.error("Failed to find the root element.");
}

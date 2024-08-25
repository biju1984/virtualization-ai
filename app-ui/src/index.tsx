import React from 'react';
import ReactDOM from 'react-dom';
import './styles/index.css';
import App from './App';
import { Provider } from 'react-redux';
import store from 'store';
import ErrorBoundary from '@components/ErrorBoundary/ErrorBoundary';

ReactDOM.render(
  <Provider store={store}>
    <ErrorBoundary>
    <App />
  </ErrorBoundary>
    </Provider>,
  document.getElementById('root')
);

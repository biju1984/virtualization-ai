import { render } from '@testing-library/react';
import { Provider } from 'react-redux';
import { store } from '../../src/store';

export const renderWithProviders = (ui: React.ReactElement) => {
  return render(
    <Provider store={store}>
      {ui}
    </Provider>
  );
};

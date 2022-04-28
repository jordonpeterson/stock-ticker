import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import StockTicker from './StockTicker';

describe('<StockTicker />', () => {
  test('it should mount', () => {
    render(<StockTicker />);
    
    const stockTicker = screen.getByTestId('StockTicker');

    expect(stockTicker).toBeInTheDocument();
  });
});
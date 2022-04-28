import React, { lazy, Suspense } from 'react';

const LazyStockTicker = lazy(() => import('./StockTicker'));

const StockTicker = (props: JSX.IntrinsicAttributes & { children?: React.ReactNode; }) => (
  <Suspense fallback={null}>
    <LazyStockTicker {...props} />
  </Suspense>
);

export default StockTicker;

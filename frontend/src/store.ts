import {configureStore} from "@reduxjs/toolkit";
import {stockTickerSlice} from "./components/StockTicker/stockTickerSlice";


export default configureStore({
    reducer: {
        stockTicker: stockTickerSlice.reducer
    }
})
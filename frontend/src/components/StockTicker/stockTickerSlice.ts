import {createSlice} from '@reduxjs/toolkit'
import {TickerData} from "../../models/TickerData";

const initialState: TickerData = {
    max_price: 0,
    min_price: 0,
    avg_price: 0,
    max_volume: 0,
    min_volume: 0,
    avg_volume: 0
}

export const stockTickerSlice = createSlice({
    name: 'stockTicker',
    initialState,
    reducers: {
        setStockTickerData: (state, action) => {
            state = action.payload
        },
    }
})

export const {setStockTickerData} = stockTickerSlice.actions

export const selectStockTickerData = (state: any) => state.stockTicker


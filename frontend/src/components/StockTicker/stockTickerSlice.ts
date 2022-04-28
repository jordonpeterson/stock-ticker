import {createAsyncThunk, createSlice} from '@reduxjs/toolkit'

const initialState = {
    tickerInfo: {
        max_price: 0,
        min_price: 0,
        avg_price: 0,
        max_volume: 0,
        min_volume: 0,
        avg_volume: 0
    },
    status: 'idle',
    error: null
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

export const loadTickerData = createAsyncThunk('stockTicker/loadTickerData', async () => {

    }
)

export const {setStockTickerData} = stockTickerSlice.actions

export const selectStockTickerData = (state: any) => state.stockTicker.tickerInfo


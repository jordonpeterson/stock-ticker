import {createAsyncThunk, createSlice} from '@reduxjs/toolkit'
import {getTickerData} from "./stockTickerAPI";

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
    },
    extraReducers(builder) {
        builder.addCase(loadTickerData.fulfilled, (state, action) => {
            state.tickerInfo = action.payload;
            state.status = 'success'
        })
    }
})

export const loadTickerData = createAsyncThunk('stockTicker/loadTickerData', async () => {
        const result = await getTickerData()
        return result
    }
)

export const {setStockTickerData} = stockTickerSlice.actions

export const selectStockTickerData = (state: any) => state.stockTicker.tickerInfo


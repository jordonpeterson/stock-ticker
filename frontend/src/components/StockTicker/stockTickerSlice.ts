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
        builder.addCase(loadTickerData.rejected, (state, action) => {
            state.status = 'failed'
        })
        builder.addCase(loadTickerData.pending, (state, action) => {
            state.tickerInfo = initialState.tickerInfo
            state.status = 'pending'
        })
    }
})

export const loadTickerData = createAsyncThunk('stockTicker/loadTickerData', async (ticker:string) => {
        const result = await getTickerData(ticker)
        return result
    }
)

export const {setStockTickerData} = stockTickerSlice.actions

export const selectStockTickerData = (state: any) => state.stockTicker.tickerInfo


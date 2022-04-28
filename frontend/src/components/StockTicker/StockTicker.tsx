import React, {FC, useState} from 'react';
import styles from './StockTicker.module.css';
import DisplayTable from "../DisplayTable/DisplayTable";
import {TickerData} from "../../models/TickerData";

interface StockTickerProps {
}

let mockTickerData: TickerData = {
    max_price: 0,
    min_price: 0,
    avg_price: 0,
    max_volume: 0,
    min_volume: 0,
    avg_volume: 0
}

const StockTicker: FC<StockTickerProps> = () => {
    const [tickerData, setTickerData] = useState(mockTickerData)
    const [ticker, setTicker] = useState('')

    async function handleSubmit(event: any) {
        event.preventDefault()
        if (ticker) {
            console.log('Selected Ticker: ' + ticker)
            const response = await getTickerData(ticker)
            setTickerData(response)
        }
    }

    async function handleChange(event: any) {
        await setTicker(event.target.value)
    }

    async function getTickerData(ticker: string = 'AAPL',
                                 startDate: string = '2020-01-01',
                                 endDate: string = '2020-12-31') {

        const url = `https://4u13q8f5d9.execute-api.us-east-2.amazonaws.com/prod/stock-ticker?` +
            `ticker=${ticker}&startDate=${startDate}&endDate=${endDate}`
        const result = await fetch(url)
        const response: TickerData = await result.json()
        console.log(response)
        return response
    }

    return (
        <div className={styles.StockTicker} data-testid="StockTicker">
            <form onSubmit={handleSubmit}>
                <label>
                    Enter a Stock Ticker
                    <input type="text" name="ticker" value={ticker} onChange={handleChange}/>
                </label>
                <input type="submit" value="Search"/>
            </form>
            <DisplayTable tickerData={tickerData}></DisplayTable>
        </div>
    )
};

export default StockTicker;

import React, {FC, useState} from 'react';
import styles from './StockTicker.module.css';
import DisplayTable from "../DisplayTable/DisplayTable";
import {useSelector} from "react-redux";
import {selectStockTickerData} from "./stockTickerSlice";
import {getTickerData} from "./stockTickerAPI";

interface StockTickerProps {
}

const StockTicker: FC<StockTickerProps> = () => {
    const [tickerData, setTickerData] = useState(useSelector(selectStockTickerData))
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

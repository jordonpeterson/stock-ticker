import React, {FC, useState} from 'react';
import styles from './StockTicker.module.scss';
import DisplayTable from "../DisplayTable/DisplayTable";
import {useDispatch, useSelector} from "react-redux";
import {loadTickerData, selectStockTickerData} from "./stockTickerSlice";

interface StockTickerProps {
}

const StockTicker: FC<StockTickerProps> = () => {
    const dispatch = useDispatch();
    const tickerData = useSelector(selectStockTickerData)
    const [ticker, setTicker] = useState('')

    async function handleSubmit(event: any) {
        event.preventDefault()
        if (ticker) {
            console.log('Selected Ticker: ' + ticker)
            dispatch(loadTickerData(ticker))
        }
    }

    async function handleChange(event: any) {
        await setTicker(event.target.value)
    }

    return (
        <div className={styles.StockTicker} data-testid="StockTicker">
            <div id="ticker-form-wrapper">
                <form onSubmit={handleSubmit}>
                    <label>
                        Enter a Stock Ticker
                        <input type="text" name="ticker" value={ticker} onChange={handleChange}/>
                    </label>
                    <input id="ticker-form-submit-button" type="submit" value="Search"/>
                </form>
            </div>
            <DisplayTable tickerData={tickerData}></DisplayTable>
        </div>
    )
};

export default StockTicker;

import React, {FC, useState} from 'react';
import styles from './StockTicker.module.scss';
import DisplayTable from "../DisplayTable/DisplayTable";
import {useDispatch, useSelector} from "react-redux";
import {loadTickerData, selectStockTickerData, selectStockTickerStatus} from "./stockTickerSlice";

interface StockTickerProps {
}

const StockTicker: FC<StockTickerProps> = () => {
    const dispatch = useDispatch();
    const tickerData = useSelector(selectStockTickerData)
    const tickerStatus: string = useSelector(selectStockTickerStatus)
    const [ticker, setTicker] = useState('')

    function isLoading(status: string): boolean {
        return status === 'pending'
    }

    async function handleSubmit(event: any) {
        event.preventDefault()
        if (ticker && ticker.trim()) {
            console.log('Selected Ticker: ' + ticker.trim())
            dispatch(loadTickerData(ticker.trim()))
        }
    }

    async function handleChange(event: any) {
        await setTicker(event.target.value)
    }

    return (
        <div className={styles.StockTicker} data-testid="StockTicker">
            <div id="ticker-form-wrapper">
                <form id="ticker-form" onSubmit={handleSubmit}>
                    <label>
                        Enter a Stock Ticker
                    </label>
                    <input type="text" name="ticker" value={ticker} onChange={handleChange}/>

                    <input id="ticker-form-submit-button" type="submit" value="Search"/>
                </form>
            </div>

            <DisplayTable tickerData={tickerData} displayLoadingIndicator={isLoading(tickerStatus)}></DisplayTable>
        </div>
    )
};

export default StockTicker;

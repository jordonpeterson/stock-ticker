import React, {FC} from 'react';
import styles from './DisplayTable.module.scss';
import {TickerData} from "../../models/TickerData";

interface DisplayTableProps {
    tickerData: TickerData,
    displayLoadingIndicator: boolean
}

const DisplayTable: FC<DisplayTableProps> = ({tickerData, displayLoadingIndicator}) => {
    if (displayLoadingIndicator) {
        return <h1>Loading Results...</h1>
    }
    return (
        <div className={styles.DisplayTable} data-testid="DisplayTable">
            <table>
                <tbody>
                <tr id="table-headers">
                    <th id="th-1">Item</th>
                    <th id="th-2">Maximum</th>
                    <th id="th-3">Minimum</th>
                    <th id="th-4">Average</th>
                </tr>
                <tr id="row-1" className={"odd-row"}>
                    <td id="tr1-1">Price</td>
                    <td id="tr1-2">${tickerData.max_price}</td>
                    <td id="tr1-3">${tickerData.min_price}</td>
                    <td id="tr1-4">${tickerData.avg_price}</td>
                </tr>
                <tr id="row-2" className={"even-row"}>
                    <td id="tr2-1">Volume</td>
                    <td id="tr2-2">{tickerData.max_volume}</td>
                    <td id="tr2-3">{tickerData.min_volume}</td>
                    <td id="tr2-4">{tickerData.avg_volume}</td>
                </tr>
                <tr id="row-3" className={"odd-row"}>
                    <td id="tr3-1"></td>
                    <td id="tr3-2"></td>
                    <td id="tr3-3"></td>
                    <td id="tr3-4"></td>
                </tr>
                </tbody>
            </table>
        </div>
    )
};

export default DisplayTable;

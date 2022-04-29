import React, {FC} from 'react';
import styles from './DisplayTable.module.scss';
import {TickerData} from "../../models/TickerData";

interface DisplayTableProps {
    tickerData: TickerData
}

const DisplayTable: FC<DisplayTableProps> = ({tickerData}) => (
    <div className={styles.DisplayTable} data-testid="DisplayTable">
        <table>
            <tbody>
            <tr>
                <th>Item</th>
                <th>Maximum</th>
                <th>Minimum</th>
                <th>Average</th>
            </tr>
            <tr>
                <td>Price</td>
                <td>{tickerData.max_price}</td>
                <td>{tickerData.min_price}</td>
                <td>{tickerData.avg_price}</td>
            </tr>
            <tr>
                <td>Volume</td>
                <td>{tickerData.max_volume}</td>
                <td>{tickerData.min_volume}</td>
                <td>{tickerData.avg_volume}</td>
            </tr>
            </tbody>
        </table>
    </div>
);

export default DisplayTable;

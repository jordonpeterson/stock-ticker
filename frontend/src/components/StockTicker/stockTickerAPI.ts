import {TickerData} from "../../models/TickerData";

export async function getTickerData(ticker: string = 'AAPL',
                             startDate: string = '2020-01-01',
                             endDate: string = '2020-12-31') {

    const url = `https://4u13q8f5d9.execute-api.us-east-2.amazonaws.com/prod/stock-ticker?` +
        `ticker=${ticker}&startDate=${startDate}&endDate=${endDate}`
    const result = await fetch(url)
    const response: TickerData = await result.json()
    console.log(response)
    return response
}
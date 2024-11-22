from fastapi import FastAPI
import json

app = FastAPI()

#чтение json-файла с тарифами
with open('rates.json') as rates_file:
    rates = json.load(rates_file)
    rates_file.close()

#основной роут расчета и возвращения стоимости страхования
@app.get('/date={date}&cargo_type={cargo_type}&price={price}')
def get_sum(date, cargo_type: str, price: int):
    current_rates_by_date = rates[date]
    for i in range(0, len(current_rates_by_date)):
        if current_rates_by_date[i]["cargo_type"] == cargo_type:
            current_rate = current_rates_by_date[i]["rate"]
    ins_price = price * float(current_rate)
    return ins_price
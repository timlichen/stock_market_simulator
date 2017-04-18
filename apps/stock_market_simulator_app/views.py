from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.utils.safestring import SafeString
import ystockquote
import json
from pprint import pprint
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'stock_market_sim_templates/index.html')

def posted_historic_stock_data(request):

    start = request.POST['start'].split("/")
    end = request.POST['end'].split("/")
    symbol = request.POST['symbol']

    date_start = datetime(int(start[2]), int(start[0]), int(start[1])).strftime('%Y-%m-%d')


    date_end = datetime(int(end[2]), int(end[0]), int(end[1])).strftime('%Y-%m-%d')


    historic_stock_data  = ystockquote.get_historical_prices(symbol, date_start, date_end)


    print type(historic_stock_data)
    # return historic_stock_data
    # messages.info(request, historic_stock_data)

    # send data through reverse route, then display
    # set validations for date
    context = { "historic_stock_data": SafeString(historic_stock_data)}
    return render(request, 'stock_market_sim_templates/hist_results.html', context)
    # return redirect(reverse('stock_market_sim_app:index'))

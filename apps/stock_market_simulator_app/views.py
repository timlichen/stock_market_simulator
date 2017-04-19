from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.utils.safestring import SafeString
from django.http import JsonResponse
import ystockquote

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
    historic_stock_data  = JsonResponse(ystockquote.get_historical_prices(symbol, date_start, date_end))

    print ystockquote.get_200_sma('googl')


    return historic_stock_data
    # context = { "historic_stock_data": SafeString(historic_stock_data)}
    # return render(request, 'stock_market_sim_templates/hist_results.html', context)

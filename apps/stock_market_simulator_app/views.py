from django.shortcuts import render, redirect
import ystockquote
from django.utils.safestring import SafeString
from pprint import pprint
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'stock_market_sim_templates/index.html')

def posted_historic_stock_data(request):

    start = request.POST['start'].split("/")
    end = request.POST['end'].split("/")

    try:
        date_start = datetime(int(start[2]), int(start[0]), int(start[1])).strftime('%Y-%m-%d')
        date_end = datetime(int(start[2]), int(start[0]), int(start[1])).strftime('%Y-%m-%d')
    except:
        return redirect("/")

    print date_start
    print date_end

    pprint(ystockquote.get_historical_prices('GOOGL', '2013-01-03', '2013-01-08'))

    # send data through reverse route, then display
    # set validations for date

    return redirect("/")

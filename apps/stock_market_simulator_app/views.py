from django.shortcuts import render, redirect
import ystockquote
from django.utils.safestring import SafeString
from pprint import pprint

# Create your views here.

def index(request):
    return render(request, 'stock_market_sim_templates/index.html')

def posted_historic_stock_data(request):
    # print request.POST['symbol']
    # print request.POST['start']
    # print request.POST['end']
    # pprint(dir(ystockquote))
    print ystockquote.get_bid_realtime('NFLX')
    return redirect("/")

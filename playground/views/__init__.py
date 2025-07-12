from playground.views.stack_views import *
from playground.views.queue_views import *
from playground.views.deque_views import *
from playground.views.linked_list_views import *
from playground.views.dlinked_list_views import *
from playground.views.minh_views import *
from playground.views.maxh_views import *
from playground.views.bt_views import *
from playground.views.bst_views import *
from playground.views.avl_views import *
from playground.views.redblack_views import *
from playground.views.graph_views import *
from playground.views.wgraph_views import *
from playground.views.dgraph_views import *
from playground.views.pq_views import *
from playground.views.ht_views import *
from playground.views.set_views import *
from playground.views.tup_views import *
from playground.views.dict_views import *

from django.shortcuts import render
from django.shortcuts import render

def home(request):
    return render(request, 'playground/home.html')

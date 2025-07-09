from django.urls import path
from playground.views import (
    disjointset_views,
    stack_views,
    queue_views,
    linked_list_views,
    dlinked_list_views,
    minh_views,
    maxh_views,
    bst_views,
    bt_views,
    deque_views,
    set_views,
    dict_views,
    tup_views,
    avl_views,
    redblack_views,
    seg_views,
    fenwicktree_views,
    trie_views,
    graph_views,
    wgraph_views,
    dgraph_views,
    pq_views,
    cb_views,
    skiplist_views,
    rope_views,
    ht_views,
    bitset_views,
    matrix_views,
    heapq_views,
)
from playground.views import home

urlpatterns = [
    path('', home, name='home'),

    # stack views
    path('stack/', stack_views.stack_view, name='stack'),
    path('stack/push/', stack_views.push, name='push'),
    path('stack/pop/', stack_views.pop, name='pop'),
    path('stack/peek/', stack_views.peek, name='peek'),

    # queue views
    path('queue/', queue_views.queue_view, name='queue'),

    # deque
    path('deque/', deque_views.deque_view, name='deque'),

    # linked list views
    path('linked-list/', linked_list_views.linked_list_view, name='linked_list'),

    # doubly linked list views
    path('dlinked-list/', dlinked_list_views.dlinked_list_view, name='dlinked_list'),

    # set
    path('set/', set_views.set_view, name='set'),

    # dictionary
    path('dictionary/', dict_views.dict_view, name='dictionary'),

    # tuple
    path('tuple/', tup_views.tup_view, name='tuple'),

    # heap views
    path('min-heap/', minh_views.minh_view, name='minh'),
    path('max-heap/', maxh_views.maxh_view, name='maxh'),

    # tree views
    path('binary-tree/', bt_views.bt_view, name='bt'),
    path('binary-search-tree/', bst_views.bst_view, name='bst'),

    # AVL and Red-Black
    path('avl/', avl_views.avl_view, name='avl'),
    path('red-black/', redblack_views.redblack_view, name='red_black'),

    # Segment and Fenwick
    path('segment-tree/', seg_views.seg_view, name='segment_tree'),
    path('fenwick-tree/', fenwicktree_views.fenwicktree_view, name='fenwicktree'),

    # Trie
    path('trie/', trie_views.trie_view, name='trie'),

    # Graphs
    path('graph/', graph_views.graph_view, name='graph'),
    path('weighted-graph/', wgraph_views.wgraph_view, name='weighted_graph'),
    path('directed-graph/', dgraph_views.dgraph_view, name='directed_graph'),

    # Disjoint Set
    path('disjointset/', disjointset_views.disjointset_view, name='disjointset'),

    # Specialized structures
    path('priority-queue/', pq_views.pq_view, name='priority_queue'),
    path('circular-buffer/', cb_views.cb_view, name='circular_buffer'),
    path('skip-list/', skiplist_views.skiplist_view, name='skip_list'),
    path('rope/', rope_views.rope_view, name='rope'),
    path('hash-table/', ht_views.ht_view, name='hash_table'),
    path('bitset/', bitset_views.bitset_view, name='bitset'),

    # Matrix and heapq
    path('matrix/', matrix_views.matrix_view, name='matrix'),
    path('heapq/', heapq_views.heapq_view, name='heapq'),
]

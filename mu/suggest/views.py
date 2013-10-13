import pdb
import simplejson
from operator import itemgetter
from datetime import datetime
from django.http import HttpResponse
from django.core.cache import get_cache
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    """
    Landing method
    """
    if True:
        return render_to_response('home/home.html',{}, RequestContext(request, { }) )
    else:
        return render_to_response('home/home.html',{}, RequestContext(request, { }) )

def autosuggest(request):
    """
    Auto suggest landing method
    """
    try:
        if (request.GET.has_key('search')):
            searchWord = request.GET['search'].lower()
            airList = []
            airList, group_dict = searchincludespace(searchWord)
            group_dict= sorted(group_dict.items(), key=itemgetter(1), reverse=True)
            result = [ group_dict[:4], airList ]
            return HttpResponse(simplejson.dumps(result))
        else:
            return HttpResponse('{"result":"failed","desc":"No Matches Found"}')
    except Exception,e:
        print e
        return HttpResponse('{"result":"failed","desc":"No Matches Found"}')

def search(word):
    """
    Search for single word
    """
    r = get_cache('autosuggest')
    hashes_list  = r._client.zrange(name="task:%s"%word,start=0, end=-1)
    return answer(hashes_list)

def searchincludespace(words):
    """
    Search in case of multiple words
    """
    r = get_cache('autosuggest')
    set_list = ["task:%s"%word for word in words.split(' ')]
    res = r._client.zinterstore("res", set_list)
    hashes_list = r._client.zrange(name="res", start=0, end=-1)
    return answer(hashes_list)

def answer(hashes_list):
    """
    All the sentences corresponding
    to the hashes dreived
    """
    suggList = []
    group_dict = {}
    r = get_cache('autosuggest')
    for hashes in reversed(hashes_list):
        di = {}
        result = r._client.hget("task", hashes)
        rlist = result.split(':')
        di['msg'] = rlist[0]
        di['nameid'] = r._client.hget(hashes, 'nameid')
        di['name'] = r._client.hget(hashes, 'name')
        di['pid'] = hashes
        ctime = r._client.hget(hashes, 'ctime')
        ctime = datetime.strptime(ctime.split(' ')[0], '%Y-%m-%d')
        di['ctime'] = str(ctime.day) + ' ' + ctime.strftime("%B") + ' ' + str(ctime.year)
        gp = r._client.hget(hashes, 'group')
        di['group'] = gp
        if group_dict.has_key(gp): 
            group_dict[gp]+=1
        else:
            group_dict[gp] = 1;
        suggList.append(di)
    return suggList, group_dict

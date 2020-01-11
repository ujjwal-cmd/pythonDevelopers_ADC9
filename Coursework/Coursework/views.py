def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['title',])

    found_entries = Finb.objects.filter(entry_query).order_by('-pub_date')
    for result in found_entries:
        print result.title
        return render_to_response('search_results.html',
                      { 'query_string': query_string, 'found_entries': found_entries, 'result':result },
                      context_instance=RequestContext(request))
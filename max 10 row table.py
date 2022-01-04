def top_10(dictionary, max_entries = 10):
    if isinstance(dictionary, str):
        return '<td>'+dictionary+'</td>'
    s = ['<!-- wp:table --><figure class="wp-block-table"><table><tbody>']
    for n, [key, value] in enumerate(dictionary.items()):
        if n == max_entries:
            break
        s.append('<tr><td>%s</td>' % key)
        # s.append('<tr><td>'+key+'</td>')
        s.append('<td>%s</td>' % value)
        s.append('</tr>')
    s.append('</tbody></table></figure><!-- /wp:table -->')
    return ''.join(s)

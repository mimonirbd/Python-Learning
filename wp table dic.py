def table_dict(dictionary):
    if isinstance(dictionary, str):
        return '<td>'+dictionary+'</td>'
    s = ['<!-- wp:table --><figure class="wp-block-table"><table><tbody>']
    for key, value in dictionary.items():
        s.append('<tr><td>%s</td>' % key)
        # s.append('<tr><td>'+key+'</td>')
        s.append('<td>%s</td>' % value)
        s.append('</tr>')
    s.append('</tbody></table></figure><!-- /wp:table -->')
    return ''.join(s)

print(table_dict(dicts))

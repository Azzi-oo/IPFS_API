from django.http import JsonResponse
from ipfshttpclient import connect

def ipfs_add(request):
    if request.method == 'POST':
        file_to_add = request.FILES['file']
        client = connect('/ip4/127.0.0.1/tcp/5001')
        res = client.add(file_to_add)
        return JsonResponse({'ipfs_hash': res['Hash']})
    else:
        return JsonResponse({'error': "Method don't supported"}, status=405)
    

def ipfs_cat(request, ipfs_hash):
    client = connect('/ip4/127.0.0.1/tcp/5001')
    data = client.cat(ipfs_hash)
    return JsonResponse({'data': data})

def ipfs_publish(request):
    if request.method == 'POST':
        ipfs_hash = request.POST['ipfs_hash']
        client = connect('/ip4/127.0.0.1/tcp/5001')
        res = client.name.publish(ipfs_hash)
        return JsonResponse({'name': res['Name']})
    else:
        return JsonResponse({'error': "Method don't supported"}, status=405)
    
import requests
payload = [{'npm': 51423033,
            'nama': 'M Yusuf Ghazali',
            'kelas': '1IA03',
            'fakultas': 'Teknologi Industri',
            'Prodi': 'Teknik Informatika'}, 
           {'npm': 10123851, 
            'nama': 'M Mumtaz Yafi',
            'kelas': '1KA07',
            'fakultas': 'Ilmu Komputer',
            'Prodi': 'Sistem Informasi'}, 
           {'npm': 11523209,
            'nama': 'Umar Mustafa Karim',
            'kelas': '1PA07',
            'fakultas': 'Psikologi',
            'prodi': 'Psikologi'}, 
           {'npm': 20323206,
            'nama': 'Rakha Fateh Ramadhan',
            'kelas': '1TB02',
            'fakultas': 'Sipil Perencanaan',
            'prodi': 'Teknik Arsitektur'}, 
           {'npm': 50423958,
            'nama': 'M Laudza Zidha Kusuma',
            'kelas': '1IA18',
            'fakultas': 'Teknologi Industri',
            'prodi': 'Teknik Informatika'}]

parameter = {'id': 5}
addPost = requests.post("https://httpbin.org/post", json=payload)
getPostId = requests.get("https://jsonplaceholder.typicode.com/posts", params=parameter)

if (len(getPostId.json()) > 0):
    print('Mencoba Melakukan Get Request')
    print('url:', getPostId.url)
    print('Payload:', getPostId.text)
    print('=============================')

if (addPost.status_code == 200 or addPost.status_code == 201):
    print('Mencoba Melakukan Post Request')
    print('Status Code:', addPost.status_code)
    print('Payload:', addPost.text)


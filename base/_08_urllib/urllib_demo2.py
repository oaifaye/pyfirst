# request:GET
import urllib.request
import time

domains = ['http://10.20.31.63',
           'http://10.20.31.64'
            ]
urls = ['/v?seconds=1.573387026786804&session_id=7b8280a0094e4983bfbe49f8ea75bb39&os_version=13.1.1&timestamp=1590112855859&remark=&app_id=893e6176-2ccc-4c34-9c67-b426c6174b4c&platform=iOS&app_ver=2.7.40&net_status=4G&version=1&appId=893e6176-2ccc-4c34-9c67-b426c6174b4c&uuid=6cdfab38b08545db8e2cdcaefe2b5f5d&type=customEvent&ph_name=iPhone%20xs&page_type=news&event_id=newsDetailReadOut&file_id=035682973&ph_brand_model=iPhone&ecAppId=44&ph_sys_revision_ver=13.1.1&nonce=6a8d590435dd4e728ad75be27b15a01b&longitude=&check_sum=087830411061bec38becd02ee49704df&sub_app_id=&ph_platform_sign=i&access_date=2020-05-22%2009%3A54%3A28&user_id=200157759&ph_sys_core_ver=13.1.1&valid_user=1&ph_product_line=apple&dev_id=6cdfab38b08545db8e2cdcaefe2b5f5d&api_token=84c37974-77d3-4af8-9988-113d2f0f9ceb&ip=169.254.95.76&ph_brand=apple&latitude=&',
        '/v?timestamp=1590112854286&session_id=7b8280a0094e4983bfbe49f8ea75bb39&os_version=13.1.1&remark=&app_id=893e6176-2ccc-4c34-9c67-b426c6174b4c&platform=iOS&app_ver=2.7.40&net_status=4G&ref_page_type=news&ref_page_id=newsId&version=1&appId=893e6176-2ccc-4c34-9c67-b426c6174b4c&uuid=6cdfab38b08545db8e2cdcaefe2b5f5d&type=customEvent&ph_name=iPhone%20xs&page_type=news&event_id=newsDetailRead&file_id=035682973&ph_brand_model=iPhone&ecAppId=44&ph_sys_revision_ver=13.1.1&nonce=1ff4586be6aa41b4bc80ad95e95e08a9&longitude=&check_sum=7f63dc0e5a019713b22e7ed9421ebea9&sub_app_id=&ph_platform_sign=i&access_date=2020-05-22%2009%3A54%3A28&user_id=200157759&ph_sys_core_ver=13.1.1&valid_user=1&ph_product_line=apple&dev_id=6cdfab38b08545db8e2cdcaefe2b5f5d&api_token=84c37974-77d3-4af8-9988-113d2f0f9ceb&ip=169.254.95.76&ph_brand=apple&latitude=&',
        '/v?api_token=30800d7c-3b6a-43f4-8730-02e36bc2ab2f&type=customEvent&nonce=1874a8a6-dcc3-4fac-bc4e-94396b976ee3&version=1&deviceId=8169d72049eda921&platform=Android&event_id=newsList&ecAppId=44&check_sum=78d64087c5fcda88588ca33cac637e9a&appId=893e6176-2ccc-4c34-9c67-b426c6174b4c&channel_id=44_GUIDELIST_1040000000000000&timestamp=1590050548586',
        '/v?ecAppId=44&check_sum=7159cca5f6c032dd97cb899f0d12bb78&appId=893e6176-2ccc-4c34-9c67-b426c6174b4c&api_token=30800d7c-3b6a-43f4-8730-02e36bc2ab2f&imei=862998044560169&type=startApp&nonce=82f1b0c6-d7bd-48e9-91ba-e846d9720304&version=1&deviceId=8169d72049eda921&platform=Android&timestamp=1590050381890',
        '/v?timestamp=1590046559446&session_id=77416f3702a74559bc652388427644d3&os_version=13.3.1&remark=&app_id=893e6176-2ccc-4c34-9c67-b426c6174b4c&platform=iOS&app_ver=2.7.30&net_status=4G&version=1&appId=893e6176-2ccc-4c34-9c67-b426c6174b4c&uuid=55e54701c95c4c639a9d10501d1f2b21&type=startApp&ph_name=iPhone&ph_brand_model=iPhone&ecAppId=44&ph_sys_revision_ver=13.3.1&nonce=7b04fd9fe1b44ecab6a03c603036c596&longitude=&check_sum=7d01e226929992fa7dfec69b54f46f37&sub_app_id=&ph_platform_sign=i&access_date=2020-05-21%2015%3A35%3A59&user_id=200157744&ph_sys_core_ver=13.3.1&valid_user=1&ph_product_line=apple&dev_id=55e54701c95c4c639a9d10501d1f2b21&api_token=cee1995f-a683-48d0-8916-0e82ef26d0ba&ip=169.254.26.79&imei=&spreader=APP%20Store&ph_brand=apple&latitude=&',
        ]

while True:
    for domain in domains:
        for url in urls:
            response = urllib.request.urlopen(domain+url)
            print(response.read().decode('utf-8'))
    time.sleep(1)